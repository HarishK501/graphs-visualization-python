import sys
sys.path.append("../graphs-visualization-python")


from graphADT import Graph

def testGraph():
    g = Graph()
    for i in range(5):
        g.addVertex(i)
    g.addEdge(5, 1, 8)
    g.addEdge(1, 2, 19)
    g.addEdge(5, 0, 10)
    g.addEdge(4, 6, 11)
    g.addEdge(6, 10, 23)
    g.addEdge(10, 9, 33)
    g.addEdge(9, 8, 7)
    g.addEdge(6, 7, 6)
    g.addEdge(8, 7, 1)
    g.addEdge(9, 6, 9)
    g.addEdge(7, 10, 14)
    g.addEdge(0, 4, 15)
    g.addEdge(0, 3, 16)
    g.addEdge(0, 2, 5)
    g.addEdge(0, 1, 2)
    g.addEdge(2, 3, 4)
    g.addEdge(3, 4, 30)
    g.addEdge(4, 5, 18)
    g.addEdge(5, 2, 22)
    g.addEdge(3, 1, 17)
    g.visualize()
    g.mstKruskal()


def main():
    testGraph()


if __name__ == '__main__':
    main()
