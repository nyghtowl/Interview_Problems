// Hangman Game

/*
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Find all words that are the length and most freq word
    Find all words with the first hit letter in that position and most freq word

    - Pseudocode on how to code this 
    loop word list and pull the ones match conditions (length, position of guessed letters)
    calc frequency of the letters in subset
    go through the list from high to low in guessing till right
    if right then reset subset of search
  
    NEXT TIME - Compare calc prob of choosing a letter based on spot 
        do one that uses total across open spots vs top freq for specific spots

      determine success rate

      create a html view


*/

// weakness: peacock

(function () {
  
  var Hangman = {};

  Hangman.HumanPlayer = function () { };
  Hangman.HumanPlayer.prototype.doTurn = function () {
    return prompt('Guess a letter:');
  };
  Hangman.HumanPlayer.prototype.afterTurn = function () { };



  Hangman.RobotPlayer = function (wordLength) {
    this.corpus = _.filter(words, function (word) { return word.length === wordLength; });
    this.possibleGuesses = 'abcdefghijklmnopqrstuvwxyz'.split('');
    this.recomputeCounts();
  };

  Hangman.RobotPlayer.prototype.doTurn = function (revealed) {
    var alphabet = this.possibleGuesses;
    var guess = alphabet[Math.floor(Math.random() * alphabet.length)];

    var max = 0, maxLetter = alphabet[0];
    _.each(this.counts, function (count, letter) {
      if (count > max) {
        max = count;
        maxLetter = letter;
      }
    });

    return maxLetter;
  };

  Hangman.RobotPlayer.prototype.afterTurn = function (guess, matched, revealed) {

    this.possibleGuesses = _.without(this.possibleGuesses, guess);
    delete this.counts[guess];

    if (matched) {
      this.trimDownCorpus(revealed);
      this.recomputeCounts();
    }

  };

  Hangman.RobotPlayer.prototype.trimDownCorpus = function (revealed) {
    var template = '^'+revealed.replace(/_/g, '.')+'$';
    var pattern = new RegExp(template, 'g');
    this.corpus = _.filter(this.corpus, function (word) {
      return word.match(pattern);
    });
  };

  Hangman.RobotPlayer.prototype.recomputeCounts = function (guess, matched, revealed) {
    var counts = {};
    _.each(this.possibleGuesses, function (letter) {
      counts[letter] = 0;
    });
    _.each(this.corpus, function (word) {
      var uniqueLetters = _.uniq(word.split(''));
      _.each(uniqueLetters, function (letter) {
        counts[letter]++;
      });
    });
    this.counts = counts;
  };





  // Pick the word
  Hangman.App = function () {
    var word = this.pickSecretWord();
    //word = 'eat'; // todo: remove later
    this.secretWordController = new Hangman.SecretWordController(word);
    this.remainingGuesses = 10;
    this.guessList = [];
    this.player = new Hangman.RobotPlayer(word.length);
    this.playGame();
  };

  Hangman.App.prototype.pickSecretWord = function() {
    return words[Math.floor(Math.random() * words.length)];
  };

  Hangman.App.prototype.guessedAlready = function(guess){
    if (this.guessList.indexOf(guess) !== -1){
      //console.log(this.guessList.indexOf(guess))
      return true;
    } else {
      this.guessList.push(guess);
      return false;
    }
  };

  Hangman.App.prototype.checkDone = function() {
    
    if (this.secretWordController.isFullyRevealed()) {
      console.log('Congratulations, you won!');
    } else {
      console.log('Sorry, you ran out of guesses. The word was: ', this.secretWordController.secretWord);      
    }
  };

  Hangman.App.prototype.playGame = function() {
    console.log('Welcome to the game, Hangman! I am thinking of a word that is ' + this.secretWordController.secretWord.length + ' letters long.');

    while (this.remainingGuesses > 0 && !this.secretWordController.isFullyRevealed()){
      this.doOneTurn();
    }
    this.checkDone();

  };

  Hangman.App.prototype.doOneTurn = function () {

    var guess = this.player.doTurn();
    if (!guess) return;

    var guessedAlready = this.guessedAlready(guess);
    var matched = this.secretWordController.processGuess(guess);
    var revealed = this.secretWordController.getRevealed();
    var remaining = '(' + this.remainingGuesses + ' remaining)';
    var message = '%c ', color = 'color:#fff;';

    if (guessedAlready) {
      message += 'Oops! You guessed ' + guess + ' already. ';
      color += 'background-color:orange';
    } else if (matched) {
      message += guess + ' was a good guess! ';
      color += 'background-color:green';
    } else {
      message += 'Oops! That ' + guess + ' is not in my word. ';
      color += 'background-color:red';
      this.remainingGuesses -= 1;
    }

    console.log(message, color, revealed, remaining);
    this.player.afterTurn(guess, matched, revealed);

  };

  Hangman.SecretWordController = function (secretWord) {
    this.secretWord = secretWord;  
    this.revealedWord = secretWord.replace(/./g, '_');
  };

  Hangman.SecretWordController.prototype.getSecret = function () {
    return this.secretWord; // accessor
  };

  Hangman.SecretWordController.prototype.getRevealed = function () {
    return this.revealedWord; // accessor
  };

  Hangman.SecretWordController.prototype.processGuess = function (guess) {
    if (this.secretWord.indexOf(guess) !== -1){
      var new_word = '';
      for (var i = 0; i < this.secretWord.length; i++) {
        new_word += this.secretWord[i] === guess ? guess : this.revealedWord[i];
      }
      this.revealedWord = new_word;
      return true;
    } else {
      return false; 
    }
  };

  Hangman.SecretWordController.prototype.isFullyRevealed = function() {
    // return this.revealedWord.indexOf('_') === -1;
    return this.revealedWord === this.secretWord;
  }

  window.Hangman = Hangman;

})();
