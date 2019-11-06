# Abdullah Arif
# COMP-3710 Final project Prisoner Dilemma simulator
# one move bot only either always defect or always cooperates
from botBase import baseBot
class basicBot(baseBot):
	def __init__(self, name, a):
		# bot inherits from base class and sets it's name
		super().__init__(name) 
		self.action = a
		
	def getMove(self,opponentMoves) -> bool:
		return self.action



