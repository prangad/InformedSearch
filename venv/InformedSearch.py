# Grand Valley State University
# Written by: Dylan Pranga
# Contributors: Aaron Kopplin, John Sjitsma
# Date: 09/27/2020
# Description: A* search algorithm to be used in heroclix map. Batteries not included.

from cfg import ADJ_MATRIX
import math

# Helper function for determining the h value between two nodes.
def h(x1, y1, x2, y2):
    return math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))

# A* Search Algorithm
def AStarSearch(startIndex, goalIndex):
    #Initialize open set with start index, and empty closed set.
    openSet = [startIndex]
    closedSet = []
    #This dictionary keeps track of the final path.
    path = {}

    #Continue while the open set is not empty.
    while len(openSet) > 0:
        # Start with the start node, and move on from there.
        currentNodeIndex = 0

        #Check every node in the open set.
        for nodeIndex in openSet:
            #Find the node in the open set with the lowest F value. (Lowest distance from goal.)
            if h(nodeIndex/16, nodeIndex%16, goalIndex/16, goalIndex%16) <\
                    h(currentNodeIndex/16, currentNodeIndex%16, goalIndex/16, goalIndex%16):
                currentNodeIndex = nodeIndex

        #Remove the current node from the open list, then append it to the closed list.
        print("Traversing to Node: {0}".format(currentNodeIndex))
        openSet.remove(currentNodeIndex)
        closedSet.append(currentNodeIndex)

        # Goal node found. Print final path.
        if (currentNodeIndex == goalIndex):
            print("!!! GOAL NODE FOUND !!!")

            # Traverse the dictionary to obtain optimal path.
            total_path = [currentNodeIndex]
            while currentNodeIndex in path.keys():
                currentNodeIndex = path[currentNodeIndex]
                total_path = [currentNodeIndex] + total_path

            #Being lazy, not formatting the best. Just printing the path as a list.
            print("Optimal path to goal node:")
            print(total_path)
            return

        #Grab all adjacent nodes. (Children)
        #i is adjBoolIndex.
        currentChildren = []
        for i in range(len(ADJ_MATRIX[currentNodeIndex])):
            #If the adjacency matrix has a 0 for the index, append it to children. (neighbors/adjacents)
            if (ADJ_MATRIX[currentNodeIndex][i]):
                currentChildren.append(i)

        for child in currentChildren:
            #If the child is in the closed set, continue.
            if child in closedSet:
                continue

            #If the child in the openSet has a greater g value (distance to start) continue.
            if child in openSet:
                if (h(child/16, child%16, startIndex/16, startIndex%16) >=\
                        h(openSet[openSet.index(child)]/16, openSet[openSet.index(child)]%16, startIndex/16, startIndex%16)):
                    continue

            #Otherwise append or override.
            path[child] = currentNodeIndex;
            openSet.append(child)

#Core code.
AStarSearch(0, (len(ADJ_MATRIX)-1))
AStarSearch(128, 143)
AStarSearch(34, 153)