# COMP-3710 Final project Prisoner Dilemma simulator			
# forgiver is a bot that will cooperate until the opponent has defected more than 10 % of the time
from botBase import baseBot
class forgivingBot(baseBot):
	def __init__(self, p:float):
		# bot inherits from base class and sets it's name
		super().__init__("forgiver") 
		self.opponentDefect = 0
		self.probability =p
	def getMove(self,opponentMoves) -> bool:
		if(len(opponentMoves)==0): #for first move return 
			return baseBot.cooperate
		if opponentMoves[-1] == baseBot.defect:
			self.opponentDefect += 1
		# more than set probability mirror
		if self.opponentDefect/len(opponentMoves) >= self.probability:
			return baseBot.defect
		return baseBot.cooperate

	def newRound(self):
		self.opponentDefect = 0
#soft average

#hard average


# go by majority
