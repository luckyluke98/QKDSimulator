from sequence.topology.topology import Topology
from sequence.kernel.timeline import Timeline
from sequence.topology.node import QKDNode
from sequence.components.optical_channel import QuantumChannel, ClassicalChannel
from sequence.topology.qkd_topo import QKDTopo
from sequence.qkd.BB84 import pair_bb84_protocols
from sequence.qkd.cascade import pair_cascade_protocols

from networkx import DiGraph, exception, shortest_path

from super_qkd_node import SuperQKDNode
from transceiver import Transceiver
from messaging import MessagingProtocol
from key_manager import KeyManager
from custom_channel import CustomChannel

import re
import json
import random

class QKDTopoExt(Topology):
    
    QKD_NODE = "QKDNode"
    P_FIDELITY = "polarization_fidelity"
    B_RATE = "bit_rate"
    
    def __init__(self, conf_file_name: str, tl):
        self.super_qkd_nodes = {}
        self.timeline = tl
        super().__init__(conf_file_name)

    def _load(self, filename):
        topo_config = json.load(open(filename))
        
        self.generate_super_nodes(topo_config)
        self.generate_transceivers(topo_config)
        self.add_channels(topo_config)
        self.generate_routing_tables()
        
    def generate_super_nodes(self, topo_config):
        for node in topo_config[Topology.ALL_NODE]:
            node_name = node[Topology.NAME]
            
            super_node = SuperQKDNode(node_name)
            self.super_qkd_nodes[node_name] = super_node
            
    def generate_transceivers(self, topo_config):
        for super_node_name in self.super_qkd_nodes.keys():
            for qc in topo_config.get(self.ALL_Q_CHANNEL):
                src_node_name, dst_node_name = qc[self.SRC], qc[self.DST]
                
                if super_node_name == src_node_name:
                    
                    src_tr_name = "tr_" + src_node_name + "_to_" + dst_node_name
                    dst_tr_name = "tr_" + dst_node_name + "_to_" + src_node_name
                    src_node = QKDNode(src_tr_name, self.timeline)
                    
                    tr_node_p = MessagingProtocol(src_node, "msgp", "msgp", dst_tr_name, self.super_qkd_nodes[super_node_name])
                    tr_node = Transceiver(src_node, tr_node_p)
                    
                    self.super_qkd_nodes[src_node_name].transceivers[src_tr_name] = tr_node
    
    def add_channels(self, topo_config):
        for super_node in self.super_qkd_nodes.values():
            for tr in super_node.transceivers.values():
                src_tr_name = tr.qkd_node.name
                
                src_node_name = super_node.name
                dst_node_name = re.findall('tr_(.*)_to_(.*)', src_tr_name)[0][1]
                dst_tr_name = "tr_"+ dst_node_name + "_to_" + super_node.name
                
                # classical channel
                for cc in topo_config.get(self.ALL_C_CHANNEL):
                    if cc[self.SRC] == src_node_name and cc[self.DST] == dst_node_name:
                        cc_name = cc[self.NAME]
                        cc_distance = cc[self.DISTANCE]
                        
                        cchannel = ClassicalChannel(cc_name, self.timeline, cc_distance)
                        cchannel.set_ends(tr.qkd_node, dst_tr_name)
                
                # quantum channel (custom channel)
                for qc in topo_config.get(self.ALL_Q_CHANNEL):
                    if qc[self.SRC] == src_node_name and qc[self.DST] == dst_node_name:
                        qc_name = qc[self.NAME]
                        qc_distance = qc[self.DISTANCE]
                        qc_attenuation = qc[self.ATTENUATION]
                        qc_polarization_fidelity = qc[self.P_FIDELITY]
                        
                        qchannel = CustomChannel(qc_name, self.timeline, 0, qc_distance, 0.9)
                        #qchannel = QuantumChannel(qc_name, self.timeline, qc_attenuation, qc_distance, 0.90)
                        qchannel.set_ends(tr.qkd_node, dst_tr_name)
                        
    def generate_routing_tables(self):
        graph = DiGraph()
        edges = []
        for super_node in self.super_qkd_nodes.values():
            graph.add_node(super_node.name)
            for tr in super_node.transceivers.values():
                
                src_node = re.findall('tr_(.*)_to_(.*)', tr.qkd_node.name)[0][0]
                dst_node = re.findall('tr_(.*)_to_(.*)', tr.qkd_node.name)[0][1]
                
                edges.append((src_node, dst_node, {"weight": 1})) # grafo usato per routing, mettere
                                                                  # peso legato al canale classico? Da chiedere.
        
        graph.add_edges_from(edges)
        
        for src in graph.nodes:
            for dst in graph.nodes:
                if src == dst:
                    continue
                try:
                    path = shortest_path(graph, source=src, target=dst, weight="weight")
                    self.super_qkd_nodes[src].routing_table[dst] = path

                except exception.NetworkXNoPath:
                    pass
                
    def add_key_managers(self, key_size, num_keys):
        for super_node in self.super_qkd_nodes.values():
            for tr in super_node.transceivers.values():
                
                km = KeyManager(tr.qkd_node, self.timeline, key_size, num_keys)
                km.lower_protocols.append(tr.qkd_node.protocol_stack[1])
                tr.qkd_node.protocol_stack[1].upper_protocols.append(km)
                
                tr.add_key_manager(km)
    
    def start_pairing(self):
        for super_node in self.super_qkd_nodes.values():
            for tr in super_node.transceivers.values():
                
                if tr.qkd_node.protocol_stack[0].role == -1 or tr.qkd_node.protocol_stack[1].role == -1:
                    
                    sender_tr_name = tr.qkd_node.name
                    sender_node_name = super_node.name
                    
                    recv_node_name = re.findall('tr_(.*)_to_(.*)', tr.qkd_node.name)[0][1]
                    recv_tr_name = "tr_" + recv_node_name + "_to_" + sender_node_name

                    recv_node = self.super_qkd_nodes[recv_node_name].transceivers[recv_tr_name].qkd_node
                    
                    pair_bb84_protocols(tr.qkd_node.protocol_stack[0], recv_node.protocol_stack[0])
                    pair_cascade_protocols(tr.qkd_node.protocol_stack[1], recv_node.protocol_stack[1])
                    
                    print("[PAIR] " + tr.qkd_node.name + " " + recv_node.name)
    
    def start_qkd(self):
        for super_node in self.super_qkd_nodes.values():
            for tr in super_node.transceivers.values():
                if tr.qkd_node.protocol_stack[0].role == 0 and tr.qkd_node.protocol_stack[1].role == 0:
                    print("[QKD] Start QKD " + tr.qkd_node.name)
                    tr.start_qkd()
    
    def start_messaging(self, tl, rate):
        node_num = len(self.super_qkd_nodes)
        dest = {}
        for super_node in self.super_qkd_nodes.keys():
            dst_node_name = f"node{random.randrange(0, node_num)}"
            while super_node == dst_node_name:
                dst_node_name = f"node{random.randrange(0, node_num)}"
            
            dest[super_node] = dst_node_name
        
        for super_node in self.super_qkd_nodes.values():
            for tr in super_node.transceivers.values():
                tr.qkd_node_p.rate = rate
        
        print("[Messaging] Start Messaging")
        for super_node in self.super_qkd_nodes.values():
            # create packet
            text = "ciao" 
            text = bytes(text, 'utf-8') # b'ciao'
            text = list(text)
            message = {
                "src": super_node.name,
                "dest": dest[super_node.name], 
                "payload": text, 
                "hop": 0,
                "time": None}
            message = json.dumps(message)
            super_node.send_message(tl, dest[super_node.name], message, False)
        
                    
                    
                    
                    
                    
                    