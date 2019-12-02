# COMP-3710 Final project Prisoner Dilemma simulator
# it can start off as either cooperating and defecting depending on the arguments
# afterwards it will mirror the opponent
from botBase import baseBot
import random
class titForTatBot(baseBot):
	def __init__(self, name, sM):
		# bot inherits from base class and sets it's name
		super().__init__(name) 
		self.startingMove = sM

	def getMove(self,opponentMoves) -> bool:
		if(len(opponentMoves)==0): #for first move return 
			return self.startingMove
		# otherwise mirror
		return opponentMoves[-1]

#bot that acts like tit-for -tat but gives an extra chance to forgive also called tit for 2 tats
class cooperativeTitForTatBot(baseBot):
	def __init__(self):
		# bot inherits from base class and sets it's name
		super().__init__("cooperative tit-for-tat") 

	def getMove(self,opponentMoves) -> bool:
		if(len(opponentMoves)<2): #for first move return 
			return baseBot.cooperate
		if(opponentMoves[-1] == baseBot.defect and opponentMoves[-2] == baseBot.defect ):
			return baseBot.defect
		return baseBot.cooperate

#at starts gives two chances then it will punish if either of the last two move were defects
class hardTitForTatBot(baseBot):
	def __init__(self):
		# bot inherits from base class and sets it's name
		super().__init__("hard tit-for-tat") 

	def getMove(self,opponentMoves) -> bool:
		if(len(opponentMoves)<2): #for first move return 
			return baseBot.cooperate
		if(opponentMoves[-1] == baseBot.defect or opponentMoves[-2] == baseBot.defect ):
			return baseBot.defect
		return baseBot.cooperate

#slow tit for tat starts of cooperating and defects if last two moves were defects then it needs to cooperates to make it calm down
class slowTitForTatBot(baseBot):
	def __init__(self):
		# bot inherits from base class and sets it's name
		super().__init__("slow tit-for-tat") 
		self.niceMode = True

	def getMove(self,opponentMoves) -> bool:
		if(len(opponentMoves)>1): #for first move return 
			if(self.niceMode and opponentMoves[-1] == baseBot.defect 
				and opponentMoves[-2] == baseBot.defect):
				self.niceMode =False
			if (not self.niceMode and opponentMoves[-1] == baseBot.cooperate 
				and opponentMoves[-2] == baseBot.cooperate ):
				self.niceMode=True
		return self.niceMode
	# make sure bot always starts off as nice
	def newRound(self):
		self.niceMode = True

# sneaky tit-for-tat acts like tit for tat but will try to get away with some cheating it it can
class sneakyTitForTatBot(baseBot):
	def __init__(self):
		# bot inherits from base class and sets it's name
		super().__init__("sneaky tit-for-tat") 
		self.tricked = False
		self.trickRound = random.randint(0,3)

	def getMove(self,opponentMoves) -> bool:
		# try trick
		if(len(opponentMoves)==self.trickRound):
			self.tricked = True
			return baseBot.defect
		if(self.tricked):
			# if trick was retaliated then fall back and apologize
			if(opponentMoves[-1] == baseBot.defect):
				self.trick = False
				return baseBot.cooperate
			# otherwise exploit
			return baseBot.defect
		else: # if not tricking then play as tit for tat
			# basic first round
			if(len(opponentMoves)==0): #for first move return 
				return baseBot.cooperate
			else:
				return opponentMoves[-1]

	# reset bot so it can try to trick again
	def newRound(self):
		self.tricked = False
		self.trickRound = random.randint(0,5)

# forgiving tit for tat is a bot that will play tit-for-tat toward anyone who 
# has defected more than set probability(10% by default) of the time otherwise it just cooperates
# can play with what percentage is best
class forgivingTitForTatBot(baseBot):
	def __init__(self, p:float):
		# bot inherits from base class and sets it's name
		super().__init__("forgiving tit-for-tat") 
		self.opponentDefect = 0
		self.probability =p
	def getMove(self,opponentMoves) -> bool:
		if(len(opponentMoves)==0): #for first move return 
			return baseBot.cooperate
		if opponentMoves[-1] == baseBot.defect:
			self.opponentDefect += 1
		# more than set probability mirror
		if self.opponentDefect/len(opponentMoves) >= self.probability:
			return opponentMoves[-1] 
		return baseBot.cooperate

	def newRound(self):
		self.opponentDefect = 0

# generous plays tit-for tat except for a small probability that it randomly forgive by default a 5% chance
class generousTitForTatBot(baseBot):
	def __init__(self, p:float):
		# bot inherits from base class and sets it's name
		super().__init__("generous tit-for-tat") 
		self.probability =p

	def getMove(self,opponentMoves) -> bool:
		if(len(opponentMoves)==0): #for first move return 
			return baseBot.cooperate
		if opponentMoves[-1] == baseBot.defect and random.uniform(0,100)<self.probability:
			return baseBot.cooperate
		return opponentMoves[-1] 

