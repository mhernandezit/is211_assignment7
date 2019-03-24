import random
import os

class Player(object):
    """ A player object instantiates with a user provided name and score of 0 """
    def __init__(self):
        self.score = 0
        self.turn = False
        self.name = raw_input('Enter player name: ').strip()
    
    def getScore(self):
        return self.score

    def setScore(self, points):
        self.score += points

    def getName(self):
        return self.name

    def setTurn(self, turn):
        self.turn = turn

    def getTurn(self):
        return self.turn

class Dice(object):
    """ Each dice is initialized with a random seed of 0"""
    def __init__(self):
        self.value = random.seed(0)

    def roll(self):
        """ Each dice is six sided and can return integers between 1 and 6 """
        self.value = random.randint(1, 6)
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
    def __init__(self, players=2):
        self.players = players
        self.pendingPoints = 0
        self.activePlayer = 0
        self.winner = False
        self.roll = 0
        self.turns = 0
        self.dice = Dice()
        self.scoreData = {}
        self.gameData = []
        for num in range(players):
            self.gameData.append(Player())
            self.scoreData[self.gameData[num].getName()] = self.gameData[num].getScore()
            print self.scoreData


    def addPlayer(self, name=""):
        """ Adds a new player to the gameData dictionary, the key is the player name
        the value is the player score """
        print 'Adding new player'
        self.players += 1

    def getPlayers(self):
        return self.gameData

    def getActivePlayer(self):
        return self.gameData[self.activePlayer]

    def getPendingPoints(self):
        return self.pendingPoints
    
    def getWinState(self):
        for player in self.gameData:
            print '{} player, {} score'.format(player.getName(), player.getScore())
            if player.getScore() >= 100:
                print 'We have a winner! {} with {} points'.format(player.getName(), player.getScore())
                self.winner = True
                return self.winner
            else:
                self.winner = False
                return self.winner

    def displayScores(self):
        print 'Player: Score'
        for player in self.gameData:
            print '{} : {} \n'.format(player.getName(), player.getScore())

    def getGameStatus(self):
        print '====Pig Game Status===='
        print 'Player:  Score'
        for player in self.gameData:
            print '{} : {} \n'.format(player.getName(), player.getScore())
        print '{} is rolling'.format(self.getActivePlayer().getName())
        print 'The last roll was a {}'.format(self.roll)

    def resetGame(self):
        self.players = players
        self.pendingPoints = 0
        self.activePlayer = 0
        self.winner = False
        self.roll = 0
        self.turns = 0
        self.dice = Dice()
        self.scoreData = {}
        self.gameData = []

    def playerTurn(self, player):
        while True:
            playerChoice = raw_input(
            "Please enter [h] for hold, or [r] for roll: ").strip()
            self.displayScores()
            self.getPendingPoints()
            print '{} is rolling'.format(self.getActivePlayer().getName())

            if playerChoice.lower() == 'h':
                self.gameData[self.activePlayer].setScore(self.getPendingPoints())
                self.pendingPoints = 0
                break
            elif playerChoice.lower() == 'r':
                self.roll = self.dice.roll()
                print 'You rolled a {}'.format(self.roll)
                if self.roll == 1:
                    print 'Sorry! You rolled a 1, it is the next player\'s turn'
                    self.pendingPoints = 0
                    break
                else:
                    self.pendingPoints += self.roll
                    print '{} points are pending'.format(self.getPendingPoints())
                    continue
            else:
                print "invalid entry, try again"
                continue

    def gameLoop(self):
        while not self.getWinState() == True:
            for _ in self.gameData:
                self.getGameStatus()
                self.activePlayer = (self.turns % len(self.gameData))
                self.playerTurn(self.activePlayer)
                self.turns += 1

        newGame = raw_input("Play again? [y]|[n]").strip()
        if newGame == 'y':
            self.resetGame()
            self.gameLoop()
        elif newGame == 'n':
            print 'goodbye!'
            SystemExit
        else:
            print 'Invalid entry, exiting...'
            SystemExit

    def clear(self):
        os.system('cls')

def main():
    testGame = Game()
    testGame.gameLoop()


if __name__ == '__main__':
    main()
