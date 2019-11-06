# Abdullah Arif
# COMP-3710 Final project Prisoner Dilemma simulator
# the soft thinker is a bot that starts off cooperating and keeps 
# cooperating as long as the opponent has cooperated more than they have defected
# heavily influenced by Axelrod's soft Majo bot
from botBase import baseBot
class softThinkerBot(baseBot):
	def __init__(self):
		# bot inherits from base class and sets it's name
		super().__init__("soft thinker") 
		self.opponentDefect = 0
		self.opponentCooperate = 0
	def getMove(self,opponentMoves) -> bool:
		if len(opponentMoves)==0: #for first move always cooperate to show good will
			return baseBot.cooperate
		else:
			# store move for efficient calculation
			if opponentMoves[-1] == baseBot.cooperate:
				self.opponentCooperate += 1
			else:
				self.opponentDefect +=1
			# calculate if it should defect
			if self.opponentCooperate >= self.opponentDefect:
				return baseBot.cooperate
			else:
				return baseBot.defect
	# reset opponent moves
	def newRound(self):
		self.opponentDefect = 0
		self.opponentCooperate = 0
			
	


