import random
import os

class Player(object):
    def __init__(self):
        self.score = 0
        self.name = raw_input('Enter player name: ')
    
    def getScore(self):
        return self.score

    def setScore(self, points):
        self.score += points

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

class Dice(object):
    def __init__(self):
        self.value = random.seed(0)

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value

class Game(object):
    def __init__(self):
        self.gameData = {}
        self.pendingPoints = 0
        self.activePlayer = None
        self.winner = False
        self.roll = 0
        self.dice = Dice()

    def addPlayer(self, player):
        print 'adding player {}'.format(player.name)
        self.gameData[player.name] = player.score

    def getPlayers(self):
        return self.gameData

    def getActivePlayer(self):
        return activePlayer

    def setActivePlayer(self, player):
        self.activePlayer = player

    def getPendingPoints(self):
        return self.pendingPoints
    
    def getWinState(self):
        print self.gameData
        for name, score in self.gameData.items():
            print '{} player, {} score'.format(name, score)
            if score >= 100:
                print 'We have a winner! {} with {} points'.format(name, score)
                self.winner = True
                return self.winner
            else:
                self.winner = False
                return self.winner

    def displayScores(self):
        for name, score in self.gameData.items():
            print 'Player: Score'
            print '{} : {} \n'.format(name, score)

    def resetGame(self):
        self.gameData = {}
        self.activePoints = 0
        self.winner = False
        self.activePlayer = None

    def playerTurn(self, player):
        self.displayScores()
        self.getPendingPoints()
        print '{} is rolling'.format(self.getActivePlayer())
        print 'The last roll was a {}'.format(self.roll)
        print '{} points are pending'.format(self.getPendingPoints())
        playerChoice = raw_input(
        "Please enter [h] for hold, or [r] for roll: ").strip()
        while True:
            if playerChoice.lower() == 'h':
                self.activePlayer.setScore(self.pendingPoints)
                self.pendingPoints = 0
                self.clear()
                break
            elif playerChoice.lower() == 'r':
                self.roll = self.dice.roll()
                self.clear()
                print 'You rolled a {}'.format(self.roll)
                if self.roll == 1:
                    print 'Sorry! You rolled a 1, it is the next player\'s turn'
                    self.pendingPoints = 0
                    break
                else:
                    self.pendingPoints += self.roll
                    continue
            else:
                print "invalid entry, try again"
                continue

    def gameLoop(self):
        print "Welcome to pig!"
        playerNumber = raw_input(
            "Please enter the number of players: ")
        num = int(playerNumber)
        for _ in range(num):
            self.addPlayer(Player())

        while self.getWinState() == False:

            for player, _ in self.getPlayers().items():
                self.setActivePlayer(player)
                self.playerTurn(player)

            
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
