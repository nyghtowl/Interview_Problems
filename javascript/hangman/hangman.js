// Hangman Game


(function () {
 
  var Hangman = {};

  // Pick the word
  Hangman.App = function(){
    this.secretWordController = new Hangman.SecretWordController('cheese');

    while (!this.secretWordController.isDone()){
      this.doOneTurn();
    }
  }

  Hangman.App.prototype.doOneTurn = function() {
    var guess = prompt('Welcome to the game. Guess a letter.');
    this.secretWordController.processGuess(guess);
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
