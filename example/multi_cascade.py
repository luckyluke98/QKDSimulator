import math
import time 
import pandas as pd
from sequence.components.optical_channel import QuantumChannel, ClassicalChannel
from sequence.kernel.event import Event
from sequence.kernel.process import Process
from sequence.kernel.timeline import Timeline
from sequence.qkd.BB84 import pair_bb84_protocols
from sequence.qkd.cascade import pair_cascade_protocols
from sequence.topology.node import QKDNode

from time import sleep, perf_counter
from threading import Thread

import os
import sys
import psutil

class KeyManager():
    def __init__(self, timeline, keysize, num_keys):
        self.timeline = timeline
        self.lower_protocols = []
        self.keysize = keysize
        self.num_keys = num_keys
        #self.keys = []
        #self.times = []
        
    def send_request(self):
        for p in self.lower_protocols:
            p.push(self.keysize, self.num_keys) # interface for cascade to generate keys
            
    def pop(self, key): # interface for cascade to return generated keys
        return
        #self.keys.append(key)
        #self.times.append(self.timeline.now() * 1e-9)
        #print(self.timeline.now()* 1e-9)

def profile_node_memory(n):
            #BB84 & Cascade
    size = int(sys.getsizeof(n.protocol_stack[0].key_bits)) + \
            int(sys.getsizeof(n.protocol_stack[0].key_lengths)) + \
            int(sys.getsizeof(n.protocol_stack[0].basis_lists)) + \
            int(sys.getsizeof(n.protocol_stack[0].bit_lists)) + \
            int(sys.getsizeof(n.protocol_stack[0].keys_left_list)) + \
            int(sys.getsizeof(n.protocol_stack[0].end_run_times)) + \
            int(sys.getsizeof(n.protocol_stack[0].error_rates)) + \
            int(sys.getsizeof(n.protocol_stack[0].throughputs)) + \
            int(sys.getsizeof(n.protocol_stack[1].bits)) + \
            int(sys.getsizeof(n.protocol_stack[1].checksum_tables)) + \
            int(sys.getsizeof(n.protocol_stack[1].another_checksums)) + \
            int(sys.getsizeof(n.protocol_stack[1].index_to_block_id_lists)) + \
            int(sys.getsizeof(n.protocol_stack[1].valid_keys)) + \
            int(sys.getsizeof(n.protocol_stack[1].block_id_to_index_lists)) + \
            int(sys.getsizeof(n.protocol_stack[1].upper_protocols))

    return size


def task(n1, n2, n3, n4, n5, n6,n7,n8,n9,n10,
        n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,
        n21,n22,n23,n24,n25,n26,n27,n28,n29,n30,
        n31,n32,n33,n34,n35,n36,n37,n38,n39,n40,
        n41,n42):
    while True:
        sleep(3)
        s = profile_node_memory(n1) + \
            profile_node_memory(n2) + \
            profile_node_memory(n3) + \
            profile_node_memory(n4) + \
            profile_node_memory(n5) + \
            profile_node_memory(n6) + \
            profile_node_memory(n7) + \
            profile_node_memory(n8) + \
            profile_node_memory(n9) + \
            profile_node_memory(n10) + \
            profile_node_memory(n11) + \
            profile_node_memory(n12) + \
            profile_node_memory(n13) + \
            profile_node_memory(n14) + \
            profile_node_memory(n15) + \
            profile_node_memory(n16) + \
            profile_node_memory(n17) + \
            profile_node_memory(n18) + \
            profile_node_memory(n19) + \
            profile_node_memory(n20) + \
            profile_node_memory(n21) + \
            profile_node_memory(n22) + \
            profile_node_memory(n23) + \
            profile_node_memory(n24) + \
            profile_node_memory(n25) + \
            profile_node_memory(n26) + \
            profile_node_memory(n27) + \
            profile_node_memory(n28) + \
            profile_node_memory(n29) + \
            profile_node_memory(n30) + \
            profile_node_memory(n31) + \
            profile_node_memory(n32) + \
            profile_node_memory(n33) + \
            profile_node_memory(n34) + \
            profile_node_memory(n35) + \
            profile_node_memory(n36) + \
            profile_node_memory(n37) + \
            profile_node_memory(n38) + \
            profile_node_memory(n39) + \
            profile_node_memory(n40) + \
            profile_node_memory(n41) + \
            profile_node_memory(n42)

        print(s)
        print("==============================")
        

      
def test(sim_time, keysize):
    """
    sim_time: duration of simulation time (ms)
    keysize: size of generated secure key (bits)
    """
    # begin by defining the simulation timeline with the correct simulation time
    tl = Timeline(sim_time * 1e9)
    
    # Here, we create nodes for the network (QKD nodes for key distribution)
    n1 = QKDNode("n1", tl)
    n2 = QKDNode("n2", tl)

    n3 = QKDNode("n3", tl)
    n4 = QKDNode("n4", tl)

    n5 = QKDNode("n5", tl)
    n6 = QKDNode("n6", tl)

    n7 = QKDNode("n7", tl)
    n8 = QKDNode("n8", tl)

    n9 = QKDNode("n9", tl)
    n10 = QKDNode("n10", tl)

    n11 = QKDNode("n11", tl)
    n12 = QKDNode("n12", tl)

    n13 = QKDNode("n13", tl)
    n14 = QKDNode("n14", tl)

    n15 = QKDNode("n15", tl)
    n16 = QKDNode("n16", tl)

    n17 = QKDNode("n17", tl)
    n18 = QKDNode("n18", tl)

    n19 = QKDNode("n19", tl)
    n20 = QKDNode("n20", tl)

    n21 = QKDNode("n21", tl)
    n22 = QKDNode("n22", tl)

    n23 = QKDNode("n23", tl)
    n24 = QKDNode("n24", tl)

    n25 = QKDNode("n25", tl)
    n26 = QKDNode("n26", tl)

    n27 = QKDNode("n27", tl)
    n28 = QKDNode("n28", tl)

    n29 = QKDNode("n29", tl)
    n30 = QKDNode("n30", tl)

    n31 = QKDNode("n31", tl)
    n32 = QKDNode("n32", tl)

    n33 = QKDNode("n33", tl)
    n34 = QKDNode("n34", tl)

    n35 = QKDNode("n35", tl)
    n36 = QKDNode("n36", tl)

    n37 = QKDNode("n37", tl)
    n38 = QKDNode("n38", tl)

    n39 = QKDNode("n39", tl)
    n40 = QKDNode("n40", tl)

    n41 = QKDNode("n41", tl)
    n42 = QKDNode("n42", tl)

    pair_bb84_protocols(n1.protocol_stack[0], n2.protocol_stack[0])
    pair_cascade_protocols(n1.protocol_stack[1], n2.protocol_stack[1])

    pair_bb84_protocols(n3.protocol_stack[0], n4.protocol_stack[0])
    pair_cascade_protocols(n3.protocol_stack[1], n4.protocol_stack[1])

    pair_bb84_protocols(n5.protocol_stack[0], n6.protocol_stack[0])
    pair_cascade_protocols(n5.protocol_stack[1], n6.protocol_stack[1])

    pair_bb84_protocols(n7.protocol_stack[0], n8.protocol_stack[0])
    pair_cascade_protocols(n7.protocol_stack[1], n8.protocol_stack[1])

    pair_bb84_protocols(n9.protocol_stack[0], n10.protocol_stack[0])
    pair_cascade_protocols(n9.protocol_stack[1], n10.protocol_stack[1])

    pair_bb84_protocols(n11.protocol_stack[0], n12.protocol_stack[0])
    pair_cascade_protocols(n11.protocol_stack[1], n12.protocol_stack[1])

    pair_bb84_protocols(n13.protocol_stack[0], n14.protocol_stack[0])
    pair_cascade_protocols(n13.protocol_stack[1], n14.protocol_stack[1])

    pair_bb84_protocols(n15.protocol_stack[0], n16.protocol_stack[0])
    pair_cascade_protocols(n15.protocol_stack[1], n16.protocol_stack[1])

    pair_bb84_protocols(n17.protocol_stack[0], n18.protocol_stack[0])
    pair_cascade_protocols(n17.protocol_stack[1], n18.protocol_stack[1])

    pair_bb84_protocols(n19.protocol_stack[0], n20.protocol_stack[0])
    pair_cascade_protocols(n1.protocol_stack[1], n2.protocol_stack[1])

    pair_bb84_protocols(n21.protocol_stack[0], n22.protocol_stack[0])
    pair_cascade_protocols(n21.protocol_stack[1], n22.protocol_stack[1])

    pair_bb84_protocols(n23.protocol_stack[0], n24.protocol_stack[0])
    pair_cascade_protocols(n23.protocol_stack[1], n24.protocol_stack[1])

    pair_bb84_protocols(n25.protocol_stack[0], n26.protocol_stack[0])
    pair_cascade_protocols(n25.protocol_stack[1], n26.protocol_stack[1])

    pair_bb84_protocols(n27.protocol_stack[0], n28.protocol_stack[0])
    pair_cascade_protocols(n27.protocol_stack[1], n28.protocol_stack[1])

    pair_bb84_protocols(n29.protocol_stack[0], n30.protocol_stack[0])
    pair_cascade_protocols(n29.protocol_stack[1], n30.protocol_stack[1])

    pair_bb84_protocols(n31.protocol_stack[0], n32.protocol_stack[0])
    pair_cascade_protocols(n31.protocol_stack[1], n32.protocol_stack[1])

    pair_bb84_protocols(n33.protocol_stack[0], n34.protocol_stack[0])
    pair_cascade_protocols(n33.protocol_stack[1], n34.protocol_stack[1])

    pair_bb84_protocols(n35.protocol_stack[0], n36.protocol_stack[0])
    pair_cascade_protocols(n35.protocol_stack[1], n36.protocol_stack[1])

    pair_bb84_protocols(n37.protocol_stack[0], n38.protocol_stack[0])
    pair_cascade_protocols(n37.protocol_stack[1], n38.protocol_stack[1])

    pair_bb84_protocols(n39.protocol_stack[0], n40.protocol_stack[0])
    pair_cascade_protocols(n39.protocol_stack[1], n40.protocol_stack[1])

    pair_bb84_protocols(n41.protocol_stack[0], n42.protocol_stack[0])
    pair_cascade_protocols(n41.protocol_stack[1], n42.protocol_stack[1])
    
    # connect the nodes and set parameters for the fibers
    cc0 = ClassicalChannel("cc_n1_n2", tl, distance=1e3)
    cc1 = ClassicalChannel("cc_n2_n1", tl, distance=1e3)
    cc0.set_ends(n1, n2.name)
    cc1.set_ends(n2, n1.name)

    cc2 = ClassicalChannel("cc_n3_n4", tl, distance=1e3)
    cc3 = ClassicalChannel("cc_n4_n3", tl, distance=1e3)
    cc2.set_ends(n3, n4.name)
    cc3.set_ends(n4, n3.name)

    cc4 = ClassicalChannel("cc_n5_n6", tl, distance=1e3)
    cc5 = ClassicalChannel("cc_n6_n5", tl, distance=1e3)
    cc4.set_ends(n5, n6.name)
    cc5.set_ends(n6, n5.name)

    cc6 = ClassicalChannel("cc_n7_n8", tl, distance=1e3)
    cc7 = ClassicalChannel("cc_n8_n7", tl, distance=1e3)
    cc6.set_ends(n7, n8.name)
    cc7.set_ends(n8, n7.name)

    cc8 = ClassicalChannel("cc_n9_n10", tl, distance=1e3)
    cc9 = ClassicalChannel("cc_n10_n9", tl, distance=1e3)
    cc8.set_ends(n9, n10.name)
    cc9.set_ends(n10, n9.name)

    cc10 = ClassicalChannel("cc_n11_n12", tl, distance=1e3)
    cc11 = ClassicalChannel("cc_n12_n11", tl, distance=1e3)
    cc10.set_ends(n11, n12.name)
    cc11.set_ends(n12, n11.name)

    cc12 = ClassicalChannel("cc_n13_n14", tl, distance=1e3)
    cc13 = ClassicalChannel("cc_n14_n13", tl, distance=1e3)
    cc12.set_ends(n13, n14.name)
    cc13.set_ends(n14, n13.name)

    cc14 = ClassicalChannel("cc_n15_n16", tl, distance=1e3)
    cc15 = ClassicalChannel("cc_n16_n15", tl, distance=1e3)
    cc14.set_ends(n15, n16.name)
    cc15.set_ends(n16, n15.name)

    cc16 = ClassicalChannel("cc_n17_n18", tl, distance=1e3)
    cc17 = ClassicalChannel("cc_n18_n17", tl, distance=1e3)
    cc16.set_ends(n17, n18.name)
    cc17.set_ends(n18, n17.name)

    cc18 = ClassicalChannel("cc_n19_n20", tl, distance=1e3)
    cc19 = ClassicalChannel("cc_n20_n19", tl, distance=1e3)
    cc18.set_ends(n19, n20.name)
    cc19.set_ends(n20, n19.name)

    cc20 = ClassicalChannel("cc_n21_n22", tl, distance=1e3)
    cc21 = ClassicalChannel("cc_n22_n21", tl, distance=1e3)
    cc20.set_ends(n21, n22.name)
    cc21.set_ends(n22, n21.name)

    cc22 = ClassicalChannel("cc_n23_n24", tl, distance=1e3)
    cc23 = ClassicalChannel("cc_n24_n23", tl, distance=1e3)
    cc22.set_ends(n23, n24.name)
    cc23.set_ends(n24, n23.name)

    cc24 = ClassicalChannel("cc_n25_n26", tl, distance=1e3)
    cc25 = ClassicalChannel("cc_n26_n25", tl, distance=1e3)
    cc24.set_ends(n25, n26.name)
    cc25.set_ends(n26, n25.name)

    cc26 = ClassicalChannel("cc_n27_n28", tl, distance=1e3)
    cc27 = ClassicalChannel("cc_n28_n27", tl, distance=1e3)
    cc26.set_ends(n27, n28.name)
    cc27.set_ends(n28, n27.name)

    cc28 = ClassicalChannel("cc_n29_n30", tl, distance=1e3)
    cc29 = ClassicalChannel("cc_n30_n29", tl, distance=1e3)
    cc28.set_ends(n29, n30.name)
    cc29.set_ends(n30, n29.name)

    cc30 = ClassicalChannel("cc_n31_n32", tl, distance=1e3)
    cc31 = ClassicalChannel("cc_n32_n31", tl, distance=1e3)
    cc30.set_ends(n31, n32.name)
    cc31.set_ends(n32, n31.name)

    cc32 = ClassicalChannel("cc_n33_n34", tl, distance=1e3)
    cc33 = ClassicalChannel("cc_n34_n33", tl, distance=1e3)
    cc32.set_ends(n33, n34.name)
    cc33.set_ends(n34, n33.name)

    cc34 = ClassicalChannel("cc_n35_n36", tl, distance=1e3)
    cc35 = ClassicalChannel("cc_n36_n35", tl, distance=1e3)
    cc34.set_ends(n35, n36.name)
    cc35.set_ends(n36, n35.name)

    cc36 = ClassicalChannel("cc_n37_n38", tl, distance=1e3)
    cc37 = ClassicalChannel("cc_n38_n37", tl, distance=1e3)
    cc36.set_ends(n37, n38.name)
    cc37.set_ends(n38, n37.name)

    cc38 = ClassicalChannel("cc_n39_n40", tl, distance=1e3)
    cc39 = ClassicalChannel("cc_n40_n39", tl, distance=1e3)
    cc38.set_ends(n39, n40.name)
    cc39.set_ends(n40, n39.name)

    cc40 = ClassicalChannel("cc_n41_n42", tl, distance=1e3)
    cc41 = ClassicalChannel("cc_n42_n41", tl, distance=1e3)
    cc40.set_ends(n41, n42.name)
    cc41.set_ends(n42, n41.name)

    ########

    qc0 = QuantumChannel("qc_n1_n2", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc1 = QuantumChannel("qc_n2_n1", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc0.set_ends(n1, n2.name)
    qc1.set_ends(n2, n1.name)

    qc2 = QuantumChannel("qc_n3_n4", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc3 = QuantumChannel("qc_n4_n3", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc2.set_ends(n3, n4.name)
    qc3.set_ends(n4, n3.name)

    qc4 = QuantumChannel("qc_n5_n6", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc5 = QuantumChannel("qc_n6_n5", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc4.set_ends(n5, n6.name)
    qc5.set_ends(n6, n5.name)

    qc6 = QuantumChannel("qc_n7_n8", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc7 = QuantumChannel("qc_n8_n7", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc6.set_ends(n7, n8.name)
    qc7.set_ends(n8, n7.name)

    qc8 = QuantumChannel("qc_n9_n10", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc9 = QuantumChannel("qc_n10_n9", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc8.set_ends(n9, n10.name)
    qc9.set_ends(n10, n9.name)

    qc10 = QuantumChannel("qc_n11_n12", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc11 = QuantumChannel("qc_n12_n11", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc10.set_ends(n11, n12.name)
    qc11.set_ends(n12, n11.name)

    qc12 = QuantumChannel("qc_n13_n14", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc13 = QuantumChannel("qc_n14_n13", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc12.set_ends(n13, n14.name)
    qc13.set_ends(n14, n13.name)

    qc14 = QuantumChannel("qc_n15_n16", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc15 = QuantumChannel("qc_n16_n15", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc14.set_ends(n15, n16.name)
    qc15.set_ends(n16, n15.name)

    qc16 = QuantumChannel("qc_n17_n18", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc17 = QuantumChannel("qc_n18_n17", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc16.set_ends(n17, n18.name)
    qc17.set_ends(n18, n17.name)

    qc18 = QuantumChannel("qc_n19_n20", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc19 = QuantumChannel("qc_n20_n19", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc18.set_ends(n19, n20.name)
    qc19.set_ends(n20, n19.name)

    qc20 = QuantumChannel("qc_n21_n22", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc21 = QuantumChannel("qc_n22_n21", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc20.set_ends(n21, n22.name)
    qc21.set_ends(n22, n21.name)

    qc22 = QuantumChannel("qc_n23_n24", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc23 = QuantumChannel("qc_n24_n23", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc22.set_ends(n23, n24.name)
    qc23.set_ends(n24, n23.name)

    qc24 = QuantumChannel("qc_n25_n26", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc25 = QuantumChannel("qc_n26_n25", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc24.set_ends(n25, n26.name)
    qc25.set_ends(n26, n25.name)

    qc26 = QuantumChannel("qc_n27_n28", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc27 = QuantumChannel("qc_n28_n27", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc26.set_ends(n27, n28.name)
    qc27.set_ends(n28, n27.name)

    qc28 = QuantumChannel("qc_n29_n30", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc29 = QuantumChannel("qc_n30_n29", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc28.set_ends(n29, n30.name)
    qc29.set_ends(n30, n29.name)

    qc30 = QuantumChannel("qc_n31_n32", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc31 = QuantumChannel("qc_n32_n31", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc30.set_ends(n31, n32.name)
    qc31.set_ends(n32, n31.name)

    qc32 = QuantumChannel("qc_n33_n34", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc33 = QuantumChannel("qc_n34_n33", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc32.set_ends(n33, n34.name)
    qc33.set_ends(n34, n33.name)

    qc34 = QuantumChannel("qc_n35_n36", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc35 = QuantumChannel("qc_n36_n35", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc34.set_ends(n35, n36.name)
    qc35.set_ends(n36, n35.name)

    qc36 = QuantumChannel("qc_n37_n38", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc37 = QuantumChannel("qc_n38_n37", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc36.set_ends(n37, n38.name)
    qc37.set_ends(n38, n37.name)

    qc38 = QuantumChannel("qc_n39_n40", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc39 = QuantumChannel("qc_n40_n39", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc38.set_ends(n39, n40.name)
    qc39.set_ends(n40, n39.name)

    qc40 = QuantumChannel("qc_n41_n42", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc41 = QuantumChannel("qc_n42_n41", tl, attenuation=1e-5, distance=1e3, polarization_fidelity=0.97)
    qc40.set_ends(n41, n42.name)
    qc41.set_ends(n42, n41.name)

    num_keys = math.inf
    
    # instantiate our written keysize protocol
    km1 = KeyManager(tl, keysize, num_keys)
    km1.lower_protocols.append(n1.protocol_stack[1])
    n1.protocol_stack[1].upper_protocols.append(km1)

    km2 = KeyManager(tl, keysize, num_keys)
    km2.lower_protocols.append(n2.protocol_stack[1])
    n2.protocol_stack[1].upper_protocols.append(km2)

    km3 = KeyManager(tl, keysize, num_keys)
    km3.lower_protocols.append(n3.protocol_stack[1])
    n3.protocol_stack[1].upper_protocols.append(km3)

    km4 = KeyManager(tl, keysize, num_keys)
    km4.lower_protocols.append(n4.protocol_stack[1])
    n4.protocol_stack[1].upper_protocols.append(km4)

    km5 = KeyManager(tl, keysize, num_keys)
    km5.lower_protocols.append(n5.protocol_stack[1])
    n5.protocol_stack[1].upper_protocols.append(km5)

    km6 = KeyManager(tl, keysize, num_keys)
    km6.lower_protocols.append(n6.protocol_stack[1])
    n6.protocol_stack[1].upper_protocols.append(km6)

    km7 = KeyManager(tl, keysize, num_keys)
    km7.lower_protocols.append(n7.protocol_stack[1])
    n7.protocol_stack[1].upper_protocols.append(km7)

    km8 = KeyManager(tl, keysize, num_keys)
    km8.lower_protocols.append(n8.protocol_stack[1])
    n8.protocol_stack[1].upper_protocols.append(km8)

    km9 = KeyManager(tl, keysize, num_keys)
    km9.lower_protocols.append(n9.protocol_stack[1])
    n9.protocol_stack[1].upper_protocols.append(km9)

    km10 = KeyManager(tl, keysize, num_keys)
    km10.lower_protocols.append(n10.protocol_stack[1])
    n10.protocol_stack[1].upper_protocols.append(km10)

    km11 = KeyManager(tl, keysize, num_keys)
    km11.lower_protocols.append(n11.protocol_stack[1])
    n11.protocol_stack[1].upper_protocols.append(km11)

    km12 = KeyManager(tl, keysize, num_keys)
    km12.lower_protocols.append(n12.protocol_stack[1])
    n12.protocol_stack[1].upper_protocols.append(km12)

    km13 = KeyManager(tl, keysize, num_keys)
    km13.lower_protocols.append(n13.protocol_stack[1])
    n13.protocol_stack[1].upper_protocols.append(km13)

    km14 = KeyManager(tl, keysize, num_keys)
    km14.lower_protocols.append(n14.protocol_stack[1])
    n14.protocol_stack[1].upper_protocols.append(km14)

    km15 = KeyManager(tl, keysize, num_keys)
    km15.lower_protocols.append(n15.protocol_stack[1])
    n15.protocol_stack[1].upper_protocols.append(km15)

    km16 = KeyManager(tl, keysize, num_keys)
    km16.lower_protocols.append(n16.protocol_stack[1])
    n16.protocol_stack[1].upper_protocols.append(km16)

    km17 = KeyManager(tl, keysize, num_keys)
    km17.lower_protocols.append(n17.protocol_stack[1])
    n17.protocol_stack[1].upper_protocols.append(km17)

    km18 = KeyManager(tl, keysize, num_keys)
    km18.lower_protocols.append(n18.protocol_stack[1])
    n18.protocol_stack[1].upper_protocols.append(km18)

    km19 = KeyManager(tl, keysize, num_keys)
    km19.lower_protocols.append(n19.protocol_stack[1])
    n19.protocol_stack[1].upper_protocols.append(km19)

    km20 = KeyManager(tl, keysize, num_keys)
    km20.lower_protocols.append(n20.protocol_stack[1])
    n20.protocol_stack[1].upper_protocols.append(km20)

    km21 = KeyManager(tl, keysize, num_keys)
    km21.lower_protocols.append(n21.protocol_stack[1])
    n21.protocol_stack[1].upper_protocols.append(km21)

    km22 = KeyManager(tl, keysize, num_keys)
    km22.lower_protocols.append(n22.protocol_stack[1])
    n22.protocol_stack[1].upper_protocols.append(km22)

    km23 = KeyManager(tl, keysize, num_keys)
    km23.lower_protocols.append(n23.protocol_stack[1])
    n23.protocol_stack[1].upper_protocols.append(km23)

    km24 = KeyManager(tl, keysize, num_keys)
    km24.lower_protocols.append(n24.protocol_stack[1])
    n24.protocol_stack[1].upper_protocols.append(km24)

    km25 = KeyManager(tl, keysize, num_keys)
    km25.lower_protocols.append(n25.protocol_stack[1])
    n25.protocol_stack[1].upper_protocols.append(km25)

    km26 = KeyManager(tl, keysize, num_keys)
    km26.lower_protocols.append(n26.protocol_stack[1])
    n26.protocol_stack[1].upper_protocols.append(km26)

    km27 = KeyManager(tl, keysize, num_keys)
    km27.lower_protocols.append(n27.protocol_stack[1])
    n27.protocol_stack[1].upper_protocols.append(km27)

    km28 = KeyManager(tl, keysize, num_keys)
    km28.lower_protocols.append(n28.protocol_stack[1])
    n28.protocol_stack[1].upper_protocols.append(km28)

    km29 = KeyManager(tl, keysize, num_keys)
    km29.lower_protocols.append(n29.protocol_stack[1])
    n29.protocol_stack[1].upper_protocols.append(km29)

    km30 = KeyManager(tl, keysize, num_keys)
    km30.lower_protocols.append(n30.protocol_stack[1])
    n30.protocol_stack[1].upper_protocols.append(km30)

    km31 = KeyManager(tl, keysize, num_keys)
    km31.lower_protocols.append(n31.protocol_stack[1])
    n31.protocol_stack[1].upper_protocols.append(km31)

    km32 = KeyManager(tl, keysize, num_keys)
    km32.lower_protocols.append(n32.protocol_stack[1])
    n32.protocol_stack[1].upper_protocols.append(km32)

    km33 = KeyManager(tl, keysize, num_keys)
    km33.lower_protocols.append(n33.protocol_stack[1])
    n33.protocol_stack[1].upper_protocols.append(km33)

    km34 = KeyManager(tl, keysize, num_keys)
    km34.lower_protocols.append(n34.protocol_stack[1])
    n34.protocol_stack[1].upper_protocols.append(km34)

    km35 = KeyManager(tl, keysize, num_keys)
    km35.lower_protocols.append(n35.protocol_stack[1])
    n35.protocol_stack[1].upper_protocols.append(km35)

    km36 = KeyManager(tl, keysize, num_keys)
    km36.lower_protocols.append(n36.protocol_stack[1])
    n36.protocol_stack[1].upper_protocols.append(km36)

    km37 = KeyManager(tl, keysize, num_keys)
    km37.lower_protocols.append(n37.protocol_stack[1])
    n37.protocol_stack[1].upper_protocols.append(km37)

    km38 = KeyManager(tl, keysize, num_keys)
    km38.lower_protocols.append(n38.protocol_stack[1])
    n38.protocol_stack[1].upper_protocols.append(km38)

    km39 = KeyManager(tl, keysize, num_keys)
    km39.lower_protocols.append(n39.protocol_stack[1])
    n39.protocol_stack[1].upper_protocols.append(km39)

    km40 = KeyManager(tl, keysize, num_keys)
    km40.lower_protocols.append(n40.protocol_stack[1])
    n40.protocol_stack[1].upper_protocols.append(km40)

    km41 = KeyManager(tl, keysize, num_keys)
    km41.lower_protocols.append(n41.protocol_stack[1])
    n41.protocol_stack[1].upper_protocols.append(km41)

    km42 = KeyManager(tl, keysize, num_keys)
    km42.lower_protocols.append(n42.protocol_stack[1])
    n42.protocol_stack[1].upper_protocols.append(km42)

    
    # start simulation and record timing
    km1.send_request()
    km3.send_request()
    km5.send_request()
    km7.send_request()
    km9.send_request()
    km11.send_request()
    km13.send_request()
    km15.send_request()
    km17.send_request()
    km19.send_request()
    km21.send_request()
    km23.send_request()
    km25.send_request()
    km27.send_request()
    km29.send_request()
    km31.send_request()
    km33.send_request()
    km35.send_request()
    km37.send_request()
    km39.send_request()
    km41.send_request()

    tick = time.time()

    t1 = Thread(target=task, args=(
        n1, n2, n3, n4, n5, n6,n7,n8,n9,n10,
        n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,
        n21,n22,n23,n24,n25,n26,n27,n28,n29,n30,
        n31,n32,n33,n34,n35,n36,n37,n38,n39,n40,
        n41,n42)
    )
    t1.start()

    tl.init()
    tl.run()

    print("execution time %.2f sec" % (time.time() - tick))

    process = psutil.Process()
    print(process.memory_info().rss/1000000000)  # in bytes 
    
    error_rates = []
    for i, key in enumerate(km1.keys):
        counter = 0
        diff = key ^ km2.keys[i]
        for j in range(km1.keysize):
            counter += (diff >> j) & 1
        error_rates.append(counter)

    print("key error rates:")
    for i, e in enumerate(error_rates):
        print("\tkey {}:\t{}%".format(i + 1, e * 100))

test(5000, 128)