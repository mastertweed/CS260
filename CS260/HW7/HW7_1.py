import math


class Graph():
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = [[0 for column in range(nodes)] for row in range(nodes)]

        self.nodeDist = []

    def minDistance(self, dist, sptSet):

        min = math.inf

        for v in range(self.nodes):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):

        dist = [math.inf] * self.nodes
        dist[src] = 0
        sptSet = [False] * self.nodes

        for c in range(self.nodes):

            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.nodes):
                if self.graph[u][v] > 0 and sptSet[v] is False and dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]

        self.nodeDist = dist


def floyd(graph, nodes):
    v = nodes
    g = graph

    # Set all unknown to inf
    for i in range(v):
        for l in range(v):
            if graph[i][l] == 0:
                graph[i][l] = math.inf
            else:
                graph[i][l] = float(graph[i][l])

    # Reset zero paths
    for i in range(v):
        graph[i][i] = float(0)

    for k in range(v):
        for i in range(v):
            for j in range(v):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = float(graph[i][k] + graph[k][j])

    return graph


def printList(d):
    d = ['%.1f' % elem for elem in d]
    print('[', end='')
    for i in range(len(d) - 1):
        print(d[i], end=', ')

    print(d[-1], end=']\n')


# Input file
file = input("File containing graph:\n")
f = open(file, "r")

# Read text file and format data
adjList = f.read()

# Pull number of nodes
numNodes = int(adjList[0])

adjList = adjList.split()
adjList.pop(0)


adjMat = []
count = 0
for i in range(int(len(adjList) / 3)):
    adjMat.append([int(adjList[count]), int(adjList[count + 1]), int(adjList[count + 2])])
    count = count + 3

adjList = adjMat

mat = [[0 for k in range(numNodes)] for i in range(numNodes)]
for i in range(numNodes):
    mat[i][i] = 0

for i in range(len(adjList)):
    mat[adjList[i][0]][adjList[i][1]] = adjList[i][2]

# Begin operations
print("Possible Commands are: ")
print("dijkstra x - Runs Dijkstra starting at node X. X must be an integer")
print("floyd - Runs Floyd's algorithm")
print("help - prints this menu")
print("exit or ctrl-D - Exits the program")

# Ask for input
end = 0
while end == 0:

    # Input command loop
    while True:
        command = input("Enter command:\n")

        # Determine starting node
        if "dijkstra" in command:
            temp = command.split(" ")

            command = temp[0]
            srcNode = int(temp[1])
            break

        # Floyd
        if command == "floyd":
            break

        # Repeat commands
        if command == "help":
            print("Possible Commands are: ")
            print("dijkstra x - Runs Dijkstra starting at node X. X must be an integer")
            print("floyd - Runs Floyd's algorithm")
            print("help - prints this menu")
            print("exit or ctrl-D - Exits the program")

        # Exit and end loop
        if command == "exit":
            end = 1
            print("Bye")
            break

    # Skip if exit was chosen
    if command != "exit":

        if command == "floyd":
            d = floyd(mat,numNodes)

            for i in range(len(d)):
                print(d[i])

        if command == "dijkstra":

            # Create graph with number of nodes, put in edge values, solve
            g = Graph(numNodes)
            g.graph = mat
            g.dijkstra(srcNode)

            d = g.nodeDist
            printList(d)


