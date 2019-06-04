
def kruskal(mat):

    outputList = []

    # [vertex1, vertex2, distance]
    edgeList = []
    for i in range(len(mat)):
        edgeList.append(mat[i])

    vertexSets = []
    for i in range(len(edgeList)):
        vertexSets.append([i])

        if edgeList[i][1] < edgeList[i][0]:
            temp = [edgeList[i][1], edgeList[i][0], edgeList[i][2]]
            edgeList[i] = temp

    while len(edgeList) != 0:

        # Find minimum distance edge
        min = 100000
        for i in range(len(edgeList)):
            if edgeList[i][2] < min:
                min = edgeList[i][2]
                minindex = i

        # Find which sets contain vertex's
        vertex1Set = 0
        vertex2Set = 0
        for i in range(len(vertexSets)):
            if edgeList[minindex][0] in vertexSets[i]:
                vertex1Set = i
            if edgeList[minindex][1] in vertexSets[i]:
                vertex2Set = i

        # If not same set combine sets, add to outputList and remove from edgeList
        if vertex1Set != vertex2Set:
            print("Select Edge: {}".format(edgeList[minindex]))

            outputList.append(edgeList[minindex])

            for i in vertexSets[vertex2Set]:
                vertexSets[vertex1Set].append(i)

            vertexSets.pop(vertex2Set)

        edgeList.pop(minindex)


def prims(startList,startNode):

    print('Starting Node: {}'.format(startNode))

    # [vertex1, vertex2, distance]
    edgeList = []
    for i in range(len(startList)):
        edgeList.append(startList[i])

    for i in range(len(edgeList)):
        if edgeList[i][1] < edgeList[i][0]:
            temp = [edgeList[i][1], edgeList[i][0], edgeList[i][2]]
            edgeList[i] = temp

    vertexList = [startNode]

    possibleVertex = []

    while len(edgeList) != 0 or len(possibleVertex) != 0:

        # Find new possible paths
        popList = []
        for i in range(len(edgeList)):
            if vertexList[-1] == edgeList[i][0] or vertexList[-1] == edgeList[i][1]:
                possibleVertex.append(edgeList[i])
                popList.append(edgeList[i])

        for i in popList:
            edgeList.remove(i)

        # Find minimum distance edge from possible paths
        min = 100000
        for i in range(len(possibleVertex)):
            if possibleVertex[i][2] < min:
                min = possibleVertex[i][2]
                minindex = i

        # If possible add to list
        if possibleVertex[minindex][1] in vertexList and possibleVertex[minindex][0] not in vertexList:
            print('Added {}'.format(possibleVertex[minindex][0]))
            print("Using Edge {}".format(possibleVertex[minindex]))
            vertexList.append(possibleVertex[minindex][0])
            possibleVertex.pop(minindex)

        elif possibleVertex[minindex][0] in vertexList and possibleVertex[minindex][1] not in vertexList:
            print('Added {}'.format(possibleVertex[minindex][1]))
            print("Using Edge {}".format(possibleVertex[minindex]))
            vertexList.append(possibleVertex[minindex][1])
            possibleVertex.pop(minindex)

        else:
            possibleVertex.pop(minindex)


# Input file
print('Welcome to Minimum Spanning Tree Finder')
file = input("Give the file name graph is in:\n")
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
    adjMat.append([int(adjList[count]), int(adjList[count + 1]), float(adjList[count + 2])])
    count = count + 3

outList = []
for i in range(len(adjMat)):
    outList.append(adjMat[i])

# Begin operations
print('Commands: ')
print('exit or ctrl-d - quits the program')
print('help - prints this menu')
print("prim integer_value - run's Prim's algorithm starting at node given")
print("kruskal - runs Kruskal's algorithm")

# Ask for input
end = 0
while end == 0:

    # Input command loop
    while True:
        command = input("Enter command:\n")

        # Determine starting node
        if "prim" in command:
            print("Running Prim's Algorithm")
            temp = command.split(" ")

            command = temp[0]
            srcNode = int(temp[1])
            break

        # Floyd
        elif command == "kruskal":
            print("Running Kruskal's Algorithm")
            break

        # Repeat commands
        elif command == "help":
            print('Commands: ')
            print('exit or ctrl-d - quits the program')
            print('help - prints this menu')
            print("prim integer_value - run's Prim's algorithm starting at node given")
            print("kruskal - runs Kruskal's algorithm")

        # Exit and end loop
        elif command == "exit":
            end = 1
            print("Bye")
            break

        else:
            print("Unknown Command")

    # Skip if exit was chosen
    if command != "exit":

        if command == "kruskal":
            kruskal(outList)

        if command == "prim":
            prims(outList,srcNode)

