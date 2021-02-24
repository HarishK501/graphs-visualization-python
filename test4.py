from graphADT import Graph


def testGraph():
    g = Graph()

    g.addEdge(0, 1, 2)
    g.addEdge(0, 2, 5)
    g.addEdge(1, 2, 2)
    g.addEdge(1, 3, 4)
    g.addEdge(2, 3, 5)
    g.addEdge(3, 4, 2)
    g.addEdge(2, 4, 5)

    g.visualize()

    print("Kruskal")
    g.mstKruskal()
    print("\nPrim's")
    g.mstPrim()


def main():
    testGraph()


if __name__ == '__main__':
    main()
