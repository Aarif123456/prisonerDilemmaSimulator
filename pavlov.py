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
			# If both defected it will try to forgive.
			# So, it see see-saws between tit-for-tat and forgiving. We could make this strategy
			# more advanced by remembering more
			if self.lastMove == opponentMoves[-1]: 
				self.lastMove = baseBot.cooperate
			# lastly if it cooperated and other defected switch to defect or if other cooperated and it defected then keep defecting
			else:
				self.lastMove = baseBot.defect			
		return self.lastMove


