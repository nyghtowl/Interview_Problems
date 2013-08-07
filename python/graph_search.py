#!/usr/bin/env python
'''
Graph Search Problem 

Input:
* N cities with a unique integer ID in the [1..N] range 
* Cities connected by X bidirectional roads which have the same length
    * List of ids of first city connected by each road 
    * List of ids of second city connected by each road
* ID home city
* ID destination city

Output: Print minimum number of roads to travel between home and destination

Assumption: destination city is always accessible from home city


The ith road connects the ith city in the firstCityRoad array and the ith city in the secondCityRoad array.

Constraints:
* Number of cities will not exceed 5000
* Number of roads will not exceed 100000
* Print the result in less than 2 seconds

Example:

    7 cities identified by IDs=1,2,3,4,5,6,7
    5 roads connecting the following pairs of cities: (1,3), (2,3), (3,4), (2,4), (5,6)
    from your home city ID=1 you can reach the destination city ID=4 taking either the 1, 3, 4 route or 1, 3, 2, 4 route
    the 1, 3, 4 route requires you to travel two roads (1,3) and (3,4)
    the 1, 3, 2, 4 route requires you to travel three roads (1,3), (3,2) and (2,4)
    the first route is the shortest one requiring you to travel only 2 roads

1 - 3 -- 4
    |   /
    2  

5 -- 6

'''

class Graph(Object):
    def __init__(self, nodes, edges):
        self.node = nodes
        self.edges = edges

    # def is_connected(self, a, b):
    #     return (a,b) in self.edges

    def edges_from(self, a):
        return [e for e in self.edges if n in e]

# g = Graph(...)

# (1,2) - > (2,1)
# (from, to)

# [(1,2),(2,1)]

# Open shortest path (ospf)
# visited { [1,2]: True, [1,4]: True }
# paths = (1,2), (1,4)

def ospf(home, dest, graph):
    visited = {}

    for e in graph.edges:
        visited[e] = False

    paths = graph.edges_from(home)

    for p in paths:
        if visited[path]:

            # new path
            other_city = p[1] 
            visited[path] = True
            paths.extend(graph.edges_from(other_city))
        else:
            # seen this already
            pass

# Track the number of results mapped
if __name__ == '__main__':
# Test search
home = 1
dest = 5
cities = [1,2,3,4,5,6,7]
road_graph = [(1,3),(3,4),(2,3),(2,4),(5,6)]

print ospf(home, dest, graph)