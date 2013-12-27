/**
Seat Circle

Input: 100 chairs in a circle and they are labeled from 1 to 100

Condition: 
Pattern of change is that seat 1 is asked to leave, seat 2 is asked to stay, seat 3 is asked to leave...
Pattern continues of skipping one and asking one to leave till only one is left

Output: Return who the last person left


**/

function lastChair(numberOfChairs) {
    var index = 0,
        chairs = _.range(numberOfChairs);
    while (chairs.length > 1) {
        chairs.splice(index, 1)
        index = ++index % chairs.length;
    }
    return chairs[0] + 1;
}


// Test section
console.log('last chair is', lastChair(100));