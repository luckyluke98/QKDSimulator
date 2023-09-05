import time
import math
from sequence.kernel.timeline import Timeline
from sequence.topology.node import QKDNode
from sequence.components.optical_channel import OpticalChannel, QuantumChannel, ClassicalChannel

from sequence.kernel.process import Process
from sequence.kernel.event import Event


class CustomChannel(OpticalChannel):
    
    def __init__(self, name: str, timeline: "Timeline", attenuation: float, distance: int,
                 polarization_fidelity=1.0, light_speed=2e-4, bit_rate=-1):
        super().__init__(name, timeline, attenuation, distance, polarization_fidelity, light_speed)
        self.delay = -1

    def init(self) -> None:
        self.delay = round(self.distance / self.light_speed)

    def set_ends(self, sender: "Node", receiver: str) -> None:
        self.sender = sender
        self.receiver = receiver
        sender.assign_qchannel(self, receiver)

    def transmit(self, qubit: "Photon", source: "Node") -> None:
        
        assert self.delay >= 0, \
            "QuantumChannel init() function has not been run for {}".format(self.name)
        assert source == self.sender

        # check if polarization encoding and apply necessary noise
        if (qubit.encoding_type["name"] == "polarization") and (
                self.sender.get_generator().random() > self.polarization_fidelity):
            qubit.random_noise(self.get_generator())

        # schedule receiving node to receive photon at future time determined by light speed
        future_time = self.timeline.now() + self.delay
        process = Process(self.receiver, "receive_qubit", [source.name, qubit])
        event = Event(future_time, process)
        self.timeline.schedule(event)