// Anagram

function anagram(words) {
    var matches = {}

    for (var word = 0; word <words.length; word ++){
        var key = word.split().sort.join();
        if key in words.list {
            matches.append(key:word);
        }
        else{
            matches[key] = word;
        }
    }
    console.log(matches);
}


var words = ['cat', 'tablet', 'wolf', 'act', 'battle', 'flow', 'batlet', 'food']

anagram(words);