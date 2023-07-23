from sequence.qkd.BB84 import pair_bb84_protocols
from sequence.qkd.cascade import pair_cascade_protocols
from sequence.kernel.process import Process
from sequence.kernel.event import Event

from keys_exception import NoMoreKeysException

import numpy

class Transceiver:

    def __init__(self, qkd_node, qkd_node_p):
        self.qkd_node = qkd_node
        self.qkd_node_p = qkd_node_p
        self.qkd_node_km = None

    def add_key_manager(self, qkd_node_km):
        self.qkd_node_km = qkd_node_km
        self.qkd_node_p.add_key_manager(qkd_node_km)

    def send_message(self, tl, plaintext, rate, forwarding=False):
        if forwarding:
            process = Process(self.qkd_node_p, "start", [plaintext, tl, rate, forwarding])
            event = Event(tl.now(), process)
            tl.schedule(event)
        else:
            time = numpy.random.exponential(rate, 1)[0]
            process = Process(self.qkd_node_p, "start", [plaintext, tl, rate])
            event = Event(tl.now() + (time * 1000000000000), process)
            tl.schedule(event)
        
        return
 
    def start_qkd(self):
        # Se non è il sender rieseguire pair
        # if self.qkd_node.protocol_stack[0].role != 0 or self.qkd_node.protocol_stack[1].role != 0:
        #     pair_bb84_protocols(self.qkd_node.protocol_stack[0], self.qkd_node.protocol_stack[0].another)
        #     pair_cascade_protocols(self.qkd_node.protocol_stack[1], self.qkd_node.protocol_stack[1].another)
            
        self.qkd_node_km.send_request()
        

    