from enum import Enum, auto
import json
import numpy

from sequence.topology.node import Node
from sequence.protocol import Protocol
from sequence.message import Message
from sequence.qkd.BB84 import pair_bb84_protocols
from sequence.qkd.cascade import pair_cascade_protocols
from sequence.kernel.process import Process
from sequence.kernel.event import Event

from onetimepad import OneTimePad

class MsgType(Enum):

    TEXT_MESS = auto()


class MessagingProtocol(Protocol):
    
    delivered_messages = 0
    dropped_messages = 0
    sent_messages = 0

    def __init__(self, own: Node, name: str, other_name: str, other_node: str, superQKD):
        super().__init__(own, name)
        self.own = own
        own.protocols.append(self)
        self.other_name = other_name
        self.other_node = other_node
        self.super_qkd = superQKD
        self.key_manager = None

    def init(self):
        pass

    def start(self, text: str, tl, rate, forwarding=False):
        if len(self.key_manager.keys) > 0:
            key = self.key_manager.consume()
            key = key.to_bytes((key.bit_length() + 7) // 8, 'big')
            
            packet = json.loads(text)
            
            message = packet["payload"]
            message = bytes(message) # b'str'
            
            key = key[0:len(message)]
            
            ciphertext = OneTimePad.encrypt(message, key)
            ciphertext = list(ciphertext)
            
            packet["payload"] = ciphertext
            
            new_msg = Message(MsgType.TEXT_MESS, self.other_name)
            new_msg.payload = json.dumps(packet)
            new_msg.protocol_type = type(self)
            
            self.own.send_message(self.other_node, new_msg)
            
            if not forwarding:
                MessagingProtocol.sent_messages += 1
                print(f"[{self.own.name}]\nMessage sent. At simulation time: {self.own.timeline.now() / 1000000000000} s\n")
                
        else:
            MessagingProtocol.dropped_messages += 1
            print(f"[{self.own.name}]\nMessage dropped. At simulation time: {self.own.timeline.now() / 1000000000000} s\n")
        
        if not forwarding:
            time = numpy.random.exponential(rate, 1)[0]
            process = Process(self, "start", [text, tl, rate])
            event = Event(tl.now() + (time * 1000000000000), process)
            tl.schedule(event)
        
        return
        

    def received_message(self, src: str, msg: Message):
        assert msg.msg_type == MsgType.TEXT_MESS
        
        key = self.key_manager.consume()
        key = key.to_bytes((key.bit_length() + 7) // 8, 'big')

        packet = json.loads(msg.payload)
        
        message = packet["payload"]
        message = bytes(message) # b'str'
        
        key = key[0:len(message)]
        
        plaintext = OneTimePad.decrypt(message, key)

        if packet["dest"] == self.super_qkd.name:
            MessagingProtocol.delivered_messages += 1
            
            print(f"[{self.own.name}]\nMessage received. At simulation time: {self.own.timeline.now() / 1000000000000} s")
            print(f"Encrypted Message: {message}")
            print(f"Decrypted Message: {plaintext}\n")

        else:
            packet["payload"] = list(plaintext)
            print(f"[{self.own.name}]\nForwarding... At simulation time: {self.own.timeline.now() / 1000000000000} s\n")
            self.super_qkd.send_message(self.own.timeline, packet["dest"], json.dumps(packet), True)

    def add_key_manager(self, key_manager):
        self.key_manager = key_manager
        
