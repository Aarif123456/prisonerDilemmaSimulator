# Abdullah Arif
# COMP-3710 Final project Prisoner Dilemma simulator
# main file that holds the AI tournament
# import all the bots
from basicBot import basicBot
from titForTatBot import titForTatBot
from grudgerBot import grudgerBot
from randomBot import randomBot
from softThinkerBot import softThinkerBot
from hardThinkerBot import hardThinkerBot
from periodicBot import periodicBot
from pavlov import pavlovBot
# ** future add min and max range for rounds and add reproductive points
class tournament:
	cooperate = True
	defect = False
	# holds all strategies currently available in game
	strategyList=[]
	strategies =["always cooperate","always defect", "tit-for-tat", "grudger","choose randomly",
	"soft thinker","hard thinker", "Cyclical DDC","Cyclical CCD","Cyclical CD",
	"mean tit-for-tat", "pavlov", "cooperative tit-for-tat", "hard tit-for-tat", "slow-tit-for-tat"
	, "gradual", "prober", "probability (set your own probability)"]
	def __init__(self, rounds):		
		self.numRounds =rounds		
		# list of bots competing
		self.botList =[]

	@staticmethod
	def printStrategyMenu(self):
		for i in range(len(self.strategies)):
			print(str(i+1) +": "+ self.strategies[i] +"\n")

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
			return softThinkerBot()
		if botNum == 7:
			return hardThinkerBot()
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
	# create round for the tournament
	def setUp(self):
		print("Welcome to the strategy choosing Menu.\n")
		test ={1,2,3,4,5,6,7,8,9,10,11,12,-1}
		testNum = [1,1,5,0,0,10,0,0,0,0,0,5]
		while(True):
			tournament.printStrategyMenu(self)
			# pick the strategy you want to enroll
			# botNum= int(input("Please the number associated with the strategy that you wish to enter in the tournament or -1 to leave the choosing menu\n"))
			botNum =test.pop()
			if(botNum <=-1 or botNum>len(self.strategies)):
				break
			# choose how many bots using the chosen strategies should be enrolled in the tournament
			# numOfBots = int(input("How many bots do you want to enter that play with the "+self.strategies[botNum-1]+" strategy?\n"))
			numOfBots = testNum[botNum-1]
			for i in range(numOfBots):
				bot = tournament.getBot(botNum) #get the using that strategy
				self.botList.append(bot)

	def faceOff(self):
		for i in range(len(self.botList)):
			for j in range(len(self.botList)):
				# list of bot moves for bots that need memory
				bot1Moves =[]
				bot2Moves =[]
				if(i==j):
					continue
				strategy1 = self.botList[i]
				strategy2 = self.botList[j]
				# for strategies that change variables during the round reset them
				strategy1.newRound()
				strategy2.newRound()
				for r in range(self.numRounds):
					move1 = strategy1.getMove(bot2Moves)
					move2 = strategy2.getMove(bot1Moves)
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
		print("")

	def displayResult(self):
		self.sortBot()
		for bot in self.botList:
			print(bot.getName()+" spent " + bot.getYears() + " in prison\n")

mainTournament = tournament(10)
mainTournament.setUp()
mainTournament.faceOff()
mainTournament.displayResult()


