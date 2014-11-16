import random
import itertools
import collections

def evaluate(guess, actual):
    correct = 0
    c_colors = [0]*6
    g_colors = [0]*6
    for g, a in zip(guess, actual):
        if g == a:
            correct += 1
        else:
            c_colors[a] += 1
            g_colors[g] += 1
    almost = 0
    for gc, ac in zip(g_colors, c_colors):
        almost += min(gc, ac)
    return correct, almost
    
def play(player):
    hidden = [random.randint(0,5) for _ in range(4)]
    for turn in range(12):
        player.message("You have %s guesses remaining."%(12-turn))
        guess = player.make_guess()
        evaluation = evaluate(guess, hidden)

        if evaluation[0] == 4:
            player.message('You Won in %s turns!'%(turn+1))
            return
        
        player.notify(evaluation)
    player.message('Try Again :(')

class HumanPlayer:

    def __init__(self):
        print("Welcome to the game of Mastermind!")
        print("You have 12 guess to find out a hidden combination of "
              "numbers between 0 and 5 inclusive")

    def message(self, message):
        print(message)

    def notify(self, message):
        print("right place, right color:" + str(message[0]))
        print("wrong place, right color:" + str(message[1]))

    def make_guess(self):
        while True:
            try:
                result = [int(x) for x in input('make a guess:')]
                if len(result) != 4 or \
                   not all([0<=y<=5 for y in result]):
                    raise ValueError
                return result
            except ValueError:
                print("Please input 4 numbers between 0 and 5 inclusive")

class ComputerPlayer:

    def __init__(self, talkative=False):
        self.talkative = talkative
        self.possible = list(itertools.product(range(6), repeat=4))

    def message(self, message):
        if self.talkative >= 1 or ':(' in message:
            print(message)

    def notify(self, message):
        self.possible = [x for x in self.possible
                         if evaluate(x, self.guess) == message]
        if self.talkative > 1:
            print("%s possible solutions"%len(self.possible))

    def make_guess(self):
        self.guess = random.choice(self.possible)
        return self.guess
        
