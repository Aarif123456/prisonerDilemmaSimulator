# Abdullah Arif
# COMP-3710 Final project Prisoner Dilemma simulator
# main file that holds the AI tournament
# import all the bots
from basicBot import basicBot
from titForTatBot import *
from grudgerBot import *
from randomBot import randomBot
from majority import *
from periodicBot import periodicBot
from pavlov import pavlovBot
from gradual import gradualBot
from prober import proberBot
from deterministic import *

# import random to add in noise
import random
# math for calculating mean and standard deviation
import math
class tournament:
	cooperate = True
	defect = False
	# holds all strategies currently available in game
	strategyList=[]
	strategies =["always cooperate","always defect", "tit-for-tat", "grudger","choose randomly",
	"soft majority","hard majority", "Cyclical DDC","Cyclical CCD","Cyclical CD",
	"mean tit-for-tat", "pavlov", "cooperative tit-for-tat", "hard tit-for-tat", "slow tit-for-tat"
	, "gradual", "prober", "sneaky tit-for-tat","forgetful grudger","forgiving tit for tat", 
	 "generous tit-for-tat", "probability (set your own probability)"]
	#    OppositeGrudger, -cooperate if the opponent has ever cooperated
	#    ForgetfulGrudger, -grudger but forgets after a set amount of time 

	# "appeaser" - starts cooperating and switches every time opponent defects
	# "randomly defect", randomly cooperate
	# tricky defect - if opponent has cooperated in the last 10 turns and has defected in the last 3 turns
	# tricky cooperate - if opponent has cooperated in the last 3 turn and has never defected
	
	

	# since random is just a variation on probability will probably remove the class and set as probability bot with a 50/50 chance 

	# add evolution, interactive, add signal error
	# ** future add min and max range for rounds and add reproductive points with genetic 
	# forgiving tit-for-tat -> better in noise but more vulnerable
	def __init__(self, rounds:int):		
		self.numRounds =rounds		
		# list of bots competing
		self.botList =[]
		self.noise = 0.0

	@staticmethod
	def printStrategyMenu():
		for i in range(len(tournament.strategies)):
			print(str(i+1) +": "+ tournament.strategies[i] +"\n")

	@staticmethod
	def getBot(botNum : int):
		if botNum == 1:
			return basicBot("always cooperate", tournament.cooperate)
		if botNum == 2:
			return basicBot("always defect", tournament.defect)
		if botNum == 3:
			return titForTatBot("tit-for-tat", tournament.cooperate)
		if botNum == 4:
			return grudgerBot()
		if botNum == 5:
			return randomBot()
		if botNum == 6:
			return softMajorityBot()
		if botNum == 7:
			return hardMajorityBot()
		if botNum == 8:
			return periodicBot("Cyclical DDC", [tournament.defect, tournament.defect, tournament.cooperate])
		if botNum == 9:
			return periodicBot("Cyclical CCD",[tournament.cooperate,tournament.cooperate, tournament.defect])
		if botNum == 10:
			return periodicBot("Cyclical CD",[tournament.cooperate, tournament.defect])
		if botNum == 11:
			return  titForTatBot("mean tit-for-tat", tournament.defect)
		if botNum == 12:
			return pavlovBot()
		if botNum == 13:
			return cooperativeTitForTatBot()
		if botNum == 14:
			return hardTitForTatBot()
		if botNum == 15:
			return slowTitForTatBot()
		if botNum == 16:
			return gradualBot()
		if botNum == 17:
			return proberBot()
		if botNum == 18:
			return sneakyTitForTatBot()
		if botNum == 19:
			return forgetfulGrudgerBot(10) # 10 rounds to forget by default
		if botNum == 20:
			return forgivingTitForTatBot(0.1) #set to 10% by default
		if botNum == 21:
			return generousTitForTatBot(0.05) #set to random forgiveness to 5%
		if(botNum !=-1): # if not a valid choice and not -1 raise
			raise Exception('Invalid choice ')


	# create round for the tournament
	def setNoise(self, n:float):
		self.noise =n
	def setUp(self):
		print("Welcome to the strategy choosing Menu.\n")
		# uncomment to test
		# test =    {1, 2, 3, 4, 5, 6, 7,8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18,-1}
		# testNum = [5,5,5,10,10,10,10,10,10,10,10, 10, 10, 10, 10, 10, 10, 10]
		while(True):
			tournament.printStrategyMenu()
			# pick the strategy you want to enroll
			botNum= int(input("Please the number associated with the strategy that you wish to enter in the tournament or -1 to leave the choosing menu\n"))
			# botNum =test.pop() # for quick testing
			if(botNum <=-1 or botNum>len(tournament.strategies)):
				break
			# choose how many bots using the chosen strategies should be enrolled in the tournament
			numOfBots = int(input("How many bots do you want to enter that play with the "+tournament.strategies[botNum-1]+" strategy?\n"))
			# numOfBots = testNum[botNum-1] # for quick testing
			for i in range(numOfBots):
				bot = tournament.getBot(botNum) #get the using that strategy
				self.botList.append(bot)
	def humanPlay(self):
		print("Welcome to the strategy choosing Menu.\n")
		tournament.printStrategyMenu()
		botNum= int(input("Please choose your opponent strategy\n"))
		if(botNum <=-1 or botNum>len(tournament.strategies)):
			print("Invalid strategy... Now exiting")
			return
		bot = tournament.getBot(botNum)
		humanMoves =[]
		humanYears =0
		for r in range(self.numRounds):
			humanMove = int(input("Please pick your move 1.Cooperate 2.Betray"))
			if(humanMove ==1):
				move1 = tournament.cooperate
			else:
				move1 = tournament.defect
			move2 = bot.getMove(humanMoves)
			humanMoves.append(move1)

			#both cooperate they both go to jail for 2 years
			if( move1 == tournament.cooperate and move2 == tournament.cooperate): 
				print("You both cooperated you get to go to jail for 2 years!")
				humanYears+= 2
				bot.addYears(2)

			#both defect they both go to jail for 5 years
			if( move1 == tournament.defect and move2 == tournament.defect): 
				print("You both betrayed each other you get to go to jail for 5 years...")
				humanYears+= 5
				bot.addYears(5)

			# if bot1 cooperates and bot 2 defects then bot1 
			# goes to jail for 10 years while bot 2 gets to walk
			if( move1 == tournament.cooperate and move2 == tournament.defect): 
				print("You got betrayed... You got sent to jail for 10 years while the bot walked free :(")
				humanYears+= 10
				bot.addYears(0)
			# same as third scenario in reverse
			if( move1 == tournament.defect and move2 == tournament.cooperate): 
				print("Your plan worked! You get to walk free and the bot got 10 years in prison O.O")
				humanYears+= 0
				bot.addYears(10)
		print("At the end of the you got " + str(humanYears) + " years in jail and the bot got "+bot.getYears() + " years")

	def faceOff(self):
		for i in range(len(self.botList)):
			for j in range(i+1, len(self.botList)):
				# list of bot moves for bots that need memory
				bot1Moves =[]
				bot2Moves =[]
				strategy1 = self.botList[i]
				strategy2 = self.botList[j]
				# for strategies that change variables during the round reset them
				strategy1.newRound()
				strategy2.newRound()
				for r in range(self.numRounds):
					move1 = strategy1.getMove(bot2Moves)
					move2 = strategy2.getMove(bot1Moves)
					# create noise
					if(random.uniform(0,100) <self.noise):
						if(random.randint(0,1)==0):
							move1 = False
						else:
							move1 = True
					if(random.uniform(0,100) <self.noise):
						if(random.randint(0,1)==0):
							move2 = False
						else:
							move2 = True
					bot1Moves.append(move1)
					bot2Moves.append(move2)
					#both cooperate they both go to jail for 2 years
					if( move1 == tournament.cooperate and move2 == tournament.cooperate): 
						strategy1.addYears(2)
						strategy2.addYears(2)

					#both defect they both go to jail for 5 years
					if( move1 == tournament.defect and move2 == tournament.defect): 
						strategy1.addYears(5)
						strategy2.addYears(5)

					# if bot1 cooperates and bot 2 defects then bot1 
					# goes to jail for 10 years while bot 2 gets to walk
					if( move1 == tournament.cooperate and move2 == tournament.defect): 
						strategy1.addYears(10)
						strategy2.addYears(0)
					# same as third scenario in reverse
					if( move1 == tournament.defect and move2 == tournament.cooperate): 
						strategy1.addYears(0)
						strategy2.addYears(10)
	# ** sort bot from best to worse performing
	def sortBot(self):
		self.botList.sort(key=lambda bot: bot.getYears())

	def geneticAlgorithm(self):
		sumYears = 0
		standardDeviation = 0.00
		variance = 0.00
		mean = 0.00
		if(self.numRounds<1):
			raise Exception("No bots faced off against each other cannot complete genetic algorithm")
			return
		# get mean
		for bot in self.botList:
			y = int(bot.getYears())
			sumYears += y
		mean = sumYears/len(self.botList)
		#get variance
		for bot in self.botList:
			y = int(bot.getYears())
			variance += pow(y-mean,2)			
		variance /= len(self.botList)
		standardDeviation = math.sqrt(variance)		
			
		newBotList = []
		for bot in self.botList:
			y = int(bot.getYears())
			numKid = -round((y - mean)/standardDeviation)
			for i in range(numKid):
				newBotList.append(bot.getChild())
		self.numRounds = 0 
		self.botList = newBotList 

	def displayResult(self):
		self.sortBot()
		for bot in self.botList:
			print(bot.getName()+" spent " + bot.getYears() + " in prison\n")

mainTournament = tournament(10)
mainTournament.setUp()
mainTournament.faceOff()
# mainTournament.humanPlay()
mainTournament.displayResult()
print("running a genetic algorithms round")
mainTournament.geneticAlgorithm()
mainTournament.displayResult()


