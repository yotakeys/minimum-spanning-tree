class Graph():

    __max = 9999
    __parent = []

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(self.__parent[i], "-", i, "\t",
                  self.graph[i][self.__parent[i]])

    def minKey(self, key, mstSet):

        min = self.__max

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def prims(self):

        key = [self.__max] * self.V
        self.__parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        self.__parent[0] = -1

        for _ in range(self.V):

            u = self.minKey(key, mstSet)

            mstSet[u] = True

            for v in range(self.V):

                if self.graph[u][v] > 0 and mstSet[v] == False \
                        and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    self.__parent[v] = u


if __name__ == '__main__':
    g = Graph(7)
    g.graph = [[0, 6, 7, 8, 0, 0, 0],
               [6, 0, 6, 0, 6, 0, 0],
               [7, 6, 0, 3, 3, 4, 2],
               [8, 0, 3, 0, 0, 1, 0],
               [0, 6, 3, 0, 0, 0, 2],
               [0, 0, 4, 1, 0, 0, 3],
               [0, 0, 2, 0, 2, 3, 0]
               ]

    g.prims()
    g.printSolution()
