print("Please think of a number between 0 and 100!")
ans = 'n'
start = 0
end = 100

while True:
    guess = (start+end)/2

    print("Is your secret number %s?" % guess) 
    
    ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if ans == 'c':
        print("Game over. Your secret number was: %d" % guess)
        break
    elif ans == 'h':
        end = guess
        lastguess = -guess
    elif ans == 'l':
        start = guess
        lastguess = guess
    else: 
        print("Sorry, I did not understand your input")
