#!/usr/bin/env python
'''
Graph Search Problem 

Input:
* N cities with a unique integer ID in the [1..N] range 
* Cities connected by M bidirectional roads which have the same length
    * List of ids of first city connected by each road 
    * List of ids of second city connected by each road
* ID home city
* ID destination city

Output: Print minimum number of roads to travel between home and destination

Assumption: destination city always accessible from home city


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

'''