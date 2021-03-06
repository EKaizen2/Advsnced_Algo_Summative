#PLEASE NOTE, I PUT THE WRONG PICTURE FOR QUESTION ALGORITHM OUTPUT ON THE PDF DOC
#THERE WAS NO SECOND ATTEMPT TO RESUBMIT SO I COULD NOT CHANGE IT, BUT THIS CODE WORKS WELL AND SHOWS THE RIGHT OUTPUT

# THANK YOU

from collections import deque
 
# A class to represent a graph object
class Graph:
 
    # Constructor
    def __init__(self, edges, x, n):
        self.adjList = [[] for _ in range(3*n)]
 
        # add edges to the directed graph
        for (v, u, weight) in edges:
 
            # Create two new vertices, `v+n` and `v+2×n`, if the edge's weight is `3x`.
            # Also, split edge (v, u) into (v, v+n), (v+n, v+2N) and (v+2N, u),
            # each having weight `x`.
            if weight == 3*x:
                self.adjList[v].append(v + n)
                self.adjList[v + n].append(v + 2*n)
                self.adjList[v + 2*n].append(u)
 
            # create one new vertex `v+n` if the weight of the edge is `2x`.
            # Also, split edge (v, u) into (v, v+n), (v+n, u) each having weight `x`
            elif weight == 2*x:
                self.adjList[v].append(v + n)
                self.adjList[v + n].append(u)
 
            # no splitting is needed if the edge weight is `1x`
            else:
                self.adjList[v].append(u)
 
 
# Recursive function to print the path of a given vertex `v` from the source vertex
def printPath(predecessor, v, cost, n):
 
    if v >= 0:
        cost = printPath(predecessor, predecessor[v], cost, n)
        cost = cost + 1
 
        # only consider the original nodes present in the graph
        if v < n:
            print(v, end=' ')
 
    return cost
 
 
# Perform BFS on the graph starting from vertex source
def findLeastPathCost(graph, source, dest, n):
 
    # stores vertex is discovered in BFS traversal or not
    discovered = [False] * 3 * n
 
    # mark the source vertex as discovered
    discovered[source] = True
 
    # `predecessor` stores predecessor information. It is used to trace
    # the least-cost path from the destination back to the source.
    predecessor = [-1] * 3 * n
 
    # create a queue for doing BFS and enqueue source vertex
    q = deque()
    q.append(source)
 
    # loop till queue is empty
    while q:
 
        # dequeue front node and print it
        curr = q.popleft()
 
        # if destination vertex is reached
        if curr == dest:
            print(f'The least-cost path between {source} and {dest} is ', end='')
            print('having cost', printPath(predecessor, dest, -1, n))
 
        # do for every adjacent edge of the current vertex
        for v in graph.adjList[curr]:
            if not discovered[v]:
                # mark it as discovered and enqueue it
                discovered[v] = True
                q.append(v)
 
                # set `curr` as the predecessor of vertex `v`
                predecessor[v] = curr
 
 
if __name__ == '__main__':
 
    x = 1
 
    # List of graph edges as per the diagram
    edges = [
        (1,2,5), (2,3,6), (3,4,2), (1,3,15), (4,5,-1),
    ]
 
    # total number of nodes in the graph
    n = 5
 
    # given the source and destination vertex
    source = 1
    dest = 2
    dest1 = 3
    dest2 = 4
    dest3 = 5
 
    # build a graph from the given edges
    graph = Graph(edges, x, n)
 
    # Perform BFS traversal from the given source
    findLeastPathCost(graph, source, dest, n)
    findLeastPathCost(graph, source, dest1, n)
    findLeastPathCost(graph, source, dest2, n)
    findLeastPathCost(graph, source, dest3, n)
    
    
    # REFERENCE: https://www.techiedelight.com/least-cost-path-weighted-digraph-using-bfs/
