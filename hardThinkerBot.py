# Abdullah Arif
# COMP-3710 Final project Prisoner Dilemma simulator
# the hard majority is a bot that starts off defecting and keeps 
# defecting as long as the opponent has defected more than they have cooperated
# heavily influenced by Axelrod's hard Majority bot
from botBase import baseBot
class hardThinkerBot(baseBot):
	def __init__(self):
		# bot inherits from base class and sets it's name
		super().__init__("hard majority") 
		self.opponentDefect = 0
		self.opponentCooperate = 0
		
	def getMove(self,opponentMoves) -> bool:
		if len(opponentMoves)==0: #for first move always defect
			return baseBot.defect
		else:
			# store move for efficient calculation
			if opponentMoves[-1] == baseBot.cooperate:
				self.opponentCooperate += 1
			else:
				self.opponentDefect +=1
			# calculate if it should defect
			if self.opponentDefect >= self.opponentCooperate:
				return baseBot.defect
			else:
				return baseBot.cooperate
	# reset opponent moves
	def newRound(self):
		self.opponentDefect = 0
		self.opponentCooperate = 0
			
	


