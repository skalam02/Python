import random


class Player(object):
    def __init__(self, money=500):
        self.money = money

    def add_money(self,amount):
        self.money += amount

    def subtract_money(self,amount):
        self.money -= amount


def start_game():

    player1 = Player()
    
    def ace_checkerbool(lists):
        if 'AH' in lists:
            return 'AH'
        elif 'AD' in lists:
            return 'AD'
        elif 'AQ' in lists:
            return 'AQ'
        elif 'AC' in lists:
            return 'AC'

    def ace_checkercard(lists):
        if 'AH' in lists:
            return 'AH'
        elif 'AD' in lists:
            return 'AD'
        elif 'AQ' in lists:
            return 'AQ'
        elif 'AC' in lists:
            return 'AC'

    def scoretotal(lst):
        total = 0
        for item in lst:
            total += values[item]

        return total

    def blackjack_check(player):
        if (values[player[0]] + values[player[1]] == 21):
            return True

    deck = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH',
            'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
            'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS',
            'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC']

    values = {'AH': 11, '2H': 2, '3H': 3, '4H': 4, '5H': 5, '6H': 6, '7H': 7, '8H': 8, '9H': 9, '10H': 10, 'JH': 10,
              'QH': 10, 'KH': 10,
              'AD': 11, '2D': 2, '3D': 3, '4D': 4, '5D': 5, '6D': 6, '7D': 7, '8D': 8, '9D': 9, '10D': 10, 'JD': 10,
              'QD': 10, 'KD': 10,
              'AS': 11, '2S': 2, '3S': 3, '4S': 4, '5S': 5, '6S': 6, '7S': 7, '8S': 8, '9S': 9, '10S': 10, 'JS': 10,
              'QS': 10, 'KS': 10,
              'AC': 11, '2C': 2, '3C': 3, '4C': 4, '5C': 5, '6C': 6, '7C': 7, '8C': 8, '9C': 9, '10C': 10, 'JC': 10,
              'QC': 10, 'KC': 10}

    shuffled_deck = random.sample(deck, len(deck))

    while True:

        bet_amount = int(raw_input("How much would you like to bet?"))
        player1.subtract_money(bet_amount)

        # deal cards
        player = []
        dealer = []

        player.append(shuffled_deck.pop())
        dealer.append(shuffled_deck.pop())
        player.append(shuffled_deck.pop())
        dealer.append(shuffled_deck.pop())

        print "Players hand: " + player[0] + " " + player[1]
        print "Dealers hand: " + dealer[0] + " X"

        if blackjack_check(player):
            print "Player has blackjack!"
            player1.add_money(bet_amount+bet_amount*1.5)
            print "Player has %d dollars" %player1.money
            continue

        elif blackjack_check(dealer):
            print "Dealer has blackjack!"
            print "Player has %d dollars" % player1.money
            continue

        playertotal = scoretotal(player)
        dealertotal = scoretotal(dealer)

        while (True):
            if playertotal > 21:
                if (ace_checkerbool(player)):
                    values[ace_checkercard(player)] = 1
                    print player
                else:

                    print "BUST, your score is %d" % playertotal
                    print "Player has %d dollars" % player1.money
                    break
            playertotal = scoretotal(player)
            response = raw_input("Your score is %d, would you like to hit or stand? " % playertotal)
            if response == 'hit':
                player.append(shuffled_deck.pop())
                playertotal = scoretotal(player)
                print "Players hand: ", player
            else:
                break

        if playertotal>21:
            continue

        while True:
            if dealertotal < 17:
                dealer.append(shuffled_deck.pop())
                dealertotal = scoretotal(dealer)
                continue
            elif dealertotal > 21:
                print "Dealers hand: ", dealer
                print "Dealer busted with a total of %d" % dealertotal
                break
            else:
                print "Dealers total is %d" % dealertotal
                break

        if dealertotal>21 or playertotal>dealertotal:
            player1.add_money(bet_amount*2)
        elif playertotal == dealertotal:
            player1.add_money(bet_amount)

        print "Player has %d dollars" %player1.money

start_game()
