# What's Left
# Create sliders (and spinboxes if applicable) for remaining strategies (see TODOs in getSliderValue function)
#              For this: use custom widget strategySlider(master=right, label="[strategy title]")
#              See "Forgetful Grudger" for spinbox example
# Display Results
#       Number of years served is the same for each bot using the same strategy, so just display average years per bot per strategy (i.e. what one bot using each strategy served)?
# Info boxes or hover text for strategy information?
# (Sam can help with things if needed once we decide what to do)
# Note: Need python 3.8 to import Tkinter


# Abdullah Arif
# COMP-3710 Final project Prisoner Dilemma simulator
# main file that holds the AI tournament
# import all the bots
from tkinter.ttk import Notebook, Panedwindow, Labelframe
from tkinter import Frame
from tkinter import *
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
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np

# import random to add in noise
import random
# math for calculating mean and standard deviation
import math


class tournament:
    cooperate = True
    defect = False
    # holds all strategies currently available in game
    strategyList = []

    # strategies array for text-based GUI only, not needed here

    strategies = ["always cooperate", "always defect", "tit-for-tat", "grudger", "choose randomly",
                  "soft majority", "hard majority", "Cyclical DDC", "Cyclical CCD", "Cyclical CD",
                  "mean tit-for-tat", "pavlov", "cooperative tit-for-tat", "hard tit-for-tat", "slow tit-for-tat", "gradual", "prober", "sneaky tit-for-tat", "forgetful grudger", "forgiving tit for tat",
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
    def __init__(self, rounds: int):
        self.numRounds = rounds
        # list of bots competing
        self.botList = []
        self.noise = 0.0

        # Sam
    def insertBots(botNum: int, numOfBots: int):
        for i in range(numOfBots):
            bot = tournament.getBot(botNum)  # get bot the using that strategy
            self.botList.append(bot)  # add to botlist

    @staticmethod
    def getBot(botNum: int):
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
            return periodicBot("Cyclical CCD", [tournament.cooperate, tournament.cooperate, tournament.defect])
        if botNum == 10:
            return periodicBot("Cyclical CD", [tournament.cooperate, tournament.defect])
        if botNum == 11:
            return titForTatBot("mean tit-for-tat", tournament.defect)
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
            # 10 rounds to forget by default
            return forgetfulGrudgerBot(grudgerForgetMemoryEntry.get())
        if botNum == 20:
            return forgivingTitForTatBot(0.1)  # set to 10% by default
        if botNum == 21:
            # set to random forgiveness to 5%
            return generousTitForTatBot(0.05)
        if (botNum != -1):  # if not a valid choice and not -1 raise
            raise Exception('Invalid choice ')

    @staticmethod  # Sam
    # Get slider values and load bots into tournament
    def getSliderValue(sliderNum: int) -> int:
        if sliderNum == 1:
            return 0  # TODO
        if sliderNum == 2:
            return 0  # TODO
        if sliderNum == 3:
            return tftSlider.get()
        if sliderNum == 4:
            return grudgerSlider.get()
        if sliderNum == 5:
            return 0  # TODO
        if sliderNum == 6:
            return majSoftSlider.get()
        if sliderNum == 7:
            return majHardSlider.get()
        if sliderNum == 8:
            return ddcSlider.get()
        if sliderNum == 9:
            return ccdSlider.get()
        if sliderNum == 10:
            return cdSlider.get()
        if sliderNum == 11:
            return tftMeanSlider.get()
        if sliderNum == 12:
            return pavlovSlider.get()
        if sliderNum == 13:
            return tftCoopSlider.get()
        if sliderNum == 14:
            return tftHardSlider.get()
        if sliderNum == 15:
            return 0  # TODO
        if sliderNum == 16:
            return 0  # TODO
        if sliderNum == 17:
            return 0  # TODO
        if sliderNum == 18:
            return 0  # TODO
        if sliderNum == 19:
            return grudgerForgetSlider.get()
        if sliderNum == 21:
            return 0  # TODO
        if sliderNum == 22:
            return 0  # TODO
        else:
            return 0

    # create round for the tournament
    def setNoise(self, n: float):
        self.noise = n

    def displayResult(self):  # moved here so could be called in runTournament
        self.sortBot()
        
        # dynamically created lists for switch case
        labels = []
        minYears = []
        maxYears = []

        # where each bot will load their corresponding .getYears() into
        alwaysCooperate = []
        alwaysDefect = []
        traditionalTFT = []
        grudgerTraditional = []
        chooseRandomly = []
        softMajority = []
        hardMajority = []
        DDC = []
        CCD = []
        CD = []
        meanTFT = []
        pavlov = []
        cooperativeTFT = []
        hardTFT = []
        slowTFT = []
        gradual = []
        prober = []
        sneakyTFT = []
        grudgerForgetful = []
        generousTFT = []

        for bot in self.botList:
            print(bot.getName() + " spent " + bot.getYears() + " in prison\n")
            if(bot.getName() == tournament.strategies[0]) :
                alwaysCooperate.append(int(bot.getYears()))
                if 'Always Cooperate' not in labels :
                    labels.append('Always Coorperate')

            elif(bot.getName() == tournament.strategies[1]) :
                alwaysDefect.append(int(bot.getYears()))
                if 'Always Defect' not in labels :
                    labels.append('Always Defect')

            elif(bot.getName() == tournament.strategies[2]) :
                traditionalTFT.append(int(bot.getYears()))
                if 'Tit-For-Tat' not in labels :
                    labels.append('Tit-For-Tat')

            elif(bot.getName() == tournament.strategies[3]) :
                grudgerTraditional.append(int(bot.getYears()))
                if 'Traditional Grudger' not in labels :
                    labels.append('Traditional Grudger')

            elif(bot.getName() == tournament.strategies[4]) :
                chooseRandomly.append(int(bot.getYears()))
                if 'Random' not in labels :
                    labels.append('Random')
                       
            elif(bot.getName() == tournament.strategies[5]) :
                softMajority.append(int(bot.getYears()))
                if 'Soft Majority' not in labels :
                    labels.append('Soft Majority')

            elif(bot.getName() == tournament.strategies[6]) :
                hardMajority.append(int(bot.getYears()))
                if 'Hard Majority' not in labels :
                    labels.append('Hard Majority')
            
            elif(bot.getName() == tournament.strategies[7]) :
                DDC.append(int(bot.getYears()))
                if 'DDC' not in labels :
                    labels.append('DDC')

            elif(bot.getName() == tournament.strategies[8]) :
                CCD.append(int(bot.getYears()))
                if 'CCD' not in labels :
                    labels.append('CCD')

            elif(bot.getName() == tournament.strategies[9]) :
                CD.append(int(bot.getYears()))
                if 'CD' not in labels :
                    labels.append('CD')

            elif(bot.getName() == tournament.strategies[10]) :
                meanTFT.append(int(bot.getYears()))
                if 'Mean TFT' not in labels :
                    labels.append('Mean TFT')

            elif(bot.getName() == tournament.strategies[11]) :
                pavlov.append(int(bot.getYears()))
                if 'Pavlov' not in labels :
                    labels.append('Pavlov')

            elif(bot.getName() == tournament.strategies[12]) :
                cooperativeTFT.append(int(bot.getYears()))
                if 'Cooperative TFT' not in labels :
                    labels.append('Cooperative TFT')

            elif(bot.getName() == tournament.strategies[13]) :
                hardTFT.append(int(bot.getYears()))
                if 'Hard TFT' not in labels :
                    labels.append('Hard TFT')

            elif(bot.getName() == tournament.strategies[14]) :
                slowTFT.append(int(bot.getYears()))
                if 'Slow TFT' not in labels :
                    labels.append('Slow TFT')

            elif(bot.getName() == tournament.strategies[15]) :
                gradual.append(int(bot.getYears()))
                if 'Gradual' not in labels :
                    labels.append('Gradual')

            elif(bot.getName() == tournament.strategies[16]) :
                prober.append(int(bot.getYears()))
                if 'Prober' not in labels :
                    labels.append('Prober')

            elif(bot.getName() == tournament.strategies[17]) :
                sneakyTFT.append(int(bot.getYears()))
                if 'Sneaky TFT' not in labels :
                    labels.append('Sneaky TFT')

            elif(bot.getName() == tournament.strategies[18]) :
                grudgerForgetful.append(int(bot.getYears()))
                if 'Forgetful Grudger' not in labels :
                    labels.append('Forgetful Grudger')

            elif(bot.getName() == tournament.strategies[19]) :
                generousTFT.append(int(bot.getYears()))
                if 'Generous TFT' not in labels :
                    labels.append('Generous TFT')

            else :
                print("Not Working")


        # Getting the minimum and maximum years spent in prison for every subset of strategies

        #DO NOT HAVE
        if labels.__contains__("Always Cooperate") :
            minYears.append(min(alwaysCooperate))
            maxYears.append(max(alwaysCooperate))
        #DO NOT HAVE
        if labels.__contains__("Always Defect") :
            minYears.append(min(alwaysDefect))
            maxYears.append(max(alwaysDefect))

        if labels.__contains__("Tit-For-Tat") :
            minYears.append(min(traditionalTFT))
            maxYears.append(max(traditionalTFT))
        
        if labels.__contains__("Traditional Grudger") :
            minYears.append(min(grudgerTraditional))
            maxYears.append(max(grudgerTraditional))
        
        #DO NOT HAVE
        if labels.__contains__("Random") :
            minYears.append(min(chooseRandomly))
            maxYears.append(max(chooseRandomly))
        
        if labels.__contains__("Soft Majority") :
            minYears.append(min(softMajority))
            maxYears.append(max(softMajority))
        
        if labels.__contains__("Hard Majority") :
            minYears.append(min(hardMajority))
            maxYears.append(max(hardMajority))
        
        if labels.__contains__("DDC") :
            minYears.append(min(DDC))
            maxYears.append(max(DDC))
        
        if labels.__contains__("CCD") :
            minYears.append(min(CCD))
            maxYears.append(max(CCD))
        
        if labels.__contains__("CD") :
            minYears.append(min(CD))
            maxYears.append(max(CD))

        if labels.__contains__("Mean TFT") :
            minYears.append(min(meanTFT))
            maxYears.append(max(meanTFT))
        
        if labels.__contains__("Pavlov") :
            minYears.append(min(pavlov))
            maxYears.append(max(pavlov))
        
        if labels.__contains__("Cooperative TFT") :
            minYears.append(min(cooperativeTFT))
            maxYears.append(max(cooperativeTFT))
        
        if labels.__contains__("Hard TFT") :
            minYears.append(min(hardTFT))
            maxYears.append(max(hardTFT))
        
        #DO NOT HAVE
        if labels.__contains__("Slow TFT") :
            minYears.append(min(slowTFT))
            maxYears.append(max(slowTFT))
        
        #DO NOT HAVE
        if labels.__contains__("Gradual") :
            minYears.append(min(gradual))
            maxYears.append(max(gradual))

        #DO NOT HAVE
        if labels.__contains__("Prober") :
            minYears.append(min(prober))
            maxYears.append(max(prober))
        
        #DO NOT HAVE
        if labels.__contains__("Sneaky TFT") :
            minYears.append(min(sneakyTFT))
            maxYears.append(max(sneakyTFT))

        #HAVE - DOESN'T WORK IN GUI
        if labels.__contains__("Forgetful Grudger") :
            minYears.append(min(grudgerForgetful))
            maxYears.append(max(grudgerForgetful))
        
        #DO NOT HAVE
        if labels.__contains__("Generous TFT") :
            minYears.append(min(generousTFT))
            maxYears.append(max(generousTFT))



        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, minYears, width, label='Min Years')
        rects2 = ax.bar(x + width/2, maxYears, width, label='Max Years')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('# of Years')
        ax.set_title('Prisoner Dilemma Observations')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()

        def autolabel(rects):
            """Attach a text label above each bar in *rects*, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                print("This is the height = " + str(height))
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)

        fig.tight_layout()

        plt.show()

    def setUp(self):  # Sam: Run Simulation button runs this function!

        i = 1
        for i in range(1, 21):
            # print(self.getSliderValue(i)) # for testing
            numOfBots = int(self.getSliderValue(i))

            if numOfBots == 0:
                pass

            else:
                j = 1
                for j in range(1, numOfBots + 1):
                    bot = tournament.getBot(i)  # get the using that strategy
                    self.botList.append(bot)

    def humanPlay(self):
        print("Welcome to the strategy choosing Menu.\n")
        tournament.printStrategyMenu()
        botNum = int(input("Please choose your opponent strategy\n"))
        if (botNum <= -1 or botNum > len(tournament.strategies)):
            print("Invalid strategy... Now exiting")
            return
        bot = tournament.getBot(botNum)
        humanMoves = []
        humanYears = 0
        for r in range(self.numRounds):
            humanMove = int(
                input("Please pick your move 1.Cooperate 2.Betray"))
            if (humanMove == 1):
                move1 = tournament.cooperate
            else:
                move1 = tournament.defect
            move2 = bot.getMove(humanMoves)
            humanMoves.append(move1)

            # both cooperate they both go to jail for 2 years
            if (move1 == tournament.cooperate and move2 == tournament.cooperate):
                print("You both cooperated you get to go to jail for 2 years!")
                humanYears += 2
                bot.addYears(2)

            # both defect they both go to jail for 5 years
            if (move1 == tournament.defect and move2 == tournament.defect):
                print(
                    "You both betrayed each other you get to go to jail for 5 years...")
                humanYears += 5
                bot.addYears(5)

            # if bot1 cooperates and bot 2 defects then bot1
            # goes to jail for 10 years while bot 2 gets to walk
            if (move1 == tournament.cooperate and move2 == tournament.defect):
                print(
                    "You got betrayed... You got sent to jail for 10 years while the bot walked free :(")
                humanYears += 10
                bot.addYears(0)
            # same as third scenario in reverse
            if (move1 == tournament.defect and move2 == tournament.cooperate):
                print(
                    "Your plan worked! You get to walk free and the bot got 10 years in prison O.O")
                humanYears += 0
                bot.addYears(10)
        print("At the end of the you got " + str(
            humanYears) + " years in jail and the bot got " + bot.getYears() + " years")

    def faceOff(self):
        for i in range(len(self.botList)):
            for j in range(i + 1, len(self.botList)):
                # list of bot moves for bots that need memory
                bot1Moves = []
                bot2Moves = []
                strategy1 = self.botList[i]
                strategy2 = self.botList[j]
                # for strategies that change variables during the round reset them
                strategy1.newRound()
                strategy2.newRound()
                for r in range(self.numRounds):
                    move1 = strategy1.getMove(bot2Moves)
                    move2 = strategy2.getMove(bot1Moves)
                    # create noise
                    if (random.uniform(0, 100) < self.noise):
                        if (random.randint(0, 1) == 0):
                            move1 = False
                        else:
                            move1 = True
                    if (random.uniform(0, 100) < self.noise):
                        if (random.randint(0, 1) == 0):
                            move2 = False
                        else:
                            move2 = True
                    bot1Moves.append(move1)
                    bot2Moves.append(move2)
                    # both cooperate they both go to jail for 2 years
                    if (move1 == tournament.cooperate and move2 == tournament.cooperate):
                        strategy1.addYears(2)
                        strategy2.addYears(2)

                    # both defect they both go to jail for 5 years
                    if (move1 == tournament.defect and move2 == tournament.defect):
                        strategy1.addYears(5)
                        strategy2.addYears(5)

                    # if bot1 cooperates and bot 2 defects then bot1
                    # goes to jail for 10 years while bot 2 gets to walk
                    if (move1 == tournament.cooperate and move2 == tournament.defect):
                        strategy1.addYears(10)
                        strategy2.addYears(0)
                    # same as third scenario in reverse
                    if (move1 == tournament.defect and move2 == tournament.cooperate):
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
        if (self.numRounds < 1):
            raise Exception(
                "No bots faced off against each other cannot complete genetic algorithm")
            return
        # get mean
        for bot in self.botList:
            y = int(bot.getYears())
            sumYears += y
        mean = sumYears / len(self.botList)
        # get variance
        for bot in self.botList:
            y = int(bot.getYears())
            variance += pow(y - mean, 2)
        variance /= len(self.botList)
        standardDeviation = math.sqrt(variance)

        newBotList = []
        for bot in self.botList:
            y = int(bot.getYears())
            numKid = -round((y - mean) / standardDeviation)
            for i in range(numKid):
                newBotList.append(bot.getChild())
        self.numRounds = 0
        self.botList = newBotList

    @staticmethod
    def runTournament():
        print(tftSlider.get())
        mainTournament = tournament(int(roundsEntry.get()))
        mainTournament.setUp()
        mainTournament.faceOff()
        mainTournament.displayResult()


# Samantha Robson
# COMP 3710 Final AI Project
# Prisoner's Dilemma Simulator GUI


# import matplotlib        #use for displaying graphs?
# matplotlib.use("TkAgg")

notebookWidth = 225


class strategySlider(Scale):
    def __init__(self, **kwargs):
        Scale.__init__(self, orient=HORIZONTAL, length=170, **kwargs)
        self.pack()


class infoButton(Button):
    def __init__(self, **kwargs):
        Button.__init__(self, text="Info", **kwargs)
        self.pack()


root = Tk()
left = Frame(root)
left.pack(side=LEFT)
right = Frame(root)
right.pack(side=RIGHT)  # TODO Pack other half of widgets here!
root.title("Prisoner\'s Dilemma Simulator")


def info_window(str):
    window = Toplevel(root)
    label = Label(window, text=str)
    label.pack()
    return


theLabel = Label(left, text="Tit-For-Tat")
theLabel.pack()

tft = Notebook(left, width=notebookWidth)
tft.pack()
tftTrad = Frame(tft)
tftMean = Frame(tft)
tftCoop = Frame(tft)
tftHard = Frame(tft)

tft.add(tftTrad, text='Traditional')
tft.add(tftMean, text='Mean')
tft.add(tftCoop, text='Cooperative')
tft.add(tftHard, text='Hard')

tftSlider = strategySlider(master=tftTrad, label="Traditional")
tftSlider.pack()

tftMeanSlider = strategySlider(master=tftMean, label="Mean")
tftMeanSlider.pack()

tftCoopSlider = strategySlider(master=tftCoop, label="Cooperative")
tftCoopSlider.pack()

tftHardSlider = strategySlider(master=tftHard, label="Hard")
tftHardSlider.pack()

# Periodic Interface

periodicLabel = Label(left, text="Periodic")
periodicLabel.pack()

periodic = Notebook(left, width=notebookWidth)
periodic.pack()
periodicDDC = Frame(periodic)
periodicCCD = Frame(periodic)
periodicCD = Frame(periodic)

periodic.add(periodicDDC, text='DDC')
periodic.add(periodicCCD, text='CCD')
periodic.add(periodicCD, text='CD')

ddcSlider = strategySlider(master=periodicDDC, label='Defect Defect Cooperate')
ddcSlider.pack()

ccdSlider = strategySlider(
    master=periodicCCD, label='Cooperate Cooperate Defect')
ccdSlider.pack()

cdSlider = strategySlider(master=periodicCD, label='Cooperate Defect')
cdSlider.pack()

# Majority Bots

majorityLabel = Label(left, text="Majority")
majorityLabel.pack()

majority = Notebook(left, width=notebookWidth)
majority.pack()
majForget = Frame(majority)
majHard = Frame(majority)
majSoft = Frame(majority)

majority.add(majHard, text='Hard')
majority.add(majSoft, text='Soft')

majHardSlider = strategySlider(master=majHard, label='Hard')
majHardSlider.pack()

majSoftSlider = strategySlider(master=majSoft, label='Soft')
majSoftSlider.pack()

# Pavlov Interface

pavlovLabel = LabelFrame(left, text="Pavlov", width=notebookWidth)
pavlovLabel.pack()

pavlovSlider = strategySlider(master=pavlovLabel, label='Pavlov')
pavlovSlider.pack()

pavInfoButton = infoButton(master=pavlovLabel, command=lambda: info_window(
    "Pavlov\n\n    This strategy plays DCC, then switches to a Tit-For-Tat style    \n"))
pavInfoButton.pack()

# Grudger Interface

grudgerLabel = Label(left, text="Grudger")
grudgerLabel.pack()

grudger = Notebook(left, width=notebookWidth)
grudger.pack()
grudgerTrad = Frame(grudger)
grudgerForget = Frame(grudger)

grudger.add(grudgerTrad, text="Traditional")
grudger.add(grudgerForget, text="Forgetful")

grudgerSlider = strategySlider(master=grudgerTrad, label='Grudger')
grudgerSlider.pack()

# Forgetful Grudger

grudgerForgetSlider = strategySlider(
    master=grudgerForget, label='Forgetful Grudger')
grudgerForgetSlider.pack()

# Forgetful memory

forgetMemoryLabel = Label(grudgerForget, text="Previous Rounds Remembered")
forgetMemoryLabel.pack()
grudgerForgetMemoryEntry = Spinbox(grudgerForget, from_=0, to=100, width=4)
# TODO Connect to memory value
grudgerForgetMemoryEntry.pack()

theLabel = Label(
    root, text="This is where graphs of \n the bots prison years accumulated \n will be displayed")
theLabel.pack(anchor=CENTER)
# Run Simulation Button

roundsLabel = Label(root, text="Rounds to Play (Max 1000):")
roundsLabel.pack()
roundsEntry = Spinbox(root, from_=1, to=1000, width=4)
roundsEntry.pack()

runButton = Button(root, text="Run Simulation",
                   command=lambda: tournament.runTournament())  # add command
runButton.pack()


root.mainloop()
# to keep GUI window open
