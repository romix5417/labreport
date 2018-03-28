import os



def read_data(filename):
    spcase_count = 0
    line_count = 0

    global_list = []
    node_block = []

    print(filename)
    fd = open(filename, "r")
    line = fd.readline()
    while line:

        line_count += 1
        if line == '\n':
            if spcase_count != 1:
                spcase_count += 1
            else:
                node_block = []
                global_list.append(node_block)
                spcase_count = 0
            continue

        node_block.append(line)
        line = fd.readline()

    print(line_count)

def proc_data(data):
    pass


def plot_data(data_array):
    pass


def main():
    filename = "routes.txt"
    read_data(filename)


if __name__ == '__main__':
    main()
