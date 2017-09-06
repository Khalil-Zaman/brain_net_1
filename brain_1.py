"""Khalil Zaman - Attempt to make a neural network"""
import random
import numpy
import csv

class create_net:

    nodes = []          # Weight on the nodes
    nodes_link = []     # Weight on the links of the nodes
    NOL = 4             # Number of layers
    NPL = 8             # Nodes per layer

    def __init__(self, number_of_layers, nodes_per_layer=8, path="brain_1.csv"):
        self.nodes = [0] * nodes_per_layer*number_of_layers
        self.nodes_link = [0] * (nodes_per_layer**2)*(number_of_layers-1)
        self.NOL = number_of_layers
        self.NPL = nodes_per_layer
        self.links()
        self.csv_writer(path)

    def links(self):
        for i in range(0, len(self.nodes)):
            self.nodes[i] = random.randint(-10, 10)
        for i in range(0, len(self.nodes_link)):
            self.nodes_link[i] = random.randint(-10, 10)

    def csv_writer(self, path):
        with open(path, "w", newline='') as file:
            file.write(str(self.NOL) + "\n")
            file.write(str(self.NPL) + "\n")
            for line in self.nodes_link:
                file.write(str(line))
                file.write(",")

class read_net:

    NOL = 0
    NPL = 0
    nodes_links = []

    def __init__(self, path):
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            x = 0
            for row in reader:
                x += 1
                if x == 1:
                    self.NOL = int(row[0])
                if x == 2:
                    self.NPL = int(row[0])
                if x == 3:
                    self.nodes_links = row


def to_binary(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]


def to_string(b=None):
    b = ''.join(str(x) for x in b)
    return chr(int(b, 2))
    return ''.join([chr(int(x, 2)) for x in b])


def sigmoid(x):
    return (1 / (1 + numpy.exp(-x)))


def sigmoid_derivative(x):
    return x * (1 - x)


def forward_propogation(txt, net):
    binary = to_binary(txt)
    print(binary)
    for char in binary:
        propagation = list(char)
        x = 0
        h = 0
        for i in range(0, (net.NPL**2)*(net.NOL-1)):
            propagation[x] = int(propagation[x]) + int(net.nodes_links[i])
            x += 1
            h += 1
            if x == net.NPL:
                x = 0
            if h == net.NPL**2:
                for d in range(0, len(propagation)):
                    if (sigmoid(propagation[d]) > 0.5):
                        propagation[d] = 1
                    else:
                        propagation[d] = 0
                #print(propagation)
                h = 0
        print(to_string(propagation), end="")


def train(txt, net):
    forward_propogation(txt, net)



#create_net(4, 8, path="brain_1.csv")
#create_net(4, path="brain_2.csv")
Brain_1 = read_net("brain_1.csv")
train ("abcd", Brain_1)