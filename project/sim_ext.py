from sequence.kernel.timeline import Timeline
import sequence.utils.log as log

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
import csv
import threading

tick = 0
current_sim = ''

def inspect(tl, rate):
    target = tl.now() + (rate * 1.0e12)
    while True:
        if tl.now() > target:
            row_b = [sim_command, tl.now() * 1.0e-12]
            row_k = [sim_command, tl.now() * 1.0e-12]
            row_d = [sim_command, tl.now() * 1.0e-12]

            for super_node in network.super_qkd_nodes.values():
                for tr in super_node.transceivers.values():
                    row_b.append(len(tr.qkd_node_p.buffer))
            
            for super_node in network.super_qkd_nodes.values():
                for tr in super_node.transceivers.values():
                    row_k.append(len(tr.qkd_node_p.key_manager.keys))
            
            for super_node in network.super_qkd_nodes.values():
                for tr in super_node.transceivers.values():
                    row_d.append(tr.qkd_node_p.del_mess)
            
            with open(current_sim + 'buffers.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(row_b)
            
            with open(current_sim + 'keys.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(row_k)
            
            with open(current_sim + 'delivered_p.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(row_d)

            target = tl.now() + (rate * 1.0e12)

def save_metrics():
    row = [sim_command]

    for super_node in network.super_qkd_nodes.values():
        for tr in super_node.transceivers.values():
            row.append(tr.qkd_node_p.key_manager.count_keys)
    
    with open(current_sim + 'tot_keys.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(row)

def handler(signal_received, frame):
    global tick
    print('\nThe Simulation is terminated manually. Exiting gracefully...')
    print(f'Delivered messages: {MessagingProtocol.delivered_messages}')
    print(f'Dropped messages : {MessagingProtocol.dropped_messages}')
    print(f'Sent messages: {MessagingProtocol.delivered_messages + MessagingProtocol.dropped_messages}')
    print("Execution time %.2f sec" % (time.time() - tick))
    print("Simulation time %.2f sec" % (timeline.now() * 1.0e-12))

    save_metrics()
    print("Bye!")

    exit(0)

def gen_csv_file():
    with open(current_sim + 'packet_result.csv', 'w') as file:
        writer = csv.writer(file)
        header = ['Sim. Command','Source','Destination','Sent','Delivered','Dropped','Num. Hop','Sending Time','Sim. Time','Tot. Time']
        writer.writerow(header)
    
    with open(current_sim + 'buffers.csv', 'w') as file:
        writer = csv.writer(file)
        header = ['Sim. Command','Time']
        for super_node in network.super_qkd_nodes.values():
            for tr in super_node.transceivers.values():
                header.append(tr.qkd_node.name)
        writer.writerow(header)

    with open(current_sim + 'keys.csv', 'w') as file:
        writer = csv.writer(file)
        header = ['Sim. Command','Time']
        for super_node in network.super_qkd_nodes.values():
            for tr in super_node.transceivers.values():
                header.append(tr.qkd_node.name)
        writer.writerow(header)
    
    with open(current_sim + 'tot_keys.csv', 'w') as file:
        writer = csv.writer(file)
        header = ['Sim. Command']
        for super_node in network.super_qkd_nodes.values():
            for tr in super_node.transceivers.values():
                header.append(tr.qkd_node.name)
        writer.writerow(header)
    
    with open(current_sim + 'delivered_p.csv', 'w') as file:
        writer = csv.writer(file)
        header = ['Sim. Command','Time']
        for super_node in network.super_qkd_nodes.values():
            for tr in super_node.transceivers.values():
                header.append(tr.qkd_node.name)
        writer.writerow(header)

def gen_network(filepath, nodes_number):
    G = nx.random_internet_as_graph(nodes_number)
    # G =  nx.path_graph(nodes_number) this is to generate the chain
    json_G = nx.node_link_data(G)
    with open(filepath, 'w') as f:
        json.dump(json_G, f, ensure_ascii=False, indent=4)
    return G

def draw_to_file(graph, filepath):
    pos = nx.kamada_kawai_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_size = 50, margins = 0.01)
    nx.draw_networkx_labels(graph, pos, font_size = 5, font_color = 'w')
    nx.draw_networkx_edges(graph, pos, width = 0.5)
    plt.savefig(filepath, dpi = 500, orientation = 'landscape', bbox_inches = 'tight')

def sim(graph_json_seq, sim_time, key_size, mess_rate, buff_capacity, inspection_rate, traffic):
    global tick
    global network
    global timeline
    timeline = Timeline(sim_time * 1.0e12)

    # log.set_logger(__name__, timeline, "log.txt")
    # log.set_logger_level('INFO')
    # log.track_module('node')

    network = QKDTopoExt(graph_json_seq, timeline)
    gen_csv_file()
    
    network.add_key_managers(key_size, math.inf)
    network.start_pairing()
    tick = time.time()
    network.start_qkd()
    network.start_messaging(timeline, mess_rate, buff_capacity, traffic)

    threading.Thread(target = inspect, args = (timeline, inspection_rate), daemon = True).start()

    timeline.init()
    timeline.run()
    
    print(f'Delivered messages: {MessagingProtocol.delivered_messages}')
    print(f'Dropped messages : {MessagingProtocol.dropped_messages}')
    print(f'Sent messages: {MessagingProtocol.delivered_messages + MessagingProtocol.dropped_messages}')
    print("Execution time %.2f sec" % (time.time() - tick))
    print("Simulation time %.2f sec" % (timeline.now() * 1.0e-12))

    process = psutil.Process()
    print(process.memory_info().rss/1000000000)  # in bytes 

def main():
    global current_sim
    global sim_command
    current_sim = 'project/simulations/sim_' + str(datetime.now().strftime('%Y-%m-%d_%H:%M:%S')) + '/'
    MessagingProtocol.sim_path = current_sim
    graph_json_ntx = 'graph_networkx.json'
    graph_json_seq = 'graph_sequence.json'
    traffic_json = 'traffic.json'
    sim_params_json = 'sim_parmas.json'
    
    parser = argparse.ArgumentParser(description='parser')
    
    parser.add_argument('--sim-time', dest='sim_time', type=float, default=5, help='Simulation time in seconds')
    parser.add_argument('--netx-graph', dest='netx_graph', type=str, help='File json for networkX graph')
    parser.add_argument('--seq-graph', dest='seq_graph', type=str, help='File json for sequence graph')
    parser.add_argument('--key-size', dest='key_size', type=int, default=128, help='Key size in bits')
    parser.add_argument('--mess-rate', dest='mess_rate', type=float, default=0.1, help='Message sending rate (exponential dist.)')
    parser.add_argument('--num-nodes', dest='num_nodes', type=int, default=10, help='Number of nodes in the graph')
    parser.add_argument('--buff-capacity', dest='buff_capacity', type=float, default=10, help='Buffer capacity of the nodes')
    parser.add_argument('--inspection-rate', dest='inspection_rate', type=float, default=0.005, help='Inspection rate')
    parser.add_argument('--traffic', dest='traffic', type=str, default=None, help='File json for traffic')
    
    args = parser.parse_args()

    print(f"[Simulation Command] {' '.join(sys.argv[0:])}")

    sim_command = ' '.join(sys.argv[0:])
    MessagingProtocol.sim_command = sim_command
    
    os.makedirs(os.path.dirname(current_sim), exist_ok=True)

    if args.traffic:
        with open(args.traffic, 'r') as f:
            js_traffic = json.load(f)
        with open(current_sim + traffic_json, 'w') as f:
            json.dump(js_traffic, f, ensure_ascii=False, indent=4)
    
    with open(current_sim + sim_params_json, 'w') as f:
        f.write(json.dumps(vars(args), indent=4))

    # Genera la rete
    if args.netx_graph == None and args.seq_graph == None:
        graph = gen_network(current_sim + graph_json_ntx, args.num_nodes)
        draw_to_file(graph, current_sim + 'network_graph.png')
        netparse(current_sim + graph_json_ntx, current_sim + graph_json_seq)
        sim(current_sim + graph_json_seq, args.sim_time, args.key_size, args.mess_rate, args.buff_capacity, args.inspection_rate, args.traffic)
        
    # Se specificati entrambi i due grafi prendimao quello di sequence  
    elif (args.netx_graph != None and args.seq_graph != None) or (args.netx_graph == None and args.seq_graph != None):
        with open(args.seq_graph, 'r') as f:
            js_graph = json.load(f)
        with open(current_sim + graph_json_seq, 'w') as f:
            json.dump(js_graph, f, ensure_ascii=False, indent=4)
        sim(current_sim + graph_json_seq, args.sim_time, args.key_size, args.mess_rate, args.buff_capacity, args.inspection_rate, args.traffic)
    
    # Se sepcificato solo quello networkX
    elif args.netx_graph != None and args.seq_graph == None:
        with open(args.netx_graph, 'r') as f:
            js_graph = json.load(f)
        graph = nx.readwrite.json_graph.node_link_graph(js_graph)
        draw_to_file(graph, current_sim + 'network_graph.png')
        with open(current_sim + graph_json_ntx, 'w') as f:
            json.dump(js_graph, f, ensure_ascii=False, indent=4)
        netparse(current_sim + graph_json_ntx, current_sim + graph_json_seq)
        sim(current_sim + graph_json_seq, args.sim_time, args.key_size, args.mess_rate, args.buff_capacity, args.inspection_rate, args.traffic)
    
    save_metrics()

    print("Bye!")

    exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler) # ctlr + c
    signal.signal(signal.SIGTSTP, handler) # ctlr + z 
    main()
