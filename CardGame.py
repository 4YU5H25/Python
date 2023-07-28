import random
import os
from random import randint

suits = ('Hearts','Spades','Clubs','Diamonds')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,'Nine': 9,'Ten':10 ,'Jack': 10, 'Queen':10,'King':10,'Ace':11}
playing = True

# Card Class
class Card:
    def __init__(this,suit,rank):
        this.suit = suit
        this.rank = rank 
    def __str__(this):
        return this.rank + " of " + this.suit

# Deck Card
class Deck:
    def __init__(this):
        this.deck = []
        for suit in suits:
            for rank in ranks:
                this.deck.append(Card(suit, rank))

    def __str__(this):
        deck_comp = ''
        for card in this.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: ' + deck_comp
    
    def shuffle(this):
        random.shuffle(this.deck)

    def deal(this):
        single_card = this.deck.pop()
        return single_card
    

class Hand:
    def __init__(this):
        this.cards = [] # start with empty list as we did in the Deck class
        this.value = 0  # start with zero value
        this.aces = 0   # add an attribute to keep a track of aces
    def add_card(this,card):
        #card passed in
        #from Deck.deal() --> single Card(suit,rank)
        this.cards.append(card)
        this.value += values[card.rank]

        #track aces
        if card.rank == 'Ace':
            this.aces = 1 

    def adjust_for_ace(this):
        while this.value > 21 and this.aces :
            this.value -= 10
            this.aces -= 1
        
class Chips:
    def __init__(this):
        this.total = 100
        this.bet = 0
    def win_bet(this):
        this.total += this.bet
    def lose_bet(this):
        this.total -= this.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Sorry, please provide an integer? ')
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips')
            else:
                break
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input('Hit or Stand? Enter h or s: ')
        if x[0].lower() == 'h':
            hit(deck,hand)
            # os.system('cls')
        elif x[0].lower() == 's':
            print('Player Stands Dealers Turn')
            playing = False
            # os.system('cls')
        else:
            print('Sorry, I did not understand that, Please enter h or s only')
            continue
        break

def show_some(player,dealer):
    print('Dealer\'s Hand: \nOne card Hidden! \n') 
    print(dealer.cards[1])
    print('\n' + 'Player\'s Hand: \n')
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    print('Dealer\'s Hand: ')
    for card in dealer.cards:
        print(card)
    print('\nPlayer\'s Hand: ')
    for card in player.cards:
        print(card)

def player_busts(player,dealer,chips):
    print('Bust Player')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('Wins Player')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Player wins, dealer busted')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('Player Busted, Dealer Wins')
    chips.lose_bet()

def push(player,dealer):
    print('Dealer and player tie! Push')

while True:
    print('Welcome to 4YU5H')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand,dealer_hand)

        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

            show_all(player_hand,dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
            else:
                push(player_hand,dealer_hand)

        print(' \nPlayer total chips are at: {}' .format(player_chips.total))

        newgame = input('Do you want to play again? (y/n): ')

        if newgame == 'y':
            playing = True
            continue
        else:
            print('Thank you for playing')
            break
       


