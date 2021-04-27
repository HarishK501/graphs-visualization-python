import sys
sys.path.append("../graphs-visualization-python")

from graphADT import Graph


def testGraph():
    g = Graph()

    g.addEdge(0, 1, 15)
    g.addEdge(1, 7, 5)
    g.addEdge(0, 2, 25)
    g.addEdge(2, 3, 10)
    g.addEdge(1, 4, 10)
    g.addEdge(1, 8, 25)
    g.addEdge(7, 8, 15)
    g.addEdge(4, 6, 5)
    g.addEdge(4, 5, 10)
    g.addEdge(2, 4, 20)
    g.visualize()

    print("Kruskal")
    g.mstKruskal()
    print("\nPrim's")
    g.mstPrim()


def main():
    testGraph()


if __name__ == '__main__':
    main()
