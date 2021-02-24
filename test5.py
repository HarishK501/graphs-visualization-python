from graphADT import Graph


def testGraph():
    g = Graph()

    g.addEdge(0, 2, 4)
    g.addEdge(0, 1, 4)
    g.addEdge(1, 2, 2)
    g.addEdge(2, 3, 3)
    g.addEdge(2, 5, 2)
    g.addEdge(2, 4, 4)
    g.addEdge(3, 4, 3)
    g.addEdge(4, 5, 3)

    g.visualize()

    print("Kruskal")
    g.mstKruskal()
    print("\nPrim's")
    g.mstPrim()


def main():
    testGraph()


if __name__ == '__main__':
    main()
