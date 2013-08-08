function lastChair(numberOfChairs) {
    var index = 0,
        chairs = _.range(numberOfChairs);
    while (chairs.length > 1) {
        chairs.splice(index, 1)
        index = ++index % chairs.length;
    }
    return chairs[0] + 1;
}


console.log('last chair is', lastChair(100));