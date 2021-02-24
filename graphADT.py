import networkx as nx
import matplotlib.pyplot as plt


class Vertex:
    def __init__(self, key):
        self.id = key
        self.visited = False
        self.connectedTo = {}
        self.set = [self.id]   # for kruskal
        self.dist = float("inf")

    def addNeighbor(self, nbr, weight):
        '''
        nbr - neighbour vertex
        '''
        self.connectedTo[nbr] = weight

    def __cmp__(self, v):
        return self.dist < v.dist

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
        self.pos = nx.spring_layout(self.G)
        nx.draw_networkx(self.G, pos=self.pos,
                         node_color='g', font_color='white', edge_color='blue')
        arc_weight = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(
            self.G, pos=self.pos, edge_labels=arc_weight, alpha=0.5)
        plt.savefig('sample.png')

    def visualizeMST(self, mst_edges, algo):
        edge_col = [
            'blue' if not(edge in mst_edges) and not(edge[::-1] in mst_edges) else 'red' for edge in self.G.edges()]

        arc_weight = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx(self.G, pos=self.pos, node_color='g',
                         edge_color=edge_col, font_color='white')
        nx.draw_networkx_edge_labels(
            self.G, pos=self.pos, edge_labels=arc_weight, alpha=0.9)
        plt.savefig(algo + '.png')
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
            disjointSet.append(self.vertList[i].set)

        # now,disjointSet contains=>[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]

        for e in edgeListAsc:

            s1 = self.findset(e.front.getId(), disjointSet)

            s2 = self.findset(e.tail.getId(), disjointSet)

            if s1 == s2:
                continue
            if s1 != s2:
                MST.append(e)
                # Here , we are combining both the sets...
                if len(s1) > len(s2) or len(s1) == len(s2):
                    # ...and removing the set which is smaller
                    disjointSet.remove(s2)
                    self.findset(e.front.getId(), disjointSet).extend(s2)
                else:
                    disjointSet.remove(s1)
                    self.findset(e.tail.getId(), disjointSet).extend(s1)

        mst_edges = []  # for visualization purpose
        for i in MST:
            print(i)
            mst_edges.append((i.front.id, i.tail.id))

        # print(mst_edges)
        # print(self.G.edges())
        self.visualizeMST(mst_edges, "kruskal")

        return

    def findStartVertex(self, mstSet):
        minVertex = Vertex(float('-inf'))
        minVertex.dist = float('inf')
        for vertex in self.vertList.values():
            if vertex.id not in mstSet:
                if vertex.dist < minVertex.dist:
                    minVertex = vertex

        return minVertex

    def mstPrim(self):
        parent = {}
        mstSet = set()  # set of vertices that are a part of mst
        self.vertList[0].dist = 0

        while not len(mstSet) == len(self.vertList):
            u = self.findStartVertex(mstSet)
            mstSet.add(u.id)

            for v in u.getConnections():
                if u.connectedTo[v] < v.dist and v.id not in mstSet:
                    v.dist = u.connectedTo[v]
                    parent[v] = u

        mst_edges = []
        for vertex in parent.keys():
            u = parent[vertex]
            v = vertex
            mst_edges.append((u.id, v.id))
            print("({},{}, w={})".format(u.id, v.id, u.connectedTo[v]))

        self.visualizeMST(mst_edges, "prims")

        return
