# Petals Around The Rose
# Emily Trabert

from random import randint

def rolldice():
    dice = []

    for i in range(5):
        dice.append(randint(1,6))

    return dice

def detsol(dice):
    sol = 0
    
    for i in dice:
        if i == 3:
            sol += 2
        elif i == 5:
            sol += 4

    return sol

def main():
    print('''Let's play 'Petals Around The Rose.' The name of the game is significant.
At each turn I will roll five dice, then ask you for the score, which
will always be zero or an even number. After you guess the score, I will tell
you if you are right, or tell you the correct score if you are wrong. The game
ends when you prove that you know the secret by guessing the score correctly
six times in a row.''')
    
    correct = 0

    while correct < 6:
        
        dice = rolldice()
        sol = detsol(dice)
        print("")
        print "The five dice are:", dice[0], dice[1], dice[2], dice[3], dice[4]
        guess = input("What is the score? ")
        if guess == sol:
            print("Correct")
            correct += 1
        else:
            print"The correct score is", sol
            correct = 0

    print('''
Congratulations! You are now a member of the Fraternity of the Petals Around
The Rose. You must pledge never to reveal the secret to anyone.''')

main()
