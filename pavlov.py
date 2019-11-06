# Abdullah Arif
# COMP-3710 Final project Prisoner Dilemma simulator
# the pavlov bot cooperates on the first move and defect if the players had two different previous move
# this strategy is also called win-stay-lose-shift 
from botBase import baseBot
class pavlovBot(baseBot):
	def __init__(self):
		# bot inherits from base class and sets it's name
		super().__init__("pavlov") 
		

	def getMove(self,opponentMoves) -> bool:
		if(len(opponentMoves)==0): #for first move cooperate
			self.lastMove = baseBot.cooperate
		else:
			# if last move match then cooperate
			if self.lastMove == opponentMoves[-1]: 
				self.lastMove = baseBot.cooperate
			else:
				self.lastMove = baseBot.defect			
		return self.lastMove


