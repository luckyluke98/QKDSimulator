from sequence.kernel.timeline import Timeline

from topology import QKDTopoExt
from messaging import MessagingProtocol
from transceiver import Transceiver
import networkx as nx
import json
import matplotlib.pyplot as plt
from parser import netparse

import json
import math
import signal
from sys import exit
import sys
import time
from datetime import datetime
import argparse
import os
import pandas as pd
import numpy
import psutil

tick = 0

def save_metrics():
    res = pd.DataFrame(data=MessagingProtocol.d)
    res.to_csv(current_sim + 'packet_result.csv')

    graph_data = []

    for super_node in network.super_qkd_nodes.values():
        dropped = sent = 0
        
        for tr_node in super_node.transceivers.values():
            dropped += tr_node.qkd_node_p.drop_mess
            sent += tr_node.qkd_node_p.sent_mess
        graph_data.append([dropped, sent])
    
    df = pd.DataFrame(numpy.array(graph_data), columns=["Dropped", "Sent"])
    df.plot.bar()
    plt.savefig(current_sim + 'node_result.pdf', dpi=300)

def handler(signal_received, frame):
    global tick
    print('\nThe Simulation is terminated manually. Exiting gracefully...')
    print(f'Delivered messages: {MessagingProtocol.delivered_messages}')
    print(f'Dropped messages : {MessagingProtocol.dropped_messages}')
    print(f'Sent messages: {MessagingProtocol.sent_messages}')
    print("Execution time %.2f sec" % (time.time() - tick))
    print("Simulation time %.2f sec" % (timeline.now() * 1.0e-12))

    save_metrics()

    exit(0)

def gen_network(filepath, nodes_number):
    G = nx.random_internet_as_graph(nodes_number)
    # G =  nx.path_graph(nodes_number) this is to generate the chain
    json_G = nx.node_link_data(G)
    with open(filepath, 'w') as f:
        json.dump(json_G, f, ensure_ascii=False)
    return G

def draw_to_file(graph, filepath):
    pos = nx.kamada_kawai_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_size=50, margins=0.01)
    nx.draw_networkx_labels(graph, pos, font_size=5, font_color='w')
    nx.draw_networkx_edges(graph, pos, width=0.5)
    plt.savefig(filepath, dpi=500, orientation='landscape', bbox_inches='tight')

def sim(graph_json_seq, sim_time, key_size, mess_rate):
    global tick
    global network
    global timeline
    timeline = Timeline(sim_time * 1000000000000)
    network = QKDTopoExt(graph_json_seq, timeline)
    
    network.add_key_managers(key_size, math.inf)
    network.start_pairing()
    tick = time.time()
    network.start_qkd()
    network.start_messaging(timeline, mess_rate)

    timeline.init()
    timeline.run()
    
    print(f'Delivered messages: {MessagingProtocol.delivered_messages}')
    print(f'Dropped messages : {MessagingProtocol.dropped_messages}')
    print(f'Sent messages: {MessagingProtocol.sent_messages}')
    print("Execution time %.2f sec" % (time.time() - tick))
    print("Simulation time %.2f sec" % (timeline.now() * 1.0e-12))

    process = psutil.Process()
    print(process.memory_info().rss/1000000000)  # in bytes 

def main():
    global current_sim
    current_sim = 'project/simulations/sim_' + str(datetime.now().strftime('%Y-%m-%d_%H:%M:%S')) + '/'
    graph_json_ntx = 'graph_networkx.json'
    graph_json_seq = 'graph_sequence.json'
    
    parser = argparse.ArgumentParser(description='parser')
    
    parser.add_argument('--sim-time', dest='sim_time', type=float, default=5, help='Simulation time in seconds')
    parser.add_argument('--netx-graph', dest='netx_graph', type=str, help='File json for networkX graph')
    parser.add_argument('--seq-graph', dest='seq_graph', type=str, help='File json for sequence graph')
    parser.add_argument('--key-size', dest='key_size', type=int, default=128, help='Key size in bits')
    parser.add_argument('--mess-rate', dest='mess_rate', type=float, default=0.1, help='Message sending rate (exponential dist.)')
    parser.add_argument('--num-nodes', dest='num_nodes', type=int, default=10, help='Number of nodes in the graph')
    
    args = parser.parse_args()
    
    print(f"[Simulation Command] {' '.join(sys.argv[0:])}")
    
    os.makedirs(os.path.dirname(current_sim), exist_ok=True)
    
    # Genera la rete
    if args.netx_graph == None and args.seq_graph == None:
        graph = gen_network(current_sim + graph_json_ntx, args.num_nodes)
        draw_to_file(graph, current_sim + 'network_graph.png')
        netparse(current_sim + graph_json_ntx, current_sim + graph_json_seq)
        sim(current_sim + graph_json_seq, args.sim_time, args.key_size, args.mess_rate)
        
    # Se specificati entrambi i due grafi prendimao quello di sequence  
    elif (args.netx_graph != None and args.seq_graph != None) or (args.netx_graph == None and args.seq_graph != None):
        with open(args.seq_graph, 'r') as f:
            js_graph = json.load(f)
        with open(current_sim + graph_json_seq, 'w') as f:
            json.dump(js_graph, f, ensure_ascii=False)
        sim(current_sim + graph_json_seq, args.sim_time, args.key_size, args.mess_rate)
    
    # Se sepcificato solo quello networkX
    elif args.netx_graph != None and args.seq_graph == None:
        with open(args.netx_graph, 'r') as f:
            js_graph = json.load(f)
        graph = nx.readwrite.json_graph.node_link_graph(js_graph)
        draw_to_file(graph, current_sim + 'network_graph.png')
        with open(current_sim + graph_json_ntx, 'w') as f:
            json.dump(js_graph, f, ensure_ascii=False)
        netparse(current_sim + graph_json_ntx, current_sim + graph_json_seq)
        sim(current_sim + graph_json_seq, args.sim_time, args.key_size, args.mess_rate)
    
    save_metrics()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler) # ctlr + c
    signal.signal(signal.SIGTSTP, handler) # ctlr + z 
    main()
