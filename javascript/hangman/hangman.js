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


*/

(function () {
    

  var Hangman = {};


  Hangman.App = function(){
    var word = this.pickSecretWord();
    
    this.secretWordController = new Hangman.SecretWordController(word);
    this.remainingGuesses = 8;
    this.guessList = [];
    this.playGame();
  }

  Hangman.App.prototype.pickSecretWord = function() {
    return words[Math.floor(Math.random() * words.length)];
  };

  Hangman.App.prototype.guessedAlready = function(guess){
    if (this.guessList.indexOf(guess) !== -1){
=======
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
>>>>>>> f8d62b1f07d569066c5dad5df7ea3f4c6e69c4fa
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
<<<<<<< HEAD

  Hangman.App.prototype.playGame = function() {
    alert('Welcome to the game, Hangman! I am thinking of a word that is ' + this.secretWordController.secretWord.length + ' letters long.');

=======

  Hangman.App.prototype.playGame = function() {
    console.log('Welcome to the game, Hangman! I am thinking of a word that is ' + this.secretWordController.secretWord.length + ' letters long.');

>>>>>>> f8d62b1f07d569066c5dad5df7ea3f4c6e69c4fa
    while (this.remainingGuesses > 0 && !this.secretWordController.isFullyRevealed()){
      this.doOneTurn();
    }
    this.checkDone();

  };

<<<<<<< HEAD
  Hangman.App.prototype.doOneTurn = function() {
    console.log('You have ' + this.remainingGuesses + ' guesses left.');
    var guess = prompt('Guess a letter:');
    var guessedAlready = this.guessedAlready(guess);
    var matched = this.secretWordController.processGuess(guess);

    if (guessedAlready){
      console.log("Oops! You guessed that letter already:");
    } else if (matched) {
      console.log("Good guess: ");
    } else {
      console.log("Oops! That letter is not in my word:");
      this.remainingGuesses -= 1;
    }
    
    console.log(this.secretWordController.getRevealed());

=======
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

>>>>>>> f8d62b1f07d569066c5dad5df7ea3f4c6e69c4fa
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
  };

  window.Hangman = Hangman;

})();
