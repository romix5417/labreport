#! /usr/bin/python
# -*- coding: utf-8 -*-


import math
import numpy as np
import matplotlib.pyplot as plt


def main():
    # 无线优化2000米测试数据
    DataSet0_x = [2.0, 1.0, 0.4, 0.2]
    DataSet0_y = [5.57, 11.01, 27.35, 52.19]

    fig = plt.figure(figsize=(8, 4))

    # fig 1
    ax1 = fig.add_subplot(221)
    ax1.set_ylim(0, 8)
    ax2 = ax1.twinx()
    ax2.set_ylim(-95, -40)

    ax1.plot(DataSet0_2to1_x, DataSet0_2to1_y,
             "o-", color='red', label="bandwidth")
    ax2.plot(DataSet0_2to1_x, DataSet0_2to1_sig,
             "o-", color='green', label="signal")
    ax1.set_ylabel("Mbps/s")
    ax1.set_xlabel("m")
    ax2.set_ylabel("db")
    legend1 = ax1.legend(loc=(.80, .92))
    legend2 = ax2.legend(loc=(.80, .84))

    plt.title("DataSet0_2to1 distance optimize 2000")

    # fig 2
    ax1 = fig.add_subplot(222)
    ax1.set_ylim(0, 8)
    ax2 = ax1.twinx()
    ax2.set_ylim(-95, -40)

    ax1.plot(DataSet0_1to2_x, DataSet0_1to2_y,
             "o-", color='red', label="bandwidth")
    ax2.plot(DataSet0_1to2_x, DataSet0_1to2_sig,
             "o-", color='green', label="signal")
    ax1.set_ylabel("Mbps/s")
    ax1.set_xlabel("m")
    ax2.set_ylabel("db")
    legend1 = ax1.legend(loc=(.80, .92))
    legend2 = ax2.legend(loc=(.80, .84))

    plt.title("DataSet0_1to2 distance optimize 2000")

    # fig 3
    ax1 = fig.add_subplot(223)
    ax1.set_ylim(0, 8)
    ax2 = ax1.twinx()
    ax2.set_ylim(-95, -40)

    ax1.plot(DataSet1_2to1_x, DataSet1_2to1_y,
             "o-", color='red', label="bandwidth")
    ax2.plot(DataSet1_2to1_x, DataSet1_2to1_sig,
             "o-", color='green', label="signal")
    ax1.set_ylabel("Mbps/s")
    ax1.set_xlabel("m")
    ax2.set_ylabel("db")
    legend1 = ax1.legend(loc=(.80, .92))
    legend2 = ax2.legend(loc=(.80, .84))

    plt.title("DataSet0_2to1 distance optimize 10000")

    # fig 4
    ax1 = fig.add_subplot(224)
    ax1.set_ylim(0, 8)
    ax2 = ax1.twinx()
    ax2.set_ylim(-95, -40)

    ax1.plot(DataSet1_1to2_x, DataSet1_1to2_y,
             "o-", color='red', label="bandwidth")
    ax2.plot(DataSet1_1to2_x, DataSet1_1to2_sig,
             "o-", color='green', label="signal")
    ax1.set_ylabel("Mbps/s")
    ax1.set_xlabel("m")
    ax2.set_ylabel("db")
    legend1 = ax1.legend(loc=(.80, .92))
    legend2 = ax2.legend(loc=(.80, .84))

    plt.title("DataSet0_1to2 distance optimize 10000")

    plt.show()


if __name__ == "__main__":
    main()
