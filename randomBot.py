# Abdullah Arif
# COMP-3710 Final project Prisoner Dilemma simulator
# bot that randomly chooses to cooperate or defect
from botBase import baseBot
import random
class randomBot(baseBot):
	def __init__(self):
		# bot inherits from base class and sets it's name
		 super().__init__("choose randomly") 
	def getMove(self,opponentMoves) -> bool:
		r = random.randint(0,1)
		if (r==0): #randomly cooperate
			return baseBot.cooperate
		return  baseBot.defect #otherwise defect



