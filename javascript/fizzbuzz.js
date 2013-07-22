Write a script that will print 1-100 except:
if divisable by 3 - write fizz
if divisable by 5 - write buzz
if divisable by 15 - write fizz buzz

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

fizzbuzz(list_of_numbers);



"tail recursion" is where you can f


triple === compares types as well

falsey: evaluates to false 

an empty array is falsey

([]) ==0 true
{}


.map takes everything in an array, transforms them, and gives back a new array

switch is like an if statement (with if, else if, else if, else, but you use case)


jsonp has some downsides: you're writing the info to the page.
You can't put, delete, update

script tags trick by making the browser think it's just some javascript



caching: client "get me the leaderboard", server does all the work
browser cache is up to the browser, but you can tell it when to expire



VPN: remote access to secure things




caching levels: browser, edge (wide distribution), 

rails cache

reddis--write the code to execute on the server(main task), then
ask someone who makes sure things are cached correctly
how do I set it up for caching? To modify how long things
get cached, you can write code to specify it and it's in the
"cache control header"


"You catch onto things really fast." -Yoh Suzuki


"this" refers to that exact object, "self" lets you continue to refer to that same object 
while inside of a callback or a function executed in a different scope that has its own "this"
