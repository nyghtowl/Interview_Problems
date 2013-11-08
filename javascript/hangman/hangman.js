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

   TO DO - Add functionality to pull random word, tell the person if a letter was guessed and streamline code into smaller methods
*/

(function () {
 
  var Hangman = {};

  // Pick the word
  Hangman.App = function(){
    this.secretWordController = new Hangman.SecretWordController('at');
    this.guessCount = 2;
    this.keepGuessing();

  }

  Hangman.App.prototype.keepGuessing = function() {
    alert('Welcome to the game, Hangman! I am thinking of a word that is ' + this.secretWordController.secretWord.length + ' letters long.');

    while (this.guessCount > 0 && !this.secretWordController.isDone()){
      this.doOneTurn();
    }

    if (this.secretWordController.isDone()) {
      console.log('Congratulations, you won!');
    } else {
      console.log('Sorry, you ran out of guesses. The word was:', this.secretWordController.secretWord);      
    }
  }

  Hangman.App.prototype.doOneTurn = function() {
    console.log('You have ' + this.guessCount + ' guesses left.');
    var guess = prompt('Guess a letter:');
    var guessCorrect = this.secretWordController.processGuess(guess);

    if (guessCorrect) {
      console.log("Good guess: ");
    } else {
      console.log("Oops! That letter is not in my word:");
      this.guessCount -= 1;
    }
    console.log(this.secretWordController.getRevealed());
  }

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

  Hangman.SecretWordController.prototype.isDone = function() {
    // return this.revealedWord.indexOf('_') === -1;
    return this.revealedWord === this.secretWord;
  }

  window.Hangman = Hangman;

})();
