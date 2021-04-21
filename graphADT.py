import networkx as nx
import matplotlib
matplotlib.use('Agg')


import matplotlib.pyplot as plt

class Vertex:
    def __init__(self, key):
        self.id = key
        self.visited = False
        self.connectedTo = {}
        self.set = [self.id]   # for kruskal

    def addNeighbor(self, nbr, weight):
        '''
        nbr - neighbour vertex
        '''
        self.connectedTo[nbr] = float(weight)

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Edge:
    def __init__(self, f, t, w):
        self.front = f
        self.tail = t
        self.weight = w

    def __repr__(self):
        return '({},{},w={})'.format(self.front.getId(), self.tail.getId(), self.weight)


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.edgeList = []
        self.G = nx.Graph()  # for visualization
        self.pos = []  # co-ordinate positions array of nodes in graph

    #       self.front=[]
    #       self.back=[]
    #       self.depfs=[]
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost):  # f is from node, t is to node
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.edgeList.append(Edge(self.vertList[f], self.vertList[t], cost))
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.vertList[t].addNeighbor(self.vertList[f], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def visualize(self):
        edges = []
        for edge in self.edgeList:
            edges.append((edge.front.id, edge.tail.id, edge.weight))
        self.G.add_weighted_edges_from(edges)
        self.pos = nx.shell_layout(self.G)
        nx.draw_networkx(self.G, pos=self.pos, node_size=500,
                         node_color='g', font_color='white', edge_color='blue')
        arc_weight = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos=self.pos,font_size=13, edge_labels=arc_weight, bbox=dict(boxstyle="square,pad=0.3",fc="white",alpha=0.4)) #  bbox=dict(boxstyle="square,pad=0.3",alpha=0)
        
        plt.axis('off')
        plt.savefig('sample.png')
        plt.clf()

    def visualizeMST(self, mst_edges, algo):
        edge_col = []
        edge_width = []

        for edge in self.G.edges():
            if not(edge in mst_edges) and not(edge[::-1] in mst_edges):
                edge_col.append('blue')
                edge_width.append(1)
            else:
                edge_col.append('red')
                edge_width.append(3)

        arc_weight = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx(self.G, pos=self.pos, node_color='g', node_size=500, edge_color=edge_col, font_color='white', width=edge_width)
        nx.draw_networkx_edge_labels(self.G, pos=self.pos,font_size=13, edge_labels=arc_weight, bbox=dict(boxstyle="square,pad=0.3",fc="white",alpha=0.4))
        plt.axis('off')

        if algo == 'kruskal':
            plt.title("Kruskal's MST")
        else:
            plt.title("Prim's MST")
        
        plt.savefig(algo + '.png')
        plt.clf()

        return

    def e_sort(self, e):
        return e.weight

    def findset(self, v, disjointSet):
        for i in disjointSet:
            if v in i:
                return i

    def mstKruskal(self):

        edgeListAsc = sorted(self.edgeList, key=self.e_sort)
        MST = []

        disjointSet = []
        for i in self.vertList:
            self.vertList[i].set = [self.vertList[i].id]
            disjointSet.append(self.vertList[i].set)

        # now,disjointSet contains=>[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]

        for e in edgeListAsc:

            s1 = self.findset(e.front.getId(), disjointSet)

            s2 = self.findset(e.tail.getId(), disjointSet)

            if s1 == s2:
                continue
            if s1 != s2:
                MST.append(e)
                if len(s1) > len(s2) or len(s1) == len(s2):
                    disjointSet.remove(s2)
                    self.findset(e.front.getId(), disjointSet).extend(s2)
                else:
                    disjointSet.remove(s1)
                    self.findset(e.tail.getId(), disjointSet).extend(s1)

        mst_edges = []  # for visualization purpose
        res = ""
        for i in MST:
            res += str(i) + " <br>"
            mst_edges.append((i.front.id, i.tail.id))

        # print(mst_edges)
        # print(self.G.edges())
        self.visualizeMST(mst_edges, "kruskal")
        # print(res)

        return 

    def findStartVertex(self, mstSet, dist):
        minVertex = Vertex(float('-inf'))
        dist[minVertex.id] = float('inf')
        for vertex in self.vertList.values():
            if vertex.id not in mstSet:
                if dist[vertex.id] < dist[minVertex.id]:
                    minVertex = vertex

        return minVertex

    def mstPrim(self):
        parent = {}
        mstSet = set()  # set of vertices that are a part of mst
        dist = {}
        
        tmp_i = 0
        for vertex in self.vertList.values():
            if tmp_i == 0:
                dist[vertex.id] = 0
                tmp_i = 1
                continue
            dist[vertex.id] = float("inf")


        while not len(mstSet) == len(self.vertList):
            u = self.findStartVertex(mstSet, dist)
            mstSet.add(u.id)

            for v in u.getConnections():
                if u.connectedTo[v] < dist[v.id] and v.id not in mstSet:
                    dist[v.id] = u.connectedTo[v]
                    parent[v] = u

        mst_edges = []
        for vertex in parent.keys():
            u = parent[vertex]
            v = vertex
            mst_edges.append((u.id, v.id))
            # print("({},{}, w={})".format(u.id, v.id, u.connectedTo[v]))

        self.visualizeMST(mst_edges, "prims")

        return
