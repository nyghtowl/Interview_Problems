'''
Fizzbuzz

Input: list of integers
Output: Write a script that will print 1-100 except:

if divisable by 3 - write fizz
if divisable by 5 - write buzz
if divisable by 15 - write fizz buzz
'''

var list_of_numbers = [1, 2, 3, 4, 5, 6, 15, 28, 30, 33, 35, 36, 40, 42];

function fizzbuzz(list_of_numbers) {
	for (var i=0; i<list_of_numbers.length; i++) {
		var j = list_of_numbers[i]
		if (j%3==0 && j%5==0) {
			console.log(j, "fizz buzz");
		}
		else if (i%3==0) {
			console.log(j, "fizz");
		}
		else if (i%5==0) {
			console.log(j, "buzz");
		}
		else {
			console.log(j);
		}
	}
}

// Test section
fizzbuzz(list_of_numbers);

