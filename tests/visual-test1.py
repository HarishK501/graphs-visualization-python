import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.distance_measures import center


# Defining a Class
class GraphVisualization:

    def __init__(self):

        # visual is a list which stores all
        # the set of edges that constitutes a
        # graph
        self.visual = []

    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)

        pos = nx.shell_layout(G)
        # pos = nx.nx_agraph.graphviz_layout(G, prog="sfdp")
        nx.draw_networkx(G, pos=pos, node_color='g')
        plt.axis('off')
        plt.savefig('sample.png')
        print(pos)


# Driver code
G = GraphVisualization()
# G.addEdge(0, 2)
# G.addEdge(1, 2)
# G.addEdge(1, 3)
# G.addEdge(5, 3)
# G.addEdge(3, 4)
# G.addEdge(1, 0)
# G.addEdge(10, 0)

G.addEdge(5, 1)
G.addEdge(1, 2)
G.addEdge(5, 0)
G.addEdge(4, 6)
G.addEdge(6, 10)
G.addEdge(10, 9)
G.addEdge(9, 8)
G.addEdge(6, 7)
G.addEdge(8, 7)
G.addEdge(9, 6)
G.addEdge(7, 10)
G.addEdge(0, 4)
G.addEdge(0, 3)
G.addEdge(0, 2)
G.addEdge(0, 1)
G.addEdge(2, 3)
G.addEdge(3, 4)
G.addEdge(4, 5)
G.addEdge(5, 2)
G.addEdge(3, 1)
G.visualize()
