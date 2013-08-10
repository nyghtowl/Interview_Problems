'''
Seat Circle

Input: 100 chairs in a circle and they are labeled from 1 to 100

Condition: 
Pattern of change is that seat 1 is asked to leave, seat 2 is asked to stay, seat 3 is asked to leave...
Pattern continues of skipping one and asking one to leave till only one is left

Output: Return who the last person left
'''

def last_person(seats)
	skip = false
	begin
        seats.each_with_index do |seat, index|
            if skip
                skip = false
            else
                seats.delete(seat)
            end
            if index == seats.length
                skip = true
            end
        end
    end while seats.length > 1 
    seats
end

if __FILE__ == $0
    # Test section
    # implementations = [last_person]
    seats = []

   # implementations.each do |impl|
    	for i in 1..100
    		seats[i-1] = i
    	end

    	puts '%s returns %s' % ['last_person', last_person(seats)]
    # end
end