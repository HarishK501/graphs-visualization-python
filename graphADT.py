# from Binaryheap import MinHeap
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

    def createAdjMatrix(self):
        cols = rows = len(self.vertList)
        arr = [[0 for i in range(cols)] for j in range(rows)]
        print("Index order", end="=>")
        for i in self:
            print(i.getId(), end=" ")
        print()
        for i in self:
            for j in i.getConnections():
                arr[i.getId()][j.getId()] = 1
        for i in arr:
            print(i, end="\n")

        return arr

    def e_sort(self, e):
        return e.weight

    def findset(self, v, disjointSet):
        for i in disjointSet:
            if v in i:
                return i

    def mstKruskal(self):
        # list of sorted edges based on edge weight.
        edgeListAsc = sorted(self.edgeList, key=self.e_sort)
        MST = []  # spanning tree with list of edges.
        # a list which contains the individual sets of all vertices.
        disjointSet = []
        for i in self.vertList:
            disjointSet.append(self.vertList[i].set)

        # now,disjointSet contains=>[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]

        for e in edgeListAsc:
            # here,we find the sets where the front and tail vertex...
            s1 = self.findset(e.front.getId(), disjointSet)
            # ...of the current edge are present.
            s2 = self.findset(e.tail.getId(), disjointSet)

            if s1 == s2:  # if s1 and s2 are same, both front and tail vertices are present in the same...
                continue  # ...set and therefore it results in a cycle.
            if s1 != s2:                # if both sets aren't same,we append the current edge to the MST
                MST.append(e)
                # Here , we are combining both the sets...
                if len(s1) > len(s2) or len(s1) == len(s2):
                    # ...and removing the set which is smaller
                    disjointSet.remove(s2)
                    self.findset(e.front.getId(), disjointSet).extend(s2)
                else:
                    disjointSet.remove(s1)
                    self.findset(e.tail.getId(), disjointSet).extend(s1)

        for i in MST:
            print(i)
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
        mstSet = set()
        self.vertList[0].dist = 0

        while not len(mstSet) == len(self.vertList):
            u = self.findStartVertex(mstSet)
            mstSet.add(u.id)

            for v in u.getConnections():
                if u.connectedTo[v] < v.dist and v.id not in mstSet:
                    v.dist = u.connectedTo[v]
                    parent[v] = u

        for vertex in parent.keys():
            u = parent[vertex]
            v = vertex
            print("({},{}, w={})".format(u.id, v.id, u.connectedTo[v]))

        return
