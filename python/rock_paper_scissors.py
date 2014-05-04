'''
Rock / Paper / Scissors

Opponent Plays:
60% Rock
30% Scissors
10% Paper

Play 10 rounds and get $10 if you win 
What is the most optimal hand to play with what you know of your opponent?
Score / Points gain
win = +1 Point
lose = -1 Point
Tie = 0 Points

Input: score, round
Output: expected value
'''

def rock_game(round, score):
    if round == 0:
        if score > 0:
            return $10
        elif score == 0:
            return $0
        else:
            return -$10
    else:
        r -= 1 
        # Take max expected value if you play rock vs play paper strategy 
        return max((.6rock_game(r, score+0)*.3rock_game(r, score+1)*.1rock_game(r, score-1)), (.6rock_game(r, score+1)*.3rock(_gamer, score-1)*.1rock_game(r, score+0)))
