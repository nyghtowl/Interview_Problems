# List comprehension
def last_person4(seats):
    while len(seats) > 1:
        print "seats> (0!r)".format(seats)
        pop_odd = (len(seats) % 2 == 0)

        if pop_odd:
            seats = [seat for i, seat in enumerate(seats) if i % 2 == 0]
        else:
            seats = [seat for i, seat in enumerate(seats) if i % 2 == 1]
        raw_input('press_enter')

    return seats

print last_person4(seats = [i for i in range(1, 101)])