
from pokereval.card import Card
from pokereval.hand_evaluator import HandEvaluator

lines = open('p054.in').read().split('\n') #file -> list
player1 = []
player2 = []
for i in lines:
	hands = i.split(' ')
	player1.append( [x for x in hands[:5]] )
	player2.append( [x for x in hands[5:]] )




hand1 = [Card(i) for i in player1[0]]
hand2 = player2[0]

print hand1, hand2






