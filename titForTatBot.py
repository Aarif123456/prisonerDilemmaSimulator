# Abdullah Arif
# COMP-3710 Final project Prisoner Dilemma simulator
# it can start off as either cooperating and defecting depending on the arguments
# afterwards it will mirror the opponent
from botBase import baseBot
class titForTatBot(baseBot):
	def __init__(self, name, sM):
		# bot inherits from base class and sets it's name
		super().__init__(name) 
		self.startingMove = sM

	def getMove(self,opponentMoves) -> bool:
		if(len(opponentMoves)==0): #for first move return 
			return self.startingMove
		else:
			return opponentMoves[-1]



