
class Graph:
    __result = []

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def applyUnion(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                self.__result.append([u, v, w])
                self.applyUnion(parent, rank, x, y)

    def printSolution(self):
        print("Edge \tWeight")
        for u, v, weight in self.__result:
            print("%d - %d\t %d" % (u, v, weight))


if __name__ == "__main__":
    g = Graph(7)

    g.addEdge(0, 1, 6)
    g.addEdge(0, 2, 7)
    g.addEdge(0, 3, 8)

    g.addEdge(1, 0, 6)
    g.addEdge(1, 2, 6)
    g.addEdge(1, 4, 6)

    g.addEdge(2, 0, 7)
    g.addEdge(2, 1, 6)
    g.addEdge(2, 3, 3)
    g.addEdge(2, 4, 3)
    g.addEdge(2, 5, 4)
    g.addEdge(2, 6, 2)

    g.addEdge(3, 0, 8)
    g.addEdge(3, 2, 3)
    g.addEdge(3, 5, 1)

    g.addEdge(4, 1, 6)
    g.addEdge(4, 2, 3)
    g.addEdge(4, 6, 2)

    g.addEdge(5, 2, 4)
    g.addEdge(5, 3, 1)
    g.addEdge(5, 6, 3)

    g.addEdge(6, 2, 2)
    g.addEdge(6, 4, 2)
    g.addEdge(6, 5, 3)

    g.kruskal()
    g.printSolution()
