
class Graph:

    __result = []
    __parent = []

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, i):
        if self.__parent[i] == i:
            return i
        return self.find(self.__parent[i])

    def union(self, rank, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if rank[xroot] < rank[yroot]:
            self.__parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            self.__parent[yroot] = xroot
        else:
            self.__parent[yroot] = xroot
            rank[xroot] += 1

    def boruvka(self):
        self.__parent = []
        rank = []

        cheapest = []

        numTrees = self.V

        for node in range(self.V):
            self.__parent.append(node)
            rank.append(0)
            cheapest = [-1] * self.V

        while numTrees > 1:

            for i in range(len(self.graph)):

                u, v, w = self.graph[i]
                set1 = self.find(u)
                set2 = self.find(v)

                if set1 != set2:

                    if cheapest[set1] == -1 or cheapest[set1][2] > w:
                        cheapest[set1] = [u, v, w]

                    if cheapest[set2] == -1 or cheapest[set2][2] > w:
                        cheapest[set2] = [u, v, w]

            for node in range(self.V):

                if cheapest[node] != -1:
                    u, v, w = cheapest[node]
                    set1 = self.find(u)
                    set2 = self.find(v)

                    if set1 != set2:
                        self.union(rank, set1, set2)
                        self.__result.append([u, v, w])
                        numTrees = numTrees - 1

            cheapest = [-1] * self.V

    def printSolution(self):
        print("Edge \tWeight")
        for u, v, weight in self.__result:
            print("%d - %d\t %d" % (u, v, weight))


if __name__ == '__main__':

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

    g.boruvka()
    g.printSolution()
