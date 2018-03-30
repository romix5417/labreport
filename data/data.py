import os
import re
import matplotlib.pyplot as plt


def read_data(filename):
    line_count = 0

    node_item = []
    node0_list = []
    node1_list = []
    node2_list = []
    node3_list = []

    fd = open(filename, "r")
    line = fd.readline()
    while line:
        line_count += 1
        if line.find("OLSR Routing table") > 0:
            node_item = []
            node_item.append(line.split(","))
            line = fd.readline()
            line = fd.readline()
            while line:
                if line.find("HNA") > 0:
                    line = fd.readline()
                    break
                else:
                    node_item.append(line)

                line = fd.readline()

            node_item[0].append(len(node_item)-1)
            node_number = int(node_item[0][0][6:])
            if node_number == 0:
                node0_list.append(node_item)
            if node_number == 1:
                node1_list.append(node_item)
            if node_number == 2:
                node2_list.append(node_item)
            if node_number == 3:
                node3_list.append(node_item)

            #print("node item:", node_item)

        line = fd.readline()

        #if line_count > 1500:
        #    break


    return node0_list, node1_list, node2_list, node3_list


def proc_data(data0, data1, data2, data3):
    #print("data0", data)

    fig = plt.figure(figsize=(8, 4))

    #fig 1
    ax1 = fig.add_subplot(411)
    ax1.set_ylim(0, 5)
    ax1.set_xlim(0, 120)

    ax1.plot([round(float(item[0][1][8:-1]), 1) for item in data0], [item[0][4] for item in data0], "-", color='red', label="route")
    ax1.set_ylabel("u")
    ax1.set_xlabel("s")
    #legend1 = ax1.legend(loc=(.80, .92))

    plt.title("Node Route Tabel Statistics")

    #fig 1
    ax2 = fig.add_subplot(412)
    ax2.set_ylim(0, 5)
    ax2.set_xlim(0, 120)

    ax2.plot([round(float(item[0][1][8:-1]), 1) for item in data1], [item[0][4] for item in data1], "-", color='red', label="route")
    ax2.set_ylabel("u")
    ax2.set_xlabel("s")
    #legend2 = ax2.legend(loc=(.80, .92))

    #fig 2
    ax3 = fig.add_subplot(413)
    ax3.set_ylim(0, 5)
    ax3.set_xlim(0, 120)

    ax3.plot([round(float(item[0][1][8:-1]), 1) for item in data2], [item[0][4] for item in data2], "-", color='red', label="route")
    ax3.set_ylabel("u")
    ax3.set_xlabel("s")
    #legend3 = ax3.legend(loc=(.80, .92))

    #fig 2
    ax4 = fig.add_subplot(414)
    ax4.set_ylim(0, 5)
    ax4.set_xlim(0, 120)

    ax4.plot([round(float(item[0][1][8:-1]), 1) for item in data3], [item[0][4] for item in data3], "-", color='red', label="route")
    ax4.set_ylabel("u")
    ax4.set_xlabel("s")
    #legend4 = ax4.legend(loc=(.80, .92))

    plt.show()

def main():
    filename = "olsr_0.2shello_0.4stc.routes"
    data0, data1, data2, data3 = read_data(filename)

    proc_data(data0, data1, data2, data3)


if __name__ == '__main__':
    main()
