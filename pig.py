""" Pig game - Week 7 Assignment """
import random
import sys
import os
import argparse

class Player(object):
    """ A player object instantiates with a user provided name and score of 0 """
    def __init__(self):
        self.score = 0
        self.turn = False
        self.name = raw_input('Enter player name: ').strip()

    def getScore(self):
        """ Getter to grab the score variable """
        return self.score

    def setScore(self, points):
        """ Score setter method """
        self.score += points

    def getName(self):
        """ Name getter """
        return self.name

    def setTurn(self, turn):
        """ Turn setter """
        self.turn = turn

    def getTurn(self):
        """ Turn getter """
        return self.turn

class Dice(object):
    """ Each dice is initialized with a random seed of 0"""
    def __init__(self):
        self.value = random.seed(0)

    def roll(self):
        """ Each dice is six sided and can return integers between 1 and 6 """
        self.value = random.randint(1, 6)
        return self.value

    def getCurrentRoll(self):
        """ Getter method to grab the value variable """
        return self.value

class Game(object):
    """ The Game object holds the bulk of the work for the Pig game
    gameData holds the player objects
    pendingPoints show how many points are in the bucket to be consumed
    activePlayer is the player name that is currently rolling
    winner boolean determines if there is a winner of the game
    roll is the current roll
    dice is the dice object currently being used
    """
    def __init__(self):
        self.pendingPoints = 0
        self.activePlayer = 0
        self.turns = 0
        self.dice = Dice()
        self.scoreData = {}
        self.gameData = []

    def addPlayer(self, index):
        """ Adds a new player to the gameData list, also updates the scoreData dictionary"""
        self.gameData.append(Player())
        self.scoreData[self.gameData[index].getName()] = self.gameData[index].getScore()

    def addPlayersToGame(self, players):
        """ Adds a multiple of players to the game """
        for player in range(players):
            self.addPlayer(player)

    def getActivePlayer(self):
        """ Getter method to pull player objects """
        return self.gameData[self.activePlayer]

    def getPendingPoints(self):
        """ Getter method to pull pending points """
        return self.pendingPoints

    def getWinState(self):
        """
        Checks player scores in the active player objects, if any of the scores are
        above 100, it returns True.
        Otherwise the function returns False.
        The Truth/False values directly correlate to the while statements which run the
        gameLoop
        """
        for player in self.gameData:
            if player.getScore() >= 100:
                return True
        return False

    def getGameStatus(self):
        """ Print functions - builds the game board, prints current status"""
        os.system('cls')
        print '====   Pig Game   ====\n'
        print '{:15} : {:>6}\n'.format('Player', 'Score')
        for player in self.gameData:
            print '{:15} : {:6} \n'.format(player.getName(), player.getScore())
        print '{} is rolling'.format(self.getActivePlayer().getName())
        if self.dice.getCurrentRoll() == 1:
            print 'The last roll was {}, next player\'s turn!'.format(self.dice.getCurrentRoll())
        else:
            print 'The last roll was {}'.format(self.dice.getCurrentRoll())
        print 'Pending Points: {:>10}'.format(self.getPendingPoints())

    def playerTurn(self, player):
        """ Interactive player turn, asks for user input about whether they want
        to roll or hold.
        Depending on the outcome of the roll, the loop will either exit due to
        a player rolling 1 or if the player has over 100 points """
        player.setTurn(True)
        while player.getTurn() and not self.getWinState():
            self.getGameStatus()
            self.getPendingPoints()
            playerChoice = raw_input(
                "Please enter [h] for hold, or [r] for roll: ").strip()

            if playerChoice.lower() == 'h':
                player.setScore(self.getPendingPoints())
                self.pendingPoints = 0
                player.setTurn(False)
            elif playerChoice.lower() == 'r':
                roll = self.dice.roll()
                if roll == 1:
                    self.pendingPoints = 0
                    player.setTurn(False)
                else:
                    self.pendingPoints += roll
                    continue
            else:
                raw_input("Invalid entry, please enter [h] for hold or [r] for roll")
                continue

    def gameLoop(self, players=2):
        """
        The game loop sets up the players in the game, and builds out a turn
        order for the players.  Once the win state is reached, the function allows for
        a game restart with user input.

        Args:
            players (optional): Number of players in the game - defaults to 2
        """
        for player in range(players):
            self.addPlayer(player)

        while not self.getWinState():
            for player in self.gameData:
                self.activePlayer = (self.turns % len(self.gameData))
                self.playerTurn(player)
                self.turns += 1
        for player in self.gameData:
            if player.getScore() >= 100:
                print '\nWe have a winner! {} with {} points'.format(
                    player.getName(), player.getScore())
        newGame = raw_input("\nPlay again? [y]|[n]: ")
        if newGame == 'y':
            try:
                newGamePlayers = int(raw_input("\nEnter number of players in this game: "))
            except ValueError:
                print 'Invalid Input, running game with default of 2 players'
            else:
                self.resetGame()
                self.gameLoop(newGamePlayers)
            finally:
                self.resetGame()
                self.gameLoop()
        elif newGame == 'n':
            print 'Thanks for playing! Goodbye!'
            sys.exit()
        else:
            print 'Invalid entry, exiting...'
            sys.exit()

    def resetGame(self):
        """ Re-initializes game variables for a fresh start """
        self.pendingPoints = 0
        self.activePlayer = 0
        self.turns = 0
        self.dice = Dice()
        self.scoreData = {}
        self.gameData = []

def main():
    """ Main method to run our game

    """
    newGame = Game()
    parser = argparse.ArgumentParser()
    parser.add_argument('--numPlayers',
                        help='Number of players in our game',
                        type=int, required=False)
    args = parser.parse_args()
    if args.numPlayers:
        newGame.gameLoop(args.numPlayers)
    else:
        newGame.gameLoop()


if __name__ == '__main__':
    main()
