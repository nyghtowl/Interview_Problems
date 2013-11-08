// Hangman Game


(function () {
 
  var Hangman = {};

  // Pick the word
  Hangman.App = function(){
    this.secretWordController = new Hangman.SecretWordController('art');
    this.keepGuessing();

    console.log('Thanks for playing!')
  }

  Hangman.App.prototype.keepGuessing = function() {
    alert('Welcome to the game, Hangman! I am thinking of a word that is ' + this.secretWordController.secretWord.length + ' letters long.');
    while (!this.secretWordController.isDone()){
      this.doOneTurn();
    }
  }

  Hangman.App.prototype.doOneTurn = function() {
    var guess = prompt('Guess a letter.');
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
