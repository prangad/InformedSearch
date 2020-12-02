from cfg import ADJ_MATRIX

class Node:
    def __init__(self, name):
        self.name = name  # Name of the node.
        self.left = None  # Left child.
        self.right = None  # Right child.
        self.parents = []  # Parent nodes used for efficient pathing.


def breadth_first_search(self, start):
    visited = [False] * self.v
    q = [start]

    # Set source as visited
    visited[start] = True

    while q:
        vis = q[0]

        # Print current node
        print(vis, end=' ')
        q.pop(0)

        # For every adjacent vertex to
        # the current vertex
        for i in range(self.v):
            if (Graph.adj[vis][i] == 1 and
                    (not visited[i])):
                # Push the adjacent node
                # in the queue
                q.append(i)

                # set
                visited[i] = True