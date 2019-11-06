#Abdullah Arif
#COMP-3710 Final project Prisoner Dilemma simulator
#base class for the bots so that they have some code in common
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