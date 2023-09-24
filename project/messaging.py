from enum import Enum, auto
import json
import numpy
import collections

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

    # For Metrics
    delivered_messages = 0
    dropped_messages = 0
    sent_messages = 0

    d = {
        'Packet': [],
        'Source': [],
        'Destination': [],
        'Sent': [],
        'Delivered': [],
        'Dropped': [],
        'Num. Hop': [],
        'Sending Time': [],
        'Sim. Time': [],
        'Tot. Time': []
    }

    def __init__(self, own: Node, name: str, other_name: str, other_node: str, superQKD):
        super().__init__(own, name)
        self.own = own
        own.protocols.append(self)
        self.other_name = other_name
        self.other_node = other_node
        self.super_qkd = superQKD
        self.key_manager = None
        self.rate = None
        self.del_mess = 0
        self.drop_mess = 0
        self.sent_mess = 0
        self.buffer = collections.deque()

    def init(self):
        pass

    # evento che viene schedulato dal keymanager appena una chiave viene generata
    def send(self, tl):
        if len(self.buffer) > 0:
            key = self.key_manager.consume()
            key = key.to_bytes((key.bit_length() + 7) // 8, 'big')

            packet = json.loads(self.buffer.pop())

            message = packet["payload"]
            message = bytes(message) # b'str'
            
            key = key[0:len(message)]
            
            ciphertext = OneTimePad.encrypt(message, key)
            ciphertext = list(ciphertext)
            
            packet["payload"] = ciphertext
            
            new_msg = Message(MsgType.TEXT_MESS, self.other_name)
            new_msg.payload = json.dumps(packet)
            new_msg.protocol_type = type(self)
            
            #send_message QKDNode
            self.own.send_message(self.other_node, new_msg)

    def start(self, text: str, tl, forwarding):
        if not forwarding:
            print(f"[{self.own.name}]\nMessage sent. At simulation time: {self.own.timeline.now() * 1.0e-12} s\n")
            MessagingProtocol.sent_messages += 1
            self.sent_mess += 1
            time = numpy.random.exponential(self.rate, 1)[0]
            process = Process(self, "start", [text, tl, False])
            event = Event(tl.now() + (time * 1000000000000), process)
            tl.schedule(event)

        if len(self.buffer) == 0 and len(self.key_manager.keys) > 0:
            
            self.buffer.appendleft(text)
            self.send(tl)
            # key = self.key_manager.consume()
            # key = key.to_bytes((key.bit_length() + 7) // 8, 'big')
            
            # packet = json.loads(text)
            
            # message = packet["payload"]
            # message = bytes(message) # b'str'
            
            # key = key[0:len(message)]
            
            # ciphertext = OneTimePad.encrypt(message, key)
            # ciphertext = list(ciphertext)
            
            # packet["payload"] = ciphertext
            
            # new_msg = Message(MsgType.TEXT_MESS, self.other_name)
            # new_msg.payload = json.dumps(packet)
            # new_msg.protocol_type = type(self)
            
            # #send_message QKDNode
            # self.own.send_message(self.other_node, new_msg)

        else:
            self.buffer.appendleft(text)
            
        # if len(self.key_manager.keys) > 0:
        #     key = self.key_manager.consume()
        #     key = key.to_bytes((key.bit_length() + 7) // 8, 'big')
            
        #     packet = json.loads(text)
            
        #     message = packet["payload"]
        #     message = bytes(message) # b'str'
            
        #     key = key[0:len(message)]
            
        #     ciphertext = OneTimePad.encrypt(message, key)
        #     ciphertext = list(ciphertext)
            
        #     packet["payload"] = ciphertext
            
        #     new_msg = Message(MsgType.TEXT_MESS, self.other_name)
        #     new_msg.payload = json.dumps(packet)
        #     new_msg.protocol_type = type(self)
            
        #     self.own.send_message(self.other_node, new_msg)
                
        # else:
        #     packet = json.loads(text)
        #     MessagingProtocol.dropped_messages += 1
        #     self.drop_mess += 1

        #     if packet["hop"] == 0:
        #         MessagingProtocol.append_metrics(
        #             packet["src"], packet["dest"], False, False, self.own.name, packet["hop"], 
        #             packet["time"]* 1.0e-12, self.own.timeline.now() * 1.0e-12, 
        #             (self.own.timeline.now() * 1.0e-12) - (packet["time"] * 1.0e-12))
        #     else:
        #         MessagingProtocol.append_metrics(
        #             packet["src"], packet["dest"], True, False, self.own.name, packet["hop"], 
        #             packet["time"] * 1.0e-12, self.own.timeline.now() * 1.0e-12, 
        #             (self.own.timeline.now() * 1.0e-12) - (packet["time"] * 1.0e-12))

        #     print(f"[{self.own.name}]\nMessage dropped. At simulation time: {self.own.timeline.now() * 1.0e-12} s\n")

    def received_message(self, src: str, msg: Message):
        assert msg.msg_type == MsgType.TEXT_MESS
        
        key = self.key_manager.consume()
        key = key.to_bytes((key.bit_length() + 7) // 8, 'big')

        packet = json.loads(msg.payload)
        
        message = packet["payload"]
        message = bytes(message) # b'str'
        
        key = key[0:len(message)]
        
        plaintext = OneTimePad.decrypt(message, key)

        packet["hop"] += 1

        if packet["dest"] == self.super_qkd.name:
            MessagingProtocol.delivered_messages += 1
            self.del_mess += 1
            MessagingProtocol.append_metrics(
                packet["src"], packet["dest"], True, True, None, packet["hop"], 
                packet["time"] * 1.0e-12, self.own.timeline.now() * 1.0e-12, 
                (self.own.timeline.now() * 1.0e-12) - (packet["time"] * 1.0e-12))
            
            print(f"[{self.own.name}]\nMessage received. At simulation time: {self.own.timeline.now() * 1.0e-12} s")
            print(f"Encrypted Message: {message}")
            print(f"Decrypted Message: {plaintext}\n")

        else:
            packet["payload"] = list(plaintext)
            print(f"[{self.own.name}]\nForwarding... At simulation time: {self.own.timeline.now() * 1.0e-12} s\n")
            self.super_qkd.send_message(self.own.timeline, packet["dest"], json.dumps(packet), True)

    def add_key_manager(self, key_manager):
        self.key_manager = key_manager

    @staticmethod
    def append_metrics(src, dest, sent, deliv, drop, num_hop, send_time, sim_time, time):
        MessagingProtocol.d["Packet"].append(len(MessagingProtocol.d["Packet"]))
        MessagingProtocol.d["Source"].append(src)
        MessagingProtocol.d["Destination"].append(dest)
        MessagingProtocol.d["Sent"].append(sent)
        MessagingProtocol.d["Delivered"].append(deliv)
        MessagingProtocol.d["Dropped"].append(drop)
        MessagingProtocol.d["Num. Hop"].append(num_hop)
        MessagingProtocol.d["Sending Time"].append(send_time)
        MessagingProtocol.d["Sim. Time"].append(sim_time)
        MessagingProtocol.d["Tot. Time"].append(time)


        
