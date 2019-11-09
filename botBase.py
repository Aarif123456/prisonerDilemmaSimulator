#Abdullah Arif
#COMP-3710 Final project Prisoner Dilemma simulator
#base class for the bots so that they have some code in common
# copy to make kids
import copy
class baseBot:
	cooperate = True
	defect = False
	def __init__(self,sName):
		self.years=0
		self.strategyName = sName

	def addYears(self, y : int):
		self.years += y

	def getYears(self) -> str:
		return str(self.years)

	def getName(self) -> str:
		return self.strategyName

	def newRound(self):
		pass

	def getMove(self,opponentMoves) -> bool: 
		pass

	# for kid class reset any variables that may have changed during the round
	def reset(self):
		self.years = 0


	def getChild(self):
		kid = copy.deepcopy(self)
		kid.reset()
		return kid