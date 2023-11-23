import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy
import csv
import json
import seaborn as sb
import math
import glob 


def tot_keys_per_bit_rate():
    pass


def tot_del_packs_time(df, bit_rate, rate_list):

    df = df[df['Sim. Command'].str.contains(bit_rate)]

    df_del_load_1 = df[df['Sim. Command'].str.contains('--mess-rate '+rate_list[0]+'$')].fillna(0)
    df_del_load_2 = df[df['Sim. Command'].str.contains('--mess-rate '+rate_list[1]+'$')].fillna(0)
    df_del_load_3 = df[df['Sim. Command'].str.contains('--mess-rate '+rate_list[2]+'$')].fillna(0)
    df_del_load_4 = df[df['Sim. Command'].str.contains('--mess-rate '+rate_list[3]+'$')].fillna(0)
    df_del_load_5 = df[df['Sim. Command'].str.contains('--mess-rate '+rate_list[4]+'$')].fillna(0)
    df_del_load_6 = df[df['Sim. Command'].str.contains('--mess-rate '+rate_list[5]+'$')].fillna(0)
    df_del_load_7 = df[df['Sim. Command'].str.contains('--mess-rate '+rate_list[6]+'$')].fillna(0)
    df_del_load_8 = df[df['Sim. Command'].str.contains('--mess-rate '+rate_list[7]+'$')].fillna(0)
    df_del_load_9 = df[df['Sim. Command'].str.contains('--mess-rate '+rate_list[8]+'$')].fillna(0)
    df_del_load_10 = df[df['Sim. Command'].str.contains('--mess-rate '+rate_list[9]+'$')].fillna(0)

    return [(df_del_load_1.Time.tolist(), df_del_load_1.tr_node1_to_node0.tolist()),
            (df_del_load_2.Time.tolist(), df_del_load_2.tr_node1_to_node0.tolist()),
            (df_del_load_3.Time.tolist(), df_del_load_3.tr_node1_to_node0.tolist()),
            (df_del_load_4.Time.tolist(), df_del_load_4.tr_node1_to_node0.tolist()),
            (df_del_load_5.Time.tolist(), df_del_load_5.tr_node1_to_node0.tolist()),
            (df_del_load_6.Time.tolist(), df_del_load_6.tr_node1_to_node0.tolist()),
            (df_del_load_7.Time.tolist(), df_del_load_7.tr_node1_to_node0.tolist()),
            (df_del_load_8.Time.tolist(), df_del_load_8.tr_node1_to_node0.tolist()),
            (df_del_load_9.Time.tolist(), df_del_load_9.tr_node1_to_node0.tolist()),
            (df_del_load_10.Time.tolist(), df_del_load_10.tr_node1_to_node0.tolist())]


def tot_del_packs(df, bit_rate, rate_list):

    df = df[df['Sim. Command'].str.contains(bit_rate)]

    df_del_load_1 = df[(df['Sim. Command'].str.contains('--mess-rate '+rate_list[0]+'$')) & (df['Delivered'] == True)]
    df_del_load_2 = df[(df['Sim. Command'].str.contains('--mess-rate '+rate_list[1]+'$')) & (df['Delivered'] == True)]
    df_del_load_3 = df[(df['Sim. Command'].str.contains('--mess-rate '+rate_list[2]+'$')) & (df['Delivered'] == True)]
    df_del_load_4 = df[(df['Sim. Command'].str.contains('--mess-rate '+rate_list[3]+'$')) & (df['Delivered'] == True)]
    df_del_load_5 = df[(df['Sim. Command'].str.contains('--mess-rate '+rate_list[4]+'$')) & (df['Delivered'] == True)]
    df_del_load_6 = df[(df['Sim. Command'].str.contains('--mess-rate '+rate_list[5]+'$')) & (df['Delivered'] == True)]
    df_del_load_7 = df[(df['Sim. Command'].str.contains('--mess-rate '+rate_list[6]+'$')) & (df['Delivered'] == True)]
    df_del_load_8 = df[(df['Sim. Command'].str.contains('--mess-rate '+rate_list[7]+'$')) & (df['Delivered'] == True)]
    df_del_load_9 = df[(df['Sim. Command'].str.contains('--mess-rate '+rate_list[8]+'$')) & (df['Delivered'] == True)]
    df_del_load_10 = df[(df['Sim. Command'].str.contains('--mess-rate '+rate_list[9]+'$')) & (df['Delivered'] == True)]

    return [len(df_del_load_1),len(df_del_load_2),len(df_del_load_3),len(df_del_load_4), \
            len(df_del_load_5),len(df_del_load_6),len(df_del_load_7),len(df_del_load_8),\
            len(df_del_load_9),len(df_del_load_10)]


if __name__ == '__main__':

    dataset = [
        'sim_2023-11-22_11:31:37', 
        'sim_2023-11-22_11:32:26',
        'sim_2023-11-22_11:33:15',
        'sim_2023-11-22_11:34:05',
        'sim_2023-11-22_11:34:55',
        'sim_2023-11-22_11:35:46',
        'sim_2023-11-22_11:36:38',
        'sim_2023-11-22_11:37:29',
        'sim_2023-11-22_11:38:20',
        'sim_2023-11-22_11:39:13',

        'sim_2023-11-21_18:01:30',
        'sim_2023-11-21_18:12:23',
        'sim_2023-11-21_18:23:18',
        'sim_2023-11-21_18:34:11',
        'sim_2023-11-21_18:45:03',
        'sim_2023-11-21_18:55:54',
        'sim_2023-11-21_19:06:43',
        'sim_2023-11-21_19:17:43',
        'sim_2023-11-21_19:28:59',
        'sim_2023-11-21_19:40:11',

        'sim_2023-11-21_19:51:44',
        'sim_2023-11-21_21:20:56',
        'sim_2023-11-21_22:49:56',
        'sim_2023-11-22_00:19:30',
        'sim_2023-11-22_01:38:14',
        'sim_2023-11-22_02:55:53',
        'sim_2023-11-22_04:13:25',
        'sim_2023-11-22_05:31:05',
        'sim_2023-11-22_06:49:04',
        'sim_2023-11-22_08:07:17',

        'sim_2023-11-22_09:25:17',
        'sim_2023-11-22_13:24:17',
        'sim_2023-11-22_13:24:25',
        'sim_2023-11-22_18:11:47',
        'sim_2023-11-22_18:20:53',
        'sim_2023-11-22_23:35:50',
        'sim_2023-11-22_23:51:14',
        'sim_2023-11-23_04:07:22',
        'sim_2023-11-23_04:22:42',
        'sim_2023-11-23_08:07:36'
    ]

    sim_dir = os.path.dirname('project/simulations/') + '/'
    joined_files = []

    # packet_result
    for d in dataset:
        joined_files.append(sim_dir + d + '/packet_result.csv')
    df = pd.concat(map(pd.read_csv, joined_files), ignore_index=True) 

    # delivered_p
    for d in dataset:
        joined_files.append(sim_dir + d + '/delivered_p.csv')
    df_p = pd.concat(map(pd.read_csv, joined_files), ignore_index=True) 

    ##############################

    #1Mbps
    rate_list_1Mbps = ['1', '0.1','0.05','0.02','0.0125','0.01','0.008064516129','0.006','0.005','0.003']

    res_1Mbps = tot_del_packs(df, '1Mbps', rate_list_1Mbps)
    res_1Mbps_p = tot_del_packs_time(df_p, '1Mbps', rate_list_1Mbps)

    #10Mbps
    rate_list_10Mbps = ['0.01','0.005','0.003','0.002','0.00125','0.001','0.0008064516129','0.0007','0.0006','0.0005']

    res_10Mbps = tot_del_packs(df, '10Mbps', rate_list_10Mbps)
    res_10Mbps_p = tot_del_packs_time(df_p, '10Mbps', rate_list_10Mbps)

    #50Mbps

    rate_list_50Mbps = ['0.002','0.001','0.0006','0.0002857','0.00023','0.0001818','0.000161290','0.000158730','0.000153846','0.000149253']

    res_50Mbps = tot_del_packs(df, '50Mbps', rate_list_50Mbps)
    res_50Mbps_p = tot_del_packs_time(df_p, '50Mbps', rate_list_50Mbps)

    #100Mbps

    rate_list_100Mbps = ['0.001','0.00025','0.0002','0.000125','0.0001','0.00009','0.00008064516','0.00007692307','0.00007407407','0.00007142857']

    res_100Mbps = tot_del_packs(df, '100Mbps', rate_list_100Mbps)
    res_100Mbps_p = tot_del_packs_time(df_p, '100Mbps', rate_list_100Mbps)

    ###############################

    fig = plt.figure(200)
    fig.subplots_adjust(hspace=0.4, wspace=0.1)
    fig.set_figwidth(12)
    fig.set_figheight(8)

    plt.subplot(4, 1, 1)
    plt.plot(rate_list_1Mbps, res_1Mbps, marker='o')
    plt.grid()
    plt.ylabel("Delivered packets")
    plt.title('1Mbps (p. = 8064 bit)')

    plt.subplot(4, 1, 2)
    plt.plot(rate_list_10Mbps, res_10Mbps, marker='o')
    plt.grid()
    plt.ylabel("Delivered packets")
    plt.title('10Mbps (p. = 8064 bit)')

    plt.subplot(4, 1, 3)
    plt.plot(rate_list_50Mbps, res_50Mbps, marker='o')
    plt.grid()
    plt.ylabel("Delivered packets")
    plt.title('50Mbps (p. = 8064 bit)')

    plt.subplot(4, 1, 4)
    plt.plot(rate_list_100Mbps, res_100Mbps, marker='o')
    plt.grid()
    plt.xlabel("Mean Packet / sec")
    plt.title('100Mbps (p. = 8064 bit)')

    fig = plt.figure(300)
    fig.subplots_adjust(hspace=0.3, wspace=0.1)
    fig.set_figwidth(12)
    fig.set_figheight(30)

    plt.subplot(4, 1, 1)
    plt.plot(res_1Mbps_p[0][0], res_1Mbps_p[0][1], label = "Load " + rate_list_1Mbps[0])
    plt.plot(res_1Mbps_p[1][0], res_1Mbps_p[1][1], label = "Load " + rate_list_1Mbps[1])
    plt.plot(res_1Mbps_p[2][0], res_1Mbps_p[2][1], label = "Load " + rate_list_1Mbps[2])
    plt.plot(res_1Mbps_p[3][0], res_1Mbps_p[3][1], label = "Load " + rate_list_1Mbps[3])
    plt.plot(res_1Mbps_p[4][0], res_1Mbps_p[4][1], label = "Load " + rate_list_1Mbps[4])
    plt.plot(res_1Mbps_p[5][0], res_1Mbps_p[5][1], label = "Load " + rate_list_1Mbps[5])
    plt.plot(res_1Mbps_p[6][0], res_1Mbps_p[6][1], label = "Load " + rate_list_1Mbps[6])
    plt.plot(res_1Mbps_p[7][0], res_1Mbps_p[7][1], label = "Load " + rate_list_1Mbps[7])
    plt.plot(res_1Mbps_p[8][0], res_1Mbps_p[8][1], label = "Load " + rate_list_1Mbps[8])
    plt.plot(res_1Mbps_p[9][0], res_1Mbps_p[9][1], label = "Load " + rate_list_1Mbps[9])
    plt.ylabel("Packets")
    plt.grid()
    plt.legend(loc='upper left', fontsize="8")
    plt.title("Total Delivered Packets 1Mbps (p. = 8064 bit)")

    plt.subplot(4, 1, 2)
    plt.plot(res_10Mbps_p[0][0], res_10Mbps_p[0][1], label = "Load " + rate_list_10Mbps[0])
    plt.plot(res_10Mbps_p[1][0], res_10Mbps_p[1][1], label = "Load " + rate_list_10Mbps[1])
    plt.plot(res_10Mbps_p[2][0], res_10Mbps_p[2][1], label = "Load " + rate_list_10Mbps[2])
    plt.plot(res_10Mbps_p[3][0], res_10Mbps_p[3][1], label = "Load " + rate_list_10Mbps[3])
    plt.plot(res_10Mbps_p[4][0], res_10Mbps_p[4][1], label = "Load " + rate_list_10Mbps[4])
    plt.plot(res_10Mbps_p[5][0], res_10Mbps_p[5][1], label = "Load " + rate_list_10Mbps[5])
    plt.plot(res_10Mbps_p[6][0], res_10Mbps_p[6][1], label = "Load " + rate_list_10Mbps[6])
    plt.plot(res_10Mbps_p[7][0], res_10Mbps_p[7][1], label = "Load " + rate_list_10Mbps[7])
    plt.plot(res_10Mbps_p[8][0], res_10Mbps_p[8][1], label = "Load " + rate_list_10Mbps[8])
    plt.plot(res_10Mbps_p[9][0], res_10Mbps_p[9][1], label = "Load " + rate_list_10Mbps[9])
    plt.ylabel("Packets")
    plt.grid()
    plt.legend(loc='upper left', fontsize="8")
    plt.title("Total Delivered Packets 10Mbps (p. = 8064 bit)")

    plt.subplot(4, 1, 3)
    plt.plot(res_50Mbps_p[0][0], res_50Mbps_p[0][1], label = "Load " + rate_list_50Mbps[0])
    plt.plot(res_50Mbps_p[1][0], res_50Mbps_p[1][1], label = "Load " + rate_list_50Mbps[1])
    plt.plot(res_50Mbps_p[2][0], res_50Mbps_p[2][1], label = "Load " + rate_list_50Mbps[2])
    plt.plot(res_50Mbps_p[3][0], res_50Mbps_p[3][1], label = "Load " + rate_list_50Mbps[3])
    plt.plot(res_50Mbps_p[4][0], res_50Mbps_p[4][1], label = "Load " + rate_list_50Mbps[4])
    plt.plot(res_50Mbps_p[5][0], res_50Mbps_p[5][1], label = "Load " + rate_list_50Mbps[5])
    plt.plot(res_50Mbps_p[6][0], res_50Mbps_p[6][1], label = "Load " + rate_list_50Mbps[6])
    plt.plot(res_50Mbps_p[7][0], res_50Mbps_p[7][1], label = "Load " + rate_list_50Mbps[7])
    plt.plot(res_50Mbps_p[8][0], res_50Mbps_p[8][1], label = "Load " + rate_list_50Mbps[8])
    plt.plot(res_50Mbps_p[9][0], res_50Mbps_p[9][1], label = "Load " + rate_list_50Mbps[9])
    plt.ylabel("Packets")
    plt.grid()
    plt.legend(loc='upper left', fontsize="8")
    plt.title("Total Delivered Packets 50Mbps (p. = 8064 bit)")

    plt.subplot(4, 1, 4)
    plt.plot(res_100Mbps_p[0][0], res_100Mbps_p[0][1], label = "Load " + rate_list_100Mbps[0])
    plt.plot(res_100Mbps_p[1][0], res_100Mbps_p[1][1], label = "Load " + rate_list_100Mbps[1])
    plt.plot(res_100Mbps_p[2][0], res_100Mbps_p[2][1], label = "Load " + rate_list_100Mbps[2])
    plt.plot(res_100Mbps_p[3][0], res_100Mbps_p[3][1], label = "Load " + rate_list_100Mbps[3])
    plt.plot(res_100Mbps_p[4][0], res_100Mbps_p[4][1], label = "Load " + rate_list_100Mbps[4])
    plt.plot(res_100Mbps_p[5][0], res_100Mbps_p[5][1], label = "Load " + rate_list_100Mbps[5])
    plt.plot(res_100Mbps_p[6][0], res_100Mbps_p[6][1], label = "Load " + rate_list_100Mbps[6])
    plt.plot(res_100Mbps_p[7][0], res_100Mbps_p[7][1], label = "Load " + rate_list_100Mbps[7])
    plt.plot(res_100Mbps_p[8][0], res_100Mbps_p[8][1], label = "Load " + rate_list_100Mbps[8])
    plt.plot(res_100Mbps_p[9][0], res_100Mbps_p[9][1], label = "Load " + rate_list_100Mbps[9])
    plt.xlabel("Time (sec)")
    plt.ylabel("Packets")
    plt.grid()
    plt.legend(loc='upper left', fontsize="8")
    plt.title("Total Delivered Packets 100Mbps (p. = 8064 bit)")


    plt.show()



