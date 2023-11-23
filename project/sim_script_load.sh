#! /bin/bash

###### 1Mbps

python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_1Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 1
wait

python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_1Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.1
wait

python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_1Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.05
wait

python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_1Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.02
wait

python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_1Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0125
wait

python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_1Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.01
wait

python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_1Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.008064516129
wait

python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_1Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.006
wait

python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_1Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.005
wait

python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_1Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.003
wait

###### 10Mbps

# 100 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_10Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.01
wait

# 200 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_10Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.005
wait

# 300 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_10Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.003
wait

# 500 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_10Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.002
wait

# 800 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_10Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.00125
wait

# 1000 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_10Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.001
wait

# 1240 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_10Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0008064516129
wait

# 1300p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_10Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0007
wait

# 1500 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_10Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0006
wait

# 1700 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_10Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0005
wait

######### 50Mbps

# 500 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_50Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.002
wait

# 1000 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_50Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.001
wait

# 1500 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_50Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0006
wait

# 3500 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_50Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0002857
wait

# 4500 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_50Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.00023
wait

# 5500 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_50Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0001818
wait

# 6200 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_50Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.000161290
wait

# 6300 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_50Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.000158730
wait

# 6500 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_50Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.000153846
wait

# 6700 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_50Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.000149253
wait

####### 100Mbps

# 1000 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_100Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.001
wait

# 4000 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_100Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.00025
wait

# 5000 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_100Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0002
wait

# 8000 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_100Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.000125
wait

# 10000 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_100Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0001
wait

# 11000 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_100Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.00009
wait

# 12400 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_100Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.00008064516
wait

# 1300 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_100Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.00007692307
wait

# 13500 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_100Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.00007407407
wait

# 14000 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_100Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.00007142857
wait

####### 600Mbps

# 5500 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_600Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0001818
wait

# 10000 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_600Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0001
wait

# 30000 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_600Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.000033
wait

# 50000 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_600Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.00002
wait

# 60000 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_600Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.00001666
wait

# 70000 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_600Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0000142857
wait

# 74404 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_600Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.00001344013
wait

# 75000 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_600Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.000013333
wait

# 80000 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_600Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0000125
wait

# 85000 p/s
python3 project/sim_ext.py --seq-graph project/file/chain_2_node_seq_600Mbps.json --traffic project/file/traffic.json --inspection-rate 0.001 --sim-time 1.0 --mess-rate 0.0000117647
wait