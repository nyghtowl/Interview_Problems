'''
Anagram 
(A word, phrase, or name formed by rearranging the letters of anothe)

Give a list of strings, return a list of anagram sets just from the original input.

Example:
    Input: ['cat', 'tablet', 'wolf', 'act', 'battle', 'flow', 'batlet', 'food']
    Output: [['cat', 'act'], ['tablet', 'battle', 'batlet'], ['wolf', 'flow']]

Note: It does not generate any new words that are not in the input.

'''

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