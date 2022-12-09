import random 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing=True

'''card class'''

class Card():
	def __init__(self,suit,rank):
		self.suit=suit
		self.rank=rank
	def __str__(self):
		return self.suit+" of "+self.rank
'''deck 
	contains every card 
	add all cards self.deck'''
class Deck():
	def __init__(self):
		self.deck=[]
		for s in suits:
			for r in ranks:
				self.deck.append(Card(s,r))
	'''def __str__(self):
        deck_comp =''
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp'''			
	def shuffle(self):
		random.shuffle(self.deck)
	def deal(self):
		single_card=self.deck.pop()
		return single_card


'''hand
	hand contains cards 
	cards will have specific suit and rank
	if we have ace we can use it as 1 or 11
	if our count exceds 21 and we also have ace we can use it as 1
	so we have to maintain separate count for aces'''
class Hand():
	def __init__(self):
		self.cards=[]
		self.value=0
		self.ace=0
	def addcard(self,card):
		self.cards.append(card)
		self.value+=values[card.rank]
		if card.rank=="Ace":
			self.ace+=1
	def adjust(self):
		while self.value > 21 and self.ace:
			self.value-=10
			self.ace-=1

''' amount to bet
	so need an account 
	if there is sufficient amount we can play
	if we win amount is added to our account
	if we loos amount will be deducted from our accont '''
class Chips():
	def __init__(self):
		self.amt=100
		self.bet=0
	def win(self):
		self.amt+=self.bet
	def lost(self):
		self.amt-=self.bet


def take_bet(chips):
	while True:
		try:
			chips.bet=int(input("enter u r bet amount\n"))
		except ValueError:
			print("values must be ints\n")
		else:
			if chips.bet > chips.amt:
				print("enter valid amount whit in",chips.amt)
			else:
				break

def hit(deck,hand):
	hand.addcard(deck.deal())
	hand.adjust()
def hit_r_stand(deck,hand):
	global playing
	#playing = True
	while True:
		x=input("u want to stand or hit 'h','s'")
		if x[0]=='h':
			hit(deck,hand)
		elif x[0]=='s':
			print("player stands ,dealer plays")
			playing=False
		else:
			print("try again")
			continue
		break
'''first time we only show both of player cards and one of dealer cards
'''		
def show_some(plyr,dealer):
	print("dealer hand\n","<card hidden>")
	for i in range(1,len(dealer.cards)):
		print(dealer.cards[i])
	print("player hand\n")
	for i in range(len(plyr.cards)):
		print(plyr.cards[i])
'''later we reveals all cards'''
def show_all(plyr,dealer):
	print("dealer hand\n")
	for i in range(len(dealer.cards)):
		print(dealer.cards[i])
	print("value of dealer's hand ",dealer.value)	
	print("player hand\n")
	print(*plyr.cards,sep="\n")
	print("value of plyr hand ",plyr.value)

def plyr_busts(plyr_hand,dealer_hand,plyr_chips):
	print("\n __--player busts--__\n")
	plyr_chips.lost()
def dealer_busts(plyr_hand,dealer_hand,plyr_chips):
	print("\n __--dealer busts--__\n")
	plyr_chips.win()
def plyr_win(plyr_hand,dealer_hand,plyr_chips):
	print("\n__--player wins--__\n")
	plyr_chips.win()
def dealer_win(plyr_hand,dealer_hand,plyr_chips):
	print("__--dealer wins--__\n")
	plyr_chips.lost()			
''' now entire game goes like this
	first distribute cards 
	then take bet
	show the cards 
	hit or stand (plyrs or dealers)
	show all cards
	compare the values and diside the winner
	adding amount to winner
	'''
while True:
		print("Welcome to the Black Jack game\n")
		deck=Deck()
		deck.shuffle()

		plyr_hand=Hand()
		plyr_hand.addcard(deck.deal())
		plyr_hand.addcard(deck.deal())

		dealer_hand=Hand()
		dealer_hand.addcard(deck.deal())
		dealer_hand.addcard(deck.deal())

		plyr_chips=Chips()
		take_bet(plyr_chips)

		show_some(plyr_hand,dealer_hand)
		print("__--__")
		while playing:
			hit_r_stand(deck,plyr_hand)
			show_some(plyr_hand,dealer_hand)
			print("__--__")
			if plyr_hand.value > 21:
				plyr_busts(plyr_hand,dealer_hand,plyr_chips)
				break	
		if plyr_hand.value<21:
			while dealer_hand.value<17:
				hit(deck,dealer_hand)
		print("__--__")
		show_all(plyr_hand,dealer_hand)		
		print("__--__")		
		if plyr_hand.value > dealer_hand.value and plyr_hand.value < 21:
			plyr_win(plyr_hand,dealer_hand,plyr_chips)
		elif dealer_hand.value > 21:
			dealer_busts(plyr_hand,dealer_hand,plyr_chips)
		elif dealer_hand.value > plyr_hand.value:
			dealer_win(plyr_hand,dealer_hand,plyr_chips)
		elif plyr_hand.value > 21:
			plyr_busts(plyr_hand,dealer_hand,plyr_chips)
		else:
			print("Tie")	

		print("player account ",plyr_chips.amt)
		
		new=input("Would u like to play again? Enter 'y' or 'n'\n")
		if new=='y':
			playing=True
			continue
		else:
			print("___---- Thanks for playing----___")
			break


