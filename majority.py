# Abdullah Arif
# COMP-3710 Final project Prisoner Dilemma simulator
# holds bots that look at the majority of the decision the opponent has
from botBase import baseBot

# the hard majority is a bot that starts off defecting and keeps 
# defecting as long as the opponent has defected more than they have cooperated
# heavily influenced by Axelrod's hard Majority bot
class historyBot(baseBot):
	def __init__(self, name):
		# bot inherits from base class and sets it's name
		super().__init__(name) 
		self.opponentDefect = 0
		self.opponentCooperate = 0

	def newRound(self):
		self.opponentDefect = 0
		self.opponentCooperate = 0

class forgetfulMajorityBot(historyBot): 
	def __init__(self, name, m:int):
		super().__init__(name) 
		self.memory = m
	def getMove(self,opponentMoves) -> bool:
		if len(opponentMoves)==0: #for first move always cooperate
			return baseBot.cooperate
		if opponentMoves[-1] == baseBot.cooperate:
			self.opponentCooperate += 1
		else:
			self.opponentDefect +=1
		# start forgetting
		if(len(opponentMoves)>= self.memory):
			if opponentMoves[len(opponentMoves)-memory] == baseBot.cooperate:
				self.opponentCooperate -= 1
			else:
				self.opponentDefect -=1
		if self.opponentCooperate >= self.opponentDefect:
			return baseBot.cooperate
		return baseBot.cooperate


class hardMajorityBot(historyBot): 
	def __init__(self):
		# bot inherits from base class and sets it's name
		super().__init__("hard majority") 
		
	def getMove(self,opponentMoves) -> bool:
		if len(opponentMoves)==0: #for first move always defect
			return baseBot.defect
		# store move for efficient calculation
		if opponentMoves[-1] == baseBot.cooperate:
			self.opponentCooperate += 1
		else:
			self.opponentDefect +=1
		# calculate if it should defect
		if self.opponentDefect >= self.opponentCooperate:
			return baseBot.defect
		return baseBot.cooperate
	
	

# the soft majority is a bot that starts off cooperating and keeps 
# cooperating as long as the opponent has cooperated more than they have defected
# heavily influenced by Axelrod's soft Majo bot
class softMajorityBot(historyBot):
	def __init__(self):
		# bot inherits from base class and sets it's name
		super().__init__("soft majority") 
	def getMove(self,opponentMoves) -> bool:
		if len(opponentMoves)==0: #for first move always cooperate to show good will
			return baseBot.cooperate
		# store move for efficient calculation
		if opponentMoves[-1] == baseBot.cooperate:
			self.opponentCooperate += 1
		else:
			self.opponentDefect +=1
		# calculate if it should defect
		if self.opponentCooperate >= self.opponentDefect:
			return baseBot.cooperate
		return baseBot.defect
	