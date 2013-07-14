#!/usr/bin/env python
'''
Travel Itinerary

Input: city_pairs of of paired travel cityations (from to)
Output: Print out the cities in order based on travel plan


'SFO' - 'LAX'
'LAX' - 'BOS'
'JFK' - 'SFO'
'BOS' - 'DEN'
'''

def sort_cities(city_pairs):
    visit_count = {}
    for index, city in enumerate(city_pairs):
        if visit_count[city[0]]:
            visit_count[city[0]] += 1
        else:
            visit_count[city[0]] = 1
        if visit_count[city[1]]:
            visit_count[city[1]] += 1
        else:
            visit_count[city[1]] = 1
    return print_cities(visit_count, city_pairs)

def print_cities(visit_count, city_pairs):
    for city, visit in visit_count:
        if visit == [0]:
            print city
            orig = city
            for index, city in enumerate(city_pairs):
                if orig == city[0]:
                    print city[1]
                    orig = city[1]
                    city_pairs.pop(index)

# Test section

# City pairs format is (from, to)
city_pairs = [('SFO','LAX'),('BOS','DEN'),('LAX','BOS'),('JFK','SFO')]
result = [('JFK','SFO'),('SFO','LAX'),('LAX','BOS'),('BOS','DEN')]

implementations = [sort_cities]

for impl in implementations:
    print 'for %s in implementations' % impl
    print 'f(%s) == %s: %s' % (city_pairs, result, impl(city_pairs) == result)