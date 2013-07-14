#!/usr/bin/env python
'''
Fizz Buzz 

Input: list of numbers

Output: print numbers submitted except:
  if divisable by 3 - write fizz
  if divisable by 5 - write buzz
  if divisable by 15 - write fizz buzz

'''

#O(n)
def fizz_buzz(num):
    for n in range(1,(num+1)):
        if n % 15 == 0:
            print "fizz buzz"
        elif n % 5 == 0:
            print "buzz"
        elif n % 3 == 0:
            print "fizz"
        else:
            print n

'''
Alternative version
- if divisible by 5 or contains 5 as a digit in the number => "fizz"
 - if divisible by 7 or contains 7 as a digit in the number => "buzz" 
 - if divisible by 5 and 7, or contains 5 and 7, or divisible by 5 and contains 7, 
 or divisible by 7 and contains 5 => "fizz buzz" 

'''

#O(n)
def fizz_buzz2(num):
    low_val = []

    for n in range(1, (num+1)):
        div_5 = has_5 = div_7 = has_7 = False

        #Find where number meets conditions
        if n%5 == 0: 
            div_5 = True 
        if str(n).find('5') != -1:
            has_5 = True
        if n%7 == 0:
            div_7 = True
        if str(n).find('7') != -1:
            has_7 = True

        #Run comparison to find fizz buzz conditions and print
        if (div_5 and div_7) or (has_5 and has_7) or (div_5 and has_7) or (has_5 and div_7):
            print 'fizz buzz'
        elif (div_5 or has_5):
            print 'fizz'
        elif (div_7 or has_7):
            print 'buzz'
        else:
            print n



'''
print lowest value of numbers that meets all 16 combinations of T/F 
to conditions

/5 or *5 25 and 53 
/7 or *7
*5 & *7 75
/5 & *7 75
/7 & *5 
/5 & /7 35


divis_5 = True # or False
divis_7 = True
has_5 = True
has_7 = True
'''

#O(n)
def fizz_buzz_combos(start, end):
    ans = {}
    while len(ans) < 16 and start <= end:
        div_5 = start%5 == 0
        div_7 = start%7 == 0
        inc_5 = str(start).find('5') != -1
        inc_7 = str(start).find('7') != -1

        combo = '%s%s%s%s' % (div_5, div_7, inc_5, inc_7)

        if combo not in ans:
            ans[combo] = start

        start += 1

    return sorted(ans.values())

#Test section
if __name__ == '__main__':
    print "fizz buzz 1st version:\n", fizz_buzz(18)
    print "fizz buzz 2nd version:\n", fizz_buzz2(40)
    print "fizz buzz 3rd version:\n", fizz_buzz_combos(0,1000)


