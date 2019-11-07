# Abdullah Arif
# COMP-3710 Final project Prisoner Dilemma simulator
# the prober is a bot who plays dcc  then if the other opponent did not try to punish it it will defect forever other wise it plays as a tit-for-tat bot

from botBase import baseBot
class proberBot(baseBot):
	def __init__(self):
		# bot inherits from base class and sets it's name
		super().__init__("prober") 
		

	def getMove(self,opponentMoves) -> bool:
		if(len(opponentMoves)==0):
			return baseBot.defect
		if(len(opponentMoves)<3): # second and third move
			return baseBot.cooperate
		# if it self or opponent reacted then tit for tat 
		if((opponentMoves[0] == baseBot.defect and opponentMoves[1] ==baseBot.cooperate and
		opponentMoves[2] ==baseBot.cooperate ) or
		(opponentMoves[1] == baseBot.defect or opponentMoves[2] == baseBot.defect)):
			return opponentMoves[-1]
		#if opponent cooperated on turn 2 and 3
		return baseBot.defect 

