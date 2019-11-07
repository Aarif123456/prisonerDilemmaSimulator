# Abdullah Arif
# COMP-3710 Final project Prisoner Dilemma simulator
# the gradual bot is a bot who starts off cooperative and then retaliates by defecting n times for the nth defect it then gives it's opponent a chance to calm down by cooperating twice

from botBase import baseBot
class gradualBot(baseBot):
	def __init__(self):
		# bot inherits from base class and sets it's name
		super().__init__("gradual") 
		self.defectNumber = 0
		self.retaliationNumber = 0

	def getMove(self,opponentMoves) -> bool:
		#retaliate n times
		self.retaliationNumber+=1
		if(self.retaliationNumber < self.defectNumber):
			return baseBot.defect
		# cooperate 2 times after retaliating 
		if(self.retaliationNumber <self.defectNumber+2):
			return baseBot.cooperate
		#defect kick off the gradual cycle
		if(opponentMoves[-1] == baseBot.defect):
			self.defectNumber+=1
			self.retaliationNumber = 0
			return baseBot.defect
		# base action is cooperate
		return baseBot.cooperate
		
	def newRound(self):
		self.defectNumber = 0
		self.retaliationNumber = 0

