import sys

def main():# ranking poker hands! and then... how many does player1 win (from text file)?
	lines = open('p54.in').read().split('\n') #file -> list
	player1 = []
	player2 = []
	for i in lines:
		hands = i.split(' ')
		player1.append( [x for x in hands[:5]] )
		player2.append( [x for x in hands[5:]] )


	c1 = Card('j','H')
	c2 = Card('10','H')
	c3 = Card('q','H')
	c4 = Card('k','H')
	c5 = Card('1','H')


	cards = [c1,c2,c3,c4,c5]

	h = Hand(cards)

	'''
	print h
	for card in h.c:
		print card.s, card.v

	return 0
	'''

class Card:
	def __init__(self, value, suite):
		self.v = value
		self.s = suite
		self.rank = -1
		self.Set_Rank()

	def Set_Rank(self):
		try:
			temp = int(self.v)
			if temp == 1:
				self.rank = 14
			elif temp <= 10:
				self.rank = temp
		except:
			if self.v == 'j':
				self.rank = 11
			if self.v == 'q':
				self.rank = 12
			if self.v == 'k':
				self.rank = 13

class Hand:
	def __init__(self, cards):
		self.c = cards
		self.rank = -1
		self.Set_Rank()


	def Set_Rank(self):
		vals = [i.rank for i in self.c]
		suites = [i.s for i in self.c]

		# high-card: ranks 2-14
		temp_rank = max(vals)
		self.rank = max(temp_rank, self.rank)

		# pairs: ranks 15-29, 3s 30-44
		for i in vals:
			if vals.count(i) == 2:
				temp_rank = 15 + i
				self.rank = max(temp_rank, self.rank)
			if vals.count(i) == 3:
				temp_rank = 30 + i
				self.rank = max(temp_rank, self.rank)


		'''
		 still have quite a bit more todo... and I also need to remember to include
		 the possibility of a tie on the pair or 3 of a kind, and then looking at
		 the rest of the cards...
		'''

		#royal flush
		is_royal_flush = True
		collapsed = set(suites)
		if len(collapsed) == 1: #flush
			if set(vals) == set(([10, 11, 12, 13, 14])): # royal-straight
				self.rank = sys.maxint

		print self.rank



if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
