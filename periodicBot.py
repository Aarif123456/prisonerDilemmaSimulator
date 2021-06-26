# COMP-3710 Final project Prisoner Dilemma simulator
# the periodic bot is a class of bots that will cycle through a given pattern
# for the start I am going to use the pattern ddc, ccd and cd feel free to add your own cyclic pattern
from botBase import baseBot
class periodicBot(baseBot):
	def __init__(self, name, c):
		# bot inherits from base class and sets it's name
		super().__init__(name) 
		self.cycle = c
		self.pos = -1

	def getMove(self,opponentMoves) -> bool:
		# use modulus to create a cycle
		self.pos = (self.pos +1) % len(self.cycle) 
		return self.cycle[self.pos]
	
	# reset cycle to start
	def newRound(self):
		self.pos = -1
			
	


