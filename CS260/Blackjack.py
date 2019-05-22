import random
from time import sleep


class Cards:
    def __init__(self,decks):
        self.values = [(2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'),
                      (9, '9'), (10, '10'), (10, 'J'), (10, 'Q'), (10, 'K'), (11, 'A')]

        self.allCards = []
        for l in range(decks*4):
            for i in range(13):
                self.allCards.append(self.values[i])

class Deck:
    def __init__(self,numDecks):
        temp = Cards(numDecks)
        self.randomDeck = temp.allCards
        random.shuffle(self.randomDeck)


class Player:
    def __init__(self,name,money):
        self.name = name
        self.money = money
        self.betAmount = 0

        self.cards = []
        self.cardTotal = 0
        self.aceCount = 0

        self.move = 0
        self.bust = 0


class Computer:
    def __init__(self):

        self.cards = []
        self.cardTotal = 0
        self.aceCount = 0

        self.move = 0
        self.bust = 0


def calcTotal(name):
    total = 0
    aceCount = 0
    for i in range(len(name.cards)):
        total += name.cards[i][0]
        if name.cards[i][1] == 'Ace':
            aceCount += 1

    # if aceCount > 0:
    #     for i in range(aceCount):
    #         temp = total
    #         total = []
    #         total.extend(temp+1)
    #         total.extend(temp+11)
    #         list(dict.fromkeys(total))
    #         total.sort()

    return total, aceCount


def printCard(name):
    for i in range(len(name.cards)):
        print('[{}]'.format(name.cards[i][0]), end=' ')


def numCheck(prompt, bot, top, varType):
    while True:
        try:
            output = varType(input(prompt))
        except ValueError:
            print("Not possible input: must be between {} and {}".format(bot,top))
            continue
        else:
            if bot < output <= top:
                break

    return output


def strCheck(prompt, options):
    while True:
        try:
            output = input(prompt)
        except ValueError:
            print("Not possible input: ")
            continue
        else:
            if output in options:
                break

    return output

# -------------------- Game

speed = 1

while True:
        name = input('Enter Name: ')
        if name != '':
            break
        else:
            print('Enter name again')

money = numCheck('Enter starting money: ',0,float('Inf'),float)
deckNum = numCheck('Enter number of playing decks: ',0,10,int)

player1 = Player(name,money)
computer1 = Computer()

d = Deck(deckNum)
dLen = len(d.randomDeck)

print('\n Game is blackjack, 21 wins 1.5x, dealer hits less than 17\n')
play = 'y'

while play == 'y':

    # Reset deck when card count drops below 1/2
    if len(d.randomDeck) < dLen/2:
        d = Deck(deckNum)

    # Betting
    print('Alex has ${}'.format(player1.money))

    bet1 = numCheck('Bet amount? ',0,player1.money,float)

    player1.money = player1.money - bet1
    player1.betAmount = bet1

    # Initial Dealing - 1st card
    computer1.cards.append(d.randomDeck.pop())
    player1.cards.append(d.randomDeck.pop())

    # 2nd card
    computer1.cards.append(d.randomDeck.pop())
    player1.cards.append(d.randomDeck.pop())

    # Calculate total cards value
    player1.cardTotal, player1.aceCount = calcTotal(player1)
    computer1.cardTotal, computer1.aceCount = calcTotal(computer1)

    print('Your cards are: [{}] [{}] with total = {}'.format(player1.cards[0][1],player1.cards[1][1],player1.cardTotal))
    print('Dealer cards are: [{}] [{}]\n'.format('Facedown', computer1.cards[1][1]))
    sleep(speed)

    # Check for blackjack
    if player1.cardTotal == 21:
        if computer1.cardTotal == 21:
            print('Dealer cards are: [{}] [{}]'.format(computer1.cards[0][1], computer1.cards[1][1]))
            print('Tie - Money back\n')
            sleep(speed)
            player1.money = player1.money + player1.betAmount
            player1.betAmount = 0
        else:
            print('Blackjack!\n')
            sleep(speed)
            player1.money = player1.money + player1.betAmount*2.5
            player1.betAmount = 0
    elif computer1.cardTotal == 21:
        print('Dealer has Blackjack')
        print('Dealer cards are: [{}] [{}]\n'.format(computer1.cards[0][2], computer1.cards[1][2]))
        sleep(speed)
        player1.betAmount = 0

    # No one has blackjack
    else:

        # Hit or Stay Phase
        player1.move = int(strCheck('Enter 1 = Hit or 0 = Stay\n', ['1', '2']))

        # Hit and stay phase for player
        while player1.cardTotal <= 21 and player1.move == 1 and player1.bust == 0:
            player1.cards.append(d.randomDeck.pop())
            player1.cardTotal, player1.aceCount = calcTotal(player1)
            # Print all cards and total
            print('Players cards are',end=' ')
            printCard(player1)
            print('with total {}\n'.format(player1.cardTotal))
            sleep(speed)
            if player1.cardTotal > 21:
                player1.bust = 1
                print('Bust\n')
                sleep(speed)

            else:
                player1.move = numCheck('Enter 1 = Hit or 0 = Stay\n',-1,1,int)

        # Print all cards and total
        print('Dealer cards are',end=' ')
        printCard(computer1)
        print('with total {}\n'.format(computer1.cardTotal))
        sleep(speed)

        # Hit and stay phase for dealer
        while computer1.cardTotal <= 16 and computer1.bust == 0:
            computer1.cards.append(d.randomDeck.pop())
            computer1.cardTotal, computer1.aceCount = calcTotal(computer1)
            # Print all cards and total
            print('Dealer cards are', end=' ')
            printCard(computer1)
            print('with total {}\n'.format(computer1.cardTotal))
            sleep(speed)
            if computer1.cardTotal > 21:
                computer1.bust = 1
                print('Dealer Bust\n')
                sleep(speed)

        # Check cards phase
        # Dealer bust but not player
        if computer1.bust == 1 and player1.bust == 0:
            player1.money += player1.betAmount
            player1.betAmount
            print('You Win\n')
            sleep(speed)

        # Player bust but not Dealer
        elif computer1.bust == 0 and player1.bust == 1:
            player1.betAmount = 0
            print('Dealer Wins\n')
            sleep(speed)

        # Both bust
        elif computer1.bust == 1 and player1.bust == 1:
            player1.betAmount = 0
            print('Dealer Wins\n')
            sleep(speed)

        # Neither bust
        else:
            # Player Wins
            if player1.cardTotal > computer1.cardTotal:
                player1.money += player1.betAmount*2
                player1.betAmount = 0
                print('You Win\n')
                sleep(speed)
            # Tie
            elif player1.cardTotal == computer1.cardTotal:
                player1.money += player1.betAmount
                player1.betAmount = 0
                print('Tie money back\n')
                sleep(speed)
            # Computer Wins
            elif player1.cardTotal < computer1.cardTotal:
                player1.betAmount = 0
                print('Dealer Wins\n')
                sleep(speed)

    print('Alex has ${}'.format(player1.money))
    play = input('To play again type y: ')