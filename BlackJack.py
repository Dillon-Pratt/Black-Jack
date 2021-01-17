import random

cards = ['1','2','3','4','5','6','7','8','9','10','J','Q','K','A']


def drawCompcard():
    compCards.append(random.choice(cards))

def drawPlayercard():
    playerCards.append(random.choice(cards))

gameRunning = True

while gameRunning == True:

    compCards = []
    playerCards = []

    drawCompcard()
    drawCompcard()
    drawPlayercard()
    drawPlayercard()

    print(f"Your hand: {playerCards}")

    hitPhase = True

    while hitPhase == True:
        x = input("Would you like to [H]it or [S]tand?")

        if x.upper() == 'H':
            drawPlayercard()
            print(f"\nYour hand:{playerCards}\n")

        elif x.upper() == 'S':
            hitPhase = False

    print(f"Your hand: {playerCards}\n Computer hand: {compCards}")



    