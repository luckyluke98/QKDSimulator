#! /bin/bash

#1Mbps
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_1Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0001 --service-rate 0.0001
wait

#10Mbps
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_10Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0001 --service-rate 0.0001
wait

#50Mbps
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_50Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0001 --service-rate 0.0001
wait

#100Mbps
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_100Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0001 --service-rate 0.0001
wait

#600Mbps
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_600Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0001 --service-rate 0.0001
wait


