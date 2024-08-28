import random

turn = 0
playerList = []
botList = []
win = False

def space():
    print(" ")

def roll(roundScore):
    roll = random.randint(1,6)
    if roll == 1:
        roundScore = 0
    else:
        roundScore = roundScore + roll
        
    return [roll, roundScore]

def playerTurn():
    global playerList

    for i in range(len(playerList)):
        inPlay = True
        playerRound = 0

        print(f'{playerList[i][0]}: Turn {turn}')
        print(f'Your Current Score is: {playerList[i][1]}')
        print("This Round: " + str(playerRound))

        while inPlay:
            play = input("Would you like to roll or bank? ")
            if play == "roll":
                space()
                rollResult = roll(playerRound)

                if rollResult[0] == 1:
                    inPlay = False
                    print("Looks like you rolled a 1, no score for this round.")
                    space()
                else:
                    print("You Rolled " + str(rollResult[0]))
                    print("This Round: " + str(rollResult[1]))
                    playerRound = rollResult[1]
            elif play == "bank":
                space()
                playerList[i][1] += playerRound
                inPlay = False
            elif play == "pWTest":
                playerRound = 100
            elif play == "bWTest":
                bot = int(input("Which bot would you like to increase the score? Enter 0 for all. "))
                if bot == 0:
                    for i in range(len(botList)):
                        botList[i][1] = 100
                else:
                    try:
                        botList[(bot - 1)][1] = 100
                    except IndexError:
                        print("That bot does not exist")
                        continue
            else:
                print("You must choose to either bank or roll")
    

def botTurn():
    global botList
    
    for i in range(len(botList)):
        inPlay = True
        playerRound = 0

        print(f'{botList[i][0]}: Turn {turn}')
        print(f'Current score is {botList[i][1]}')
        print("This Round: " + str(playerRound))

        while inPlay:
            if playerRound < 15:
                play = "roll"
            else:
                play = "bank"
            if play == "roll":
                space()
                rollResult = roll(playerRound)

                if rollResult[0] == 1:
                    inPlay = False
                    print(f'{botList[i][0]} rolled a 1, no score this round.')
                    space()
                else:
                    print(f'{botList[i][0]} rolled {rollResult[1]}')
                    print("This Round: " + str(rollResult[1]))
                    playerRound = rollResult[1]
            elif play == "bank":
                space()
                botList[i][1] += playerRound
                inPlay = False

def winTest():
    global win
    global playerList
    global botList
    winGroup = []
    position = 1
    
    for index in playerList:
        if index[1] >= 100:
            winGroup.append(index)

    for index in botList:
        if index[1] >= 100:
            winGroup.append(index)

    if len(winGroup) == 1:
        win = True
        print(f'Congratulations {winGroup[0][0]}! You won with {winGroup[0][1]} points on turn {turn}')
    elif len(winGroup) > 1:
        win = True
        print(f'Congratulations {len(winGroup)} players Broke 100 points on turn {turn}!')
        leaderboard = sorted(winGroup, key = lambda x: x[1])
        leaderboard.reverse()
        print(f'The overal winner is {leaderboard[0][0]} with a score of {leaderboard[0][1]}!')
        space()
        print("Here is the winners leaderboard.")
        for index in leaderboard:
            print(f'{position}. {index[0]}, {index[1]}')
            position += 1
            if position >= 1001:
                break

def main():
    global turn
    
    print("Welcome to the Game of Pig.")
    print("Your Goal is to get 100 points or more to win.")
    print("To do this each turn you have the choice to either roll or bank.")
    print("If you choose to roll you will roll a 6 sided die and have the oportunity to add 2-6 points to your round score. However if you roll a 1 then your round score goes to zero the turn is over")
    print("If you choose to bank then your round score getts added to your total score and the turn is over.")
    print("You only win if you bank your points")
    print("Good luck")
    space()
    
    for i in range(int(input("How many players are there? "))):
        print(f'Player {i + 1}')
        name = input("What is your Name? ")
        playerList.append([name, 0])
        
    for i in range(int(input("How many Bots would you like to play against? "))):
        botNum = str(f'Bot {i + 1}')
        botList.append([botNum, 0])
        
    space()
    
    print("Here is the player list.")
    
    for index in playerList:
        print(index[0])
        
    for index in botList:
        print(index[0])
        
    space()
    
    while not win:
        turn += 1
        print(turn)
        playerTurn()
        botTurn()
        winTest()
        
main()  
