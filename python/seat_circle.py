'''
Seat Circle

Input: 100 chairs in a circle and they are labeled from 1 to 100

Condition: 
Pattern of change is that seat 1 is asked to leave, seat 2 is asked to stay, seat 3 is asked to leave...
Pattern continues of skipping one and asking one to leave till only one is left

Output: Return who the last person left
'''

# Pseudo coded answer in class
def last_person(seats):
    pop_odd = True
    while len(seats) > 1:
        for i, seat in enumerate(seats):
            if pop_odd and i % 2 == 1:
                del seats[i]
            elif not pop_odd and i % 2 == 0:
                del seats[i]

# Melanie
def last_person2(seats):
    # Skip marker for first num in list if last num in is deleted from previous loop
    skip = False 
    while len(seats) > 1:
        for index, seat in enumerate(seats):
            if skip:
                skip = False
            else:
                x = seats.pop(index)
            if index == len(seats):
                skip = True
    return seats

# Erica
def last_person3(seats):
    odd_toggle = 0
    while len(seats) > 1:
        if len(seats) % 2 == 0 and odd_toggle == 0:
            del seats[odd_toggle::2]
        elif len(seats) % 2 == 0 and odd_toggle == 1:
            del seats[odd_toggle::2]
        elif len(seats) % 2 == 1 and odd_toggle == 0:
            del seats[odd_toggle::2]
            odd_toggle = 1
        else:
            del seats[odd_toggle::2]
            odd_toggle == 0
    return seats

# Jesse - List comprehension
def last_person4(seats):
    while len(seats) > 1:
        pop_odd = (len(seats) % 2 == 0)

        if pop_odd:
            seats = [seat for i, seat in enumerate(seats) if i % 2 == 0]
        else:
            seats = [seat for i, seat in enumerate(seats) if i % 2 == 1]

    return seats

#Test section
if __name__ == '__main__':

    implementations = [last_person2, last_person3, last_person4]



    for impl in implementations:
        seats = [i for i in range(1,101)]
        print '%s returns %s' % (impl.__name__, impl(seats))

