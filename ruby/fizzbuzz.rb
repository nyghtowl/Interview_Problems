'''
Fizz Buzz 

Input: list of numbers

Output: print numbers submitted except:
  if divisable by 3 - write fizz
  if divisable by 5 - write buzz
  if divisable by 15 - write fizz buzz


'''

# O(n)
def fizz_buzz(num_list)
    response = Array.new [0]
    num_list.each{ |num|
        if num % 15 == 0
            response << 'fizz buzz'
        elsif num % 5 == 0
            response << 'buzz'
        elsif num % 3 == 0
            response << 'fizz'
        else 
            response << num
        end 
    }
    response[1..num_list.length]
end

if __FILE__ == $0

    # Test section
    list_input = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    results = [1,2,'fizz',4,'buzz','fizz',7,8,'fizz','buzz',11,'fizz',13,14,'fizz buzz']

    ans = fizz_buzz(list_input) == results
    puts "%s == %s : %s" % ['fizz_buzz', results, ans]
end 

