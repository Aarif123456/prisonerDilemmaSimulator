# Abdullah Arif
# COMP-3710 Final project Prisoner Dilemma simulator
# Holds deterministic strategies as labeled in Dyson and Press' paper 
# which can be found at https://www.pnas.org/content/109/26/10409
# the basis of these strategy is to analyze the last 2 move and use a probabilistic chance to use one method

from botBase import baseBot
import random
# scenario  (D,C), (C,C),(D,D), (C,D) -> (self, opponent)
# p is the probability to cooperate depending on scenario
class deterministicBot(baseBot):
	def __init__(self,name:str, p1:float, p2:float, p3:float, p4:float):
		# bot inherits from base class and sets it's name
		super().__init__(name) 
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
		self.p4 = p4

	def getMove(self,opponentMoves) -> bool:
		if(len(opponentMoves)==0): #for first move cooperate
			self.lastMove = baseBot.cooperate
		#option 1 D,C best in terms of self-gain
		elif(opponentMoves[-1] == baseBot.defect and self.lastMove == baseBot.cooperate):
			if(random.uniform(0,100) < self.p1):
				self.lastMove = baseBot.cooperate
			self.lastMove = baseBot.defect
		# second best option C,C
		elif(opponentMoves[-1] == baseBot.cooperate and self.lastMove == baseBot.cooperate):
			if(random.uniform(0,100) < self.p2):
				self.lastMove = baseBot.cooperate
			self.lastMove = baseBot.defect
		# D,D third best option
		elif(opponentMoves[-1] == baseBot.defect and self.lastMove == baseBot.defect):
			if(random.uniform(0,100) < self.p3):
				self.lastMove = baseBot.cooperate
			self.lastMove = baseBot.defect
		# final option
		elif(opponentMoves[-1] == baseBot.cooperate and self.lastMove == baseBot.defect):
			if(random.uniform(0,100) < self.p4):
				self.lastMove = baseBot.cooperate
			self.lastMove = baseBot.defect
		return self.lastMove