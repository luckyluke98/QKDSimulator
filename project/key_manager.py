from sequence.kernel.process import Process
from sequence.kernel.event import Event

import numpy

from memory_profiler import profile

class KeyManager():

    def __init__(self, own, timeline, keysize, num_keys):
        self.own = own
        self.timeline = timeline
        self.lower_protocols = []
        self.keysize = keysize
        self.num_keys = num_keys
        self.keys = []
        self.mp = None
        # this is to avoid synchronization of sending events
        # self.last_pop_time = timeline.now()
        # self.next_pop_time = timeline.now()
        self.first = True
        self.count_keys = 0
        
    def send_request(self):
        for p in self.lower_protocols:
            p.push(self.keysize, self.num_keys)
            
    def pop(self, key):
        if len(self.keys) <= 0:
            self.first = True

        self.keys.append(key)
        self.count_keys += 1

        if self.first and len(self.mp.buffer) > 0:

            #time = numpy.random.exponential(self.mp.service_rate, 1)[0]
            time = self.mp.packet_rate
            process = Process(self.mp, "send", [self.timeline])
            event = Event(self.timeline.now(), process)
            self.timeline.schedule(event)

            self.first = False

        # if self.timeline.now() * 1.0e-12 == self.last_pop_time * 1.0e-12:
        #     # Per ogni chiave generata verifica se nel buffer ci sono pacchetti da inviare
        #     process = Process(self.mp, "send", [self.timeline])
        #     event = Event(self.next_pop_time, process)
        #     self.timeline.schedule(event)
        #     self.next_pop_time += 1
            
        # else:
        #     # Per ogni chiave generata verifica se nel buffer ci sono pacchetti da inviare
        #     process = Process(self.mp, "send", [self.timeline])
        #     event = Event(self.timeline.now(), process)
        #     self.timeline.schedule(event)
        #     self.last_pop_time = self.timeline.now()
        #     self.next_pop_time = self.last_pop_time + 1
        
    def consume(self):
        return self.keys.pop(0)

