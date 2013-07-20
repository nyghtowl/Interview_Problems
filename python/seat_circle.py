'''
Seat Circle

Input: 100 chairs in a circle and they are labeled from 1 to 100

Condition: 
Pattern of change is that seat 1 is asked to leave, seat 2 is asked to stay, seat 3 is asked to leave...
Pattern continues of skipping one and asking one to leave till one left

Output: Return who the last person left
'''

def last_person(seats):
    pop_odd = True
    while len(seats) > 1:
        for i, seat in enumerate(seats):
            if pop_odd and i % 2 == 1:
                del seats[i]
            elif not pop_odd and i % 2 == 0:
                del seats[i]


#Test section

seats = [1...100]