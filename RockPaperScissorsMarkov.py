from SecondOrderPredictor import *
from random import *
import math


# rpsMarkov.py

numStates = 3 # rock, paper, scissors
convert012ToRPS=["Rock","Paper","Scissors"]
resultLabels=["WIN?!?!?!","Lose","Draw"]

# /******* R, P, S*/
#    /*R*/ {2,1,0},
#    /*P*/ {0,2,1},
#    /*S*/ {1,0,2}
resultMatrix = [[2,1,0], [0,2,1], [1,0,2]]

stats = [0,0,0]
randomState = randrange(0,numStates)
predictor = SecondOrderPredictor(numStates)

print("+++++++++++++++++++++++++++++++++++++")
print("Welcome to Rock Paper Scissors MARKOV")
print("+++++++++++++++++++++++++++++++++++++")
print("The computer will use an algorithm to learn and predict the player's moves.")
print("You can enter r = Rock, p = Paper, s = Scissors, or q = Quit")
print("You can enter one letter at a time OR a series of letters (like rpsrps)")

def convertRPSTo012 (char):
    if "r" in char:
        result = 0
    elif "p" in char:
        result = 1
    elif "s" in char:
        result = 2
    return result

while True:
    # enemy chooses first
    predictedPlayerState = predictor.getPredictedState()
    if predictedPlayerState == -1:
        predictedPlayerState = randrange(0,numStates)
        print("Computer is taking a random guess")
    enemyState = (predictedPlayerState + 1) % numStates
    # print("predicted"+str(predictedPlayerState))
    # print("enemy"+str(enemyState))
    # player chooses
    playerChoice = input("> ");
    if playerChoice == 'q':
        break
    if len(playerChoice) > 1:#if player enters long string
        for i in range(0,len(playerChoice)):
            if playerChoice[i] == 'r' or playerChoice[i] == 'p' or playerChoice[i] == 's':
                playerState = convertRPSTo012(playerChoice[i])
            elif playerChoice[i] == '1' or playerChoice[i] == '2' or playerChoice[i] == '3':
                playerState = int(playerChoice[i]) - 1
            else:
                continue
            predictor.setLearn(playerState)
            result = resultMatrix[playerState][enemyState]# determine results
            stats[result] += 1
            print(resultLabels[result])
            predictedPlayerState = predictor.getPredictedState()# enemy chooses first
            if predictedPlayerState == -1:
                predictedPlayerState = randrange(0,numStates)
            enemyState = (predictedPlayerState + 1) % numStates
    elif playerChoice == 'r' or playerChoice == 'p' or playerChoice == 's':
        playerState = convertRPSTo012(playerChoice)
        print("Player choice: " + convert012ToRPS[playerState])
        print("CPU choice: " + convert012ToRPS[enemyState])
    elif playerChoice == '1' or playerChoice == '2' or playerChoice == '3':
        playerState = int(playerChoice) - 1
        print("Player choice: " + convert012ToRPS[playerState])
        print("CPU choice: " + convert012ToRPS[enemyState])
    else:
        continue
    predictor.setLearn(playerState)
    result = resultMatrix[playerState][enemyState]# determine results
    stats[result] += 1
    print(resultLabels[result])
    print("W/L/D: " + str(stats[0]) + "/" + str(stats[1]) + "/" + str(stats[2]))
    if stats[0]+stats[1] != 0:
        print("Winning "+str(math.ceil(stats[0]/(stats[0]+stats[1])*100))+"%")
    else:
        print("Winning 0%")
