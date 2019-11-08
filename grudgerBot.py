# Abdullah Arif
# COMP-3710 Final project Prisoner Dilemma simulator
# the grudger is a bot who starts out cooperating but if it was betrayed it always defects
from botBase import baseBot
class grudgerBot(baseBot):
	def __init__(self):
		# bot inherits from base class and sets it's name
		 super().__init__("grudger") 
		 self.grudge = False
	def getMove(self,opponentMoves) -> bool:
		if(len(opponentMoves)==0): #for first move return 
			return baseBot.cooperate
		else:
			# if not holding a grudge and bot has defected then bot will hold a grudge
			if not self.grudge and opponentMoves[-1] == baseBot.defect: 
				self.grudge = True
			if self.grudge:
				return baseBot.defect
			else:
				return baseBot.cooperate
	def newRound(self): # on new round reset the grudge
		self.grudge = False

class forgetfulGrudgerBot(baseBot):
	def __init__(self, mem):
		# bot inherits from base class and sets it's name
		super().__init__("forgetful grudger") 
		self.grudge = 0
		self.memoryLength = mem

	def getMove(self,opponentMoves) -> bool:
		if(len(opponentMoves)==0): #for first move return 
			return baseBot.cooperate
		# while in grudge mode defect
		if self.grudge >0 : 
			self.grudge -=1
			return baseBot.defect
		if opponentMoves[-1] == baseBot.defect:
			# grudge will last as long as memory
			self.grudge = self.memoryLength-1
			return baseBot.defect
		return baseBot.cooperate
	def newRound(self): # on new round reset the grudge
		self.grudge = 0

