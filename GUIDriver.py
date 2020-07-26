"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


import random
import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from AlphaBetaPruning import alphabeta
from CheckWinUtil import noToCoord, coordToNo
from MiniMax import minimax
from State import State
from SuccessorFunction import possibleClicks
from TerminalTest import terminalTest
from UtilityValue import utilityValue

globalState = State([],[])

class GUIDriver(QMainWindow):

    gameType = None

    def __init__(self):
        super(GUIDriver,self).__init__()
        self.setGeometry(30,30,1220,750)
        self.setWindowTitle("AI Assignment 3")
        self.initGUI()

    def initGUI(self):
        self.baseLineLabel = QtWidgets.QLabel(self)
        self.baseLineLabel.setText("Base Line")
        self.baseLineLabel.move(140, 5)

        self.b = []
        #row1
        self.b.append(QtWidgets.QPushButton(self))
        self.b[0].resize(75,75)
        self.b[0].move(40,40)
        self.b[0].clicked.connect(self.b1clicked)

        self.b.append(QtWidgets.QPushButton(self))
        self.b[1].resize(75, 75)
        self.b[1].move(104, 40)
        self.b[1].clicked.connect(self.b2clicked)

        self.b.append(QtWidgets.QPushButton(self))
        self.b[2].resize(75, 75)
        self.b[2].move(168, 40)
        self.b[2].clicked.connect(self.b3clicked)

        self.b.append(QtWidgets.QPushButton(self))
        self.b[3].resize(75, 75)
        self.b[3].move(232, 40)
        self.b[3].clicked.connect(self.b4clicked)

        # row2
        self.b.append(QtWidgets.QPushButton(self))
        self.b[4].resize(75, 75)
        self.b[4].move(40, 108)
        self.b[4].clicked.connect(self.b5clicked)

        self.b.append(QtWidgets.QPushButton(self))
        self.b[5].resize(75, 75)
        self.b[5].move(104, 108)
        self.b[5].clicked.connect(self.b6clicked)

        self.b.append(QtWidgets.QPushButton(self))
        self.b[6].resize(75, 75)
        self.b[6].move(168, 108)
        self.b[6].clicked.connect(self.b7clicked)

        self.b.append(QtWidgets.QPushButton(self))
        self.b[7].resize(75, 75)
        self.b[7].move(232, 108)
        self.b[7].clicked.connect(self.b8clicked)

        # row3
        self.b.append(QtWidgets.QPushButton(self))
        self.b[8].resize(75, 75)
        self.b[8].move(40, 176)
        self.b[8].clicked.connect(self.b9clicked)

        self.b.append(QtWidgets.QPushButton(self))
        self.b[9].resize(75, 75)
        self.b[9].move(104, 176)
        self.b[9].clicked.connect(self.b10clicked)

        self.b.append(QtWidgets.QPushButton(self))
        self.b[10].resize(75, 75)
        self.b[10].move(168, 176)
        self.b[10].clicked.connect(self.b11clicked)

        self.b.append(QtWidgets.QPushButton(self))
        self.b[11].resize(75, 75)
        self.b[11].move(232, 176)
        self.b[11].clicked.connect(self.b12clicked)

        # row4
        self.b.append(QtWidgets.QPushButton(self))
        self.b[12].resize(75, 75)
        self.b[12].move(40, 244)
        self.b[12].clicked.connect(self.b13clicked)

        self.b.append(QtWidgets.QPushButton(self))
        self.b[13].resize(75, 75)
        self.b[13].move(104, 244)
        self.b[13].clicked.connect(self.b14clicked)

        self.b.append(QtWidgets.QPushButton(self))
        self.b[14].resize(75, 75)
        self.b[14].move(168, 244)
        self.b[14].clicked.connect(self.b15clicked)

        self.b.append(QtWidgets.QPushButton(self))
        self.b[15].resize(75, 75)
        self.b[15].move(232, 244)
        self.b[15].clicked.connect(self.b16clicked)

        for i in range(16):
            self.b[i].setEnabled(False)

        #minimax button
        self.minimaxB = QtWidgets.QPushButton(self)
        self.minimaxB.resize(120, 30)
        self.minimaxB.move(50, 410)
        self.minimaxB.setText("Play MiniMax")
        self.minimaxB.clicked.connect(self.minimaxBclicked)

        #alphabeta button
        self.alphabetaB = QtWidgets.QPushButton(self)
        self.alphabetaB.resize(120, 30)
        self.alphabetaB.move(205, 410)
        self.alphabetaB.setText("Play Alpha Beta")
        self.alphabetaB.clicked.connect(self.alphabetaBclicked)

        # restart button
        self.restartB = QtWidgets.QPushButton(self)
        self.restartB.resize(120, 30)
        self.restartB.move(50, 480)
        self.restartB.setText("Reset All")
        self.restartB.clicked.connect(self.restartBclicked)

        # exit button
        self.exitB = QtWidgets.QPushButton(self)
        self.exitB.resize(120, 30)
        self.exitB.move(205, 480)
        self.exitB.setText("Exit")
        self.exitB.clicked.connect(self.exitBclicked)


        #12 alalysis label
        self.r1L = QtWidgets.QLabel(self)
        self.r1L.setText("R1 -> No of nodes till end of one random game (minimax):  7249993")
        self.r1L.move(400,10)
        self.r1L.adjustSize()

        self.r2L = QtWidgets.QLabel(self)
        self.r2L.setText("R2 -> Memory allocated to one node:  32 bits")
        self.r2L.move(400,50)
        self.r2L.adjustSize()

        self.r3L = QtWidgets.QLabel(self)
        self.r3L.setText("R3 -> Maximum Length of implicit stack generated:  16")
        self.r3L.move(400,90)
        self.r3L.adjustSize()

        self.r4L = QtWidgets.QLabel(self)
        self.r4L.setText("R4 -> Total time to play one random game (minimax):  724 sec")
        self.r4L.move(400,130)
        self.r4L.adjustSize()

        self.r5L = QtWidgets.QLabel(self)
        self.r5L.setText("R5 -> Nodes created in one micro second (minimax):  9")
        self.r5L.move(400,170)
        self.r5L.adjustSize()

        self.r6L = QtWidgets.QLabel(self)
        self.r6L.setText("R6 -> No of nodes till end of one random gamev(alpha-beta pruning):  10291")
        self.r6L.move(400,210)
        self.r6L.adjustSize()

        self.r7L = QtWidgets.QLabel(self)
        self.r7L.setText("R7 -> (R1 - R6)/R1:  0.9985")
        self.r7L.move(400,250)
        self.r7L.adjustSize()

        self.r8L = QtWidgets.QLabel(self)
        self.r8L.setText("R8 -> Total time to play one random game (alpha-beta pruning):  113 sec")
        self.r8L.move(400,290)
        self.r8L.adjustSize()

        self.r9L = QtWidgets.QLabel(self)
        self.r9L.setText("R9 -> Maximum memory used in both technique is same = max. Stack size * memory of one node = 16*32 = 512 bits")
        self.r9L.move(400,330)
        self.r9L.adjustSize()

        self.r10L = QtWidgets.QLabel(self)
        self.r10L.setText("R10 -> 10 rounds: minimax av. time = 648 sec | alpha-beta av. time = 100 sec")
        self.r10L.move(400,370)
        self.r10L.adjustSize()

        self.r11L = QtWidgets.QLabel(self)
        self.r11L.setText("R11 -> 10 rounds: Player M wins 9 out of 10 times atleast, using both the techniques")
        self.r11L.move(400,410)
        self.r11L.adjustSize()

        self.r12L = QtWidgets.QLabel(self)
        self.r12L.setText("R12 -> 10 rounds 20 times: av. win for M in both techniques = 9.9 approx")
        self.r12L.move(400,450)
        self.r12L.adjustSize()

        self.r13L = QtWidgets.QLabel(self)
        self.r13L.setText("Comparing R4 and R8 -> :  It takes machine 84% less time to compute a move using alpha-beta than MiniMax Algorithm")
        self.r13L.move(400,490)
        self.r13L.adjustSize()

        #instruction label
        self.instL = QtWidgets.QLabel(self)
        self.instL.setText("******************************INSTRUCTIONS******************************\nClick on any of the two buttons – Play minimax/ Play alphabeta. Machine will move first and his move will be visible after its computation. \nNow after machine has moved, the buttons will be enabled for click, click on the desired button according to rules \n(if clicked on coordinate not according to rule, it’ll issue a message to click on correct possible coordinates).\n--> WIN or DRAW status will be updated on box just below game board.\n\nPlease wait for a while after clicking on a button in your turn for machine to compute his strategy.\n--> In case of MiniMax Algo, the very first move by machine will take around 8-10 minutes to compute, next move by machine will take around 1 min and subsequent move will take less than 30 seconds\n--> In case of Alpha-Beta pruning all moves by machine take less than 20 seconds to compute\n       (Please check console for some outputs after only during the first move of Machine under computation for both techniques) \n--> Once any one technique is clicked, game will run using that technique (other button will be disabled), to change it press reset button and then press desired game technique.")
        self.instL.move(10, 550)
        self.instL.adjustSize()

        #win label
        self.winL = QtWidgets.QLabel(self)
        self.winL.setText("Machine will move FIRST!!!")
        self.winL.move(20,359)
        self.winL.adjustSize()

    def paintEvent(self, event):
        line = QPainter()
        line.begin(self)
        line.setPen(Qt.red)
        line.drawLine(5,33,340,33)
        line.setPen(Qt.black)
        line.drawLine(375,0,375,530)
        line.drawLine(0,530,1220,530)
        line.drawLine(0,350,375,350)
        line.drawLine(0,400,375,400)
        line.drawLine(0,450,375,450)
        line.drawLine(187,400,187,450)

    def b1clicked(self):
        if not possibleClicks(globalState).__contains__([0,0]):
            self.winL.setText("HUMAN TURN -- \nPlease place your coin in right position")
            self.winL.adjustSize()
            return
        else:
            self.b[0].setIcon(QIcon("blue.png"))
            self.b[0].setIconSize(QSize(50, 50))
            self.b[0].setEnabled(False)
            globalState.humanCoord.append([0,0])

            if terminalTest(globalState) and utilityValue(globalState) == -1:
                self.winL.setText("HUMAN WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            if self.gameType == "MINIMAX":
                action = minimax(globalState)
            elif self.gameType == "ALPHABETA":
                action = alphabeta(globalState)

            globalState.machineCoord.append(action)
            temp = coordToNo(action)
            self.b[temp-1].setIcon(QIcon("green.png"))
            self.b[temp -1].setIconSize(QSize(50, 50))
            self.b[temp-1].setEnabled(False)

            if terminalTest(globalState) and utilityValue(globalState) == 1:
                self.winL.setText("MACHINE WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            self.winL.setText("Machine already played ! \nHuman it's your Turn...Place your blue coin")
            self.winL.adjustSize()


    def b2clicked(self):
        if not possibleClicks(globalState).__contains__([0, 1]):
            self.winL.setText("HUMAN TURN -- \nPlease place your coin in right position")
            self.winL.adjustSize()
            return
        else:
            self.b[1].setIcon(QIcon("blue.png"))
            self.b[1].setIconSize(QSize(50, 50))
            self.b[1].setEnabled(False)
            globalState.humanCoord.append([0, 1])

            if terminalTest(globalState) and utilityValue(globalState) == -1:
                self.winL.setText("HUMAN WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            if self.gameType == "MINIMAX":
                action = minimax(globalState)
            elif self.gameType == "ALPHABETA":
                action = alphabeta(globalState)

            globalState.machineCoord.append(action)
            temp = coordToNo(action)
            self.b[temp - 1].setIcon(QIcon("green.png"))
            self.b[temp - 1].setIconSize(QSize(50, 50))
            self.b[temp - 1].setEnabled(False)

            if terminalTest(globalState) and utilityValue(globalState) == 1:
                self.winL.setText("MACHINE WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            self.winL.setText("Machine already played ! \nHuman it's your Turn...Place your blue coin")
            self.winL.adjustSize()


    def b3clicked(self):
        if not possibleClicks(globalState).__contains__([0, 2]):
            self.winL.setText("HUMAN TURN -- \nPlease place your coin in right position")
            self.winL.adjustSize()
            return
        else:
            self.b[2].setIcon(QIcon("blue.png"))
            self.b[2].setIconSize(QSize(50, 50))
            self.b[2].setEnabled(False)
            globalState.humanCoord.append([0, 2])

            if terminalTest(globalState) and utilityValue(globalState) == -1:
                self.winL.setText("HUMAN WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            if self.gameType == "MINIMAX":
                action = minimax(globalState)
            elif self.gameType == "ALPHABETA":
                action = alphabeta(globalState)

            globalState.machineCoord.append(action)
            temp = coordToNo(action)
            self.b[temp - 1].setIcon(QIcon("green.png"))
            self.b[temp - 1].setIconSize(QSize(50, 50))
            self.b[temp - 1].setEnabled(False)

            if terminalTest(globalState) and utilityValue(globalState) == 1:
                self.winL.setText("MACHINE WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            self.winL.setText("Machine already played ! \nHuman it's your Turn...Place your blue coin")
            self.winL.adjustSize()


    def b4clicked(self):
        if not possibleClicks(globalState).__contains__([0, 3]):
            self.winL.setText("HUMAN TURN -- \nPlease place your coin in right position")
            self.winL.adjustSize()
            return
        else:
            self.b[3].setIcon(QIcon("blue.png"))
            self.b[3].setIconSize(QSize(50, 50))
            self.b[3].setEnabled(False)
            globalState.humanCoord.append([0, 3])

            if terminalTest(globalState) and utilityValue(globalState) == -1:
                self.winL.setText("HUMAN WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            if self.gameType == "MINIMAX":
                action = minimax(globalState)
            elif self.gameType == "ALPHABETA":
                action = alphabeta(globalState)

            globalState.machineCoord.append(action)
            temp = coordToNo(action)
            self.b[temp - 1].setIcon(QIcon("green.png"))
            self.b[temp - 1].setIconSize(QSize(50, 50))
            self.b[temp - 1].setEnabled(False)

            if terminalTest(globalState) and utilityValue(globalState) == 1:
                self.winL.setText("MACHINE WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            self.winL.setText("Machine already played ! \nHuman it's your Turn...Place your blue coin")
            self.winL.adjustSize()


    def b5clicked(self):
        if not possibleClicks(globalState).__contains__([1,0]):
            self.winL.setText("HUMAN TURN -- \nPlease place your coin in right position")
            self.winL.adjustSize()
            return
        else:
            self.b[4].setIcon(QIcon("blue.png"))
            self.b[4].setIconSize(QSize(50, 50))
            self.b[4].setEnabled(False)
            globalState.humanCoord.append([1, 0])

            if terminalTest(globalState) and utilityValue(globalState) == -1:
                self.winL.setText("HUMAN WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            if self.gameType == "MINIMAX":
                action = minimax(globalState)
            elif self.gameType == "ALPHABETA":
                action = alphabeta(globalState)

            globalState.machineCoord.append(action)
            temp = coordToNo(action)
            self.b[temp - 1].setIcon(QIcon("green.png"))
            self.b[temp - 1].setIconSize(QSize(50, 50))
            self.b[temp - 1].setEnabled(False)

            if terminalTest(globalState) and utilityValue(globalState) == 1:
                self.winL.setText("MACHINE WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            self.winL.setText("Machine already played ! \nHuman it's your Turn...Place your blue coin")
            self.winL.adjustSize()


    def b6clicked(self):
        if not possibleClicks(globalState).__contains__([1,1]):
            self.winL.setText("HUMAN TURN -- \nPlease place your coin in right position")
            self.winL.adjustSize()
            return
        else:
            self.b[5].setIcon(QIcon("blue.png"))
            self.b[5].setIconSize(QSize(50, 50))
            self.b[5].setEnabled(False)
            globalState.humanCoord.append([1,1])

            if terminalTest(globalState) and utilityValue(globalState) == -1:
                self.winL.setText("HUMAN WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            if self.gameType == "MINIMAX":
                action = minimax(globalState)
            elif self.gameType == "ALPHABETA":
                action = alphabeta(globalState)

            globalState.machineCoord.append(action)
            temp = coordToNo(action)
            self.b[temp - 1].setIcon(QIcon("green.png"))
            self.b[temp - 1].setIconSize(QSize(50, 50))
            self.b[temp - 1].setEnabled(False)

            if terminalTest(globalState) and utilityValue(globalState) == 1:
                self.winL.setText("MACHINE WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            self.winL.setText("Machine already played ! \nHuman it's your Turn...Place your blue coin")
            self.winL.adjustSize()


    def b7clicked(self):
        if not possibleClicks(globalState).__contains__([1,2]):
            self.winL.setText("HUMAN TURN -- \nPlease place your coin in right position")
            self.winL.adjustSize()
            return
        else:
            self.b[6].setIcon(QIcon("blue.png"))
            self.b[6].setIconSize(QSize(50, 50))
            self.b[6].setEnabled(False)
            globalState.humanCoord.append([1,2])

            if terminalTest(globalState) and utilityValue(globalState) == -1:
                self.winL.setText("HUMAN WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            if self.gameType == "MINIMAX":
                action = minimax(globalState)
            elif self.gameType == "ALPHABETA":
                action = alphabeta(globalState)

            globalState.machineCoord.append(action)
            temp = coordToNo(action)
            self.b[temp - 1].setIcon(QIcon("green.png"))
            self.b[temp - 1].setIconSize(QSize(50, 50))
            self.b[temp - 1].setEnabled(False)

            if terminalTest(globalState) and utilityValue(globalState) == 1:
                self.winL.setText("MACHINE WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            self.winL.setText("Machine already played ! \nHuman it's your Turn...Place your blue coin")
            self.winL.adjustSize()


    def b8clicked(self):
        if not possibleClicks(globalState).__contains__([1,3]):
            self.winL.setText("HUMAN TURN -- \nPlease place your coin in right position")
            self.winL.adjustSize()
            return
        else:
            self.b[7].setIcon(QIcon("blue.png"))
            self.b[7].setIconSize(QSize(50, 50))
            self.b[7].setEnabled(False)
            globalState.humanCoord.append([1,3])

            if terminalTest(globalState) and utilityValue(globalState) == -1:
                self.winL.setText("HUMAN WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            if self.gameType == "MINIMAX":
                action = minimax(globalState)
            elif self.gameType == "ALPHABETA":
                action = alphabeta(globalState)

            globalState.machineCoord.append(action)
            temp = coordToNo(action)
            self.b[temp - 1].setIcon(QIcon("green.png"))
            self.b[temp - 1].setIconSize(QSize(50, 50))
            self.b[temp - 1].setEnabled(False)

            if terminalTest(globalState) and utilityValue(globalState) == 1:
                self.winL.setText("MACHINE WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            self.winL.setText("Machine already played ! \nHuman it's your Turn...Place your blue coin")
            self.winL.adjustSize()


    def b9clicked(self):
        if not possibleClicks(globalState).__contains__([2,0]):
            self.winL.setText("HUMAN TURN -- \nPlease place your coin in right position")
            self.winL.adjustSize()
            return
        else:
            self.b[8].setIcon(QIcon("blue.png"))
            self.b[8].setIconSize(QSize(50, 50))
            self.b[8].setEnabled(False)
            globalState.humanCoord.append([2,0])

            if terminalTest(globalState) and utilityValue(globalState) == -1:
                self.winL.setText("HUMAN WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            if self.gameType == "MINIMAX":
                action = minimax(globalState)
            elif self.gameType == "ALPHABETA":
                action = alphabeta(globalState)

            globalState.machineCoord.append(action)
            temp = coordToNo(action)
            self.b[temp - 1].setIcon(QIcon("green.png"))
            self.b[temp - 1].setIconSize(QSize(50, 50))
            self.b[temp - 1].setEnabled(False)

            if terminalTest(globalState) and utilityValue(globalState) == 1:
                self.winL.setText("MACHINE WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            self.winL.setText("Machine already played ! \nHuman it's your Turn...Place your blue coin")
            self.winL.adjustSize()


    def b10clicked(self):
        if not possibleClicks(globalState).__contains__([2,1]):
            self.winL.setText("HUMAN TURN -- \nPlease place your coin in right position")
            self.winL.adjustSize()
            return
        else:
            self.b[9].setIcon(QIcon("blue.png"))
            self.b[9].setIconSize(QSize(50, 50))
            self.b[9].setEnabled(False)
            globalState.humanCoord.append([2,1])

            if terminalTest(globalState) and utilityValue(globalState) == -1:
                self.winL.setText("HUMAN WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            if self.gameType == "MINIMAX":
                action = minimax(globalState)
            elif self.gameType == "ALPHABETA":
                action = alphabeta(globalState)

            globalState.machineCoord.append(action)
            temp = coordToNo(action)
            self.b[temp - 1].setIcon(QIcon("green.png"))
            self.b[temp - 1].setIconSize(QSize(50, 50))
            self.b[temp - 1].setEnabled(False)

            if terminalTest(globalState) and utilityValue(globalState) == 1:
                self.winL.setText("MACHINE WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            self.winL.setText("Machine already played ! \nHuman it's your Turn...Place your blue coin")
            self.winL.adjustSize()


    def b11clicked(self):
        if not possibleClicks(globalState).__contains__([2,2]):
            self.winL.setText("HUMAN TURN -- \nPlease place your coin in right position")
            self.winL.adjustSize()
            return
        else:
            self.b[10].setIcon(QIcon("blue.png"))
            self.b[10].setIconSize(QSize(50, 50))
            self.b[10].setEnabled(False)
            globalState.humanCoord.append([2,2])

            if terminalTest(globalState) and utilityValue(globalState) == -1:
                self.winL.setText("HUMAN WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            if self.gameType == "MINIMAX":
                action = minimax(globalState)
            elif self.gameType == "ALPHABETA":
                action = alphabeta(globalState)

            globalState.machineCoord.append(action)
            temp = coordToNo(action)
            self.b[temp - 1].setIcon(QIcon("green.png"))
            self.b[temp - 1].setIconSize(QSize(50, 50))
            self.b[temp - 1].setEnabled(False)

            if terminalTest(globalState) and utilityValue(globalState) == 1:
                self.winL.setText("MACHINE WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            self.winL.setText("Machine already played ! \nHuman it's your Turn...Place your blue coin")
            self.winL.adjustSize()


    def b12clicked(self):
        if not possibleClicks(globalState).__contains__([2,3]):
            self.winL.setText("HUMAN TURN -- \nPlease place your coin in right position")
            self.winL.adjustSize()
            return
        else:
            self.b[11].setIcon(QIcon("blue.png"))
            self.b[11].setIconSize(QSize(50, 50))
            self.b[11].setEnabled(False)
            globalState.humanCoord.append([2,3])

            if terminalTest(globalState) and utilityValue(globalState) == -1:
                self.winL.setText("HUMAN WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            if self.gameType == "MINIMAX":
                action = minimax(globalState)
            elif self.gameType == "ALPHABETA":
                action = alphabeta(globalState)

            globalState.machineCoord.append(action)
            temp = coordToNo(action)
            self.b[temp - 1].setIcon(QIcon("green.png"))
            self.b[temp - 1].setIconSize(QSize(50, 50))
            self.b[temp - 1].setEnabled(False)

            if terminalTest(globalState) and utilityValue(globalState) == 1:
                self.winL.setText("MACHINE WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            self.winL.setText("Machine already played ! \nHuman it's your Turn...Place your blue coin")
            self.winL.adjustSize()


    def b13clicked(self):
        if not possibleClicks(globalState).__contains__([3,0]):
            self.winL.setText("HUMAN TURN -- \nPlease place your coin in right position")
            self.winL.adjustSize()
            return
        else:
            self.b[12].setIcon(QIcon("blue.png"))
            self.b[12].setIconSize(QSize(50, 50))
            self.b[12].setEnabled(False)
            globalState.humanCoord.append([3,0])

            if terminalTest(globalState) and utilityValue(globalState) == -1:
                self.winL.setText("HUMAN WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            if self.gameType == "MINIMAX":
                action = minimax(globalState)
            elif self.gameType == "ALPHABETA":
                action = alphabeta(globalState)

            globalState.machineCoord.append(action)
            temp = coordToNo(action)
            self.b[temp - 1].setIcon(QIcon("green.png"))
            self.b[temp - 1].setIconSize(QSize(50, 50))
            self.b[temp - 1].setEnabled(False)

            if terminalTest(globalState) and utilityValue(globalState) == 1:
                self.winL.setText("MACHINE WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            self.winL.setText("Machine already played ! \nHuman it's your Turn...Place your blue coin")
            self.winL.adjustSize()


    def b14clicked(self):
        if not possibleClicks(globalState).__contains__([3,1]):
            self.winL.setText("HUMAN TURN -- \nPlease place your coin in right position")
            self.winL.adjustSize()
            return
        else:
            self.b[13].setIcon(QIcon("blue.png"))
            self.b[13].setIconSize(QSize(50, 50))
            self.b[13].setEnabled(False)
            globalState.humanCoord.append([3,1])

            if terminalTest(globalState) and utilityValue(globalState) == -1:
                self.winL.setText("HUMAN WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            if self.gameType == "MINIMAX":
                action = minimax(globalState)
            elif self.gameType == "ALPHABETA":
                action = alphabeta(globalState)

            globalState.machineCoord.append(action)
            temp = coordToNo(action)
            self.b[temp - 1].setIcon(QIcon("green.png"))
            self.b[temp - 1].setIconSize(QSize(50, 50))
            self.b[temp - 1].setEnabled(False)

            if terminalTest(globalState) and utilityValue(globalState) == 1:
                self.winL.setText("MACHINE WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            self.winL.setText("Machine already played ! \nHuman it's your Turn...Place your blue coin")
            self.winL.adjustSize()


    def b15clicked(self):
        if not possibleClicks(globalState).__contains__([3,2]):
            self.winL.setText("HUMAN TURN -- \nPlease place your coin in right position")
            self.winL.adjustSize()
            return
        else:
            self.b[14].setIcon(QIcon("blue.png"))
            self.b[14].setIconSize(QSize(50, 50))
            self.b[14].setEnabled(False)
            globalState.humanCoord.append([3,2])

            if terminalTest(globalState) and utilityValue(globalState) == -1:
                self.winL.setText("HUMAN WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            if self.gameType == "MINIMAX":
                action = minimax(globalState)
            elif self.gameType == "ALPHABETA":
                action = alphabeta(globalState)

            globalState.machineCoord.append(action)
            temp = coordToNo(action)
            self.b[temp - 1].setIcon(QIcon("green.png"))
            self.b[temp - 1].setIconSize(QSize(50, 50))
            self.b[temp - 1].setEnabled(False)

            if terminalTest(globalState) and utilityValue(globalState) == 1:
                self.winL.setText("MACHINE WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            self.winL.setText("Machine already played ! \nHuman it's your Turn...Place your blue coin")
            self.winL.adjustSize()


    def b16clicked(self):
        if not possibleClicks(globalState).__contains__([3,3]):
            self.winL.setText("HUMAN TURN -- \nPlease place your coin in right position")
            self.winL.adjustSize()
            return
        else:
            self.b[15].setIcon(QIcon("blue.png"))
            self.b[15].setIconSize(QSize(50, 50))
            self.b[15].setEnabled(False)
            globalState.humanCoord.append([3,3])

            if terminalTest(globalState) and utilityValue(globalState) == -1:
                self.winL.setText("HUMAN WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            if self.gameType == "MINIMAX":
                action = minimax(globalState)
            elif self.gameType == "ALPHABETA":
                action = alphabeta(globalState)

            globalState.machineCoord.append(action)
            temp = coordToNo(action)
            self.b[temp - 1].setIcon(QIcon("green.png"))
            self.b[temp - 1].setIconSize(QSize(50, 50))
            self.b[temp - 1].setEnabled(False)

            if terminalTest(globalState) and utilityValue(globalState) == 1:
                self.winL.setText("MACHINE WON!! Please reset")
                self.winL.adjustSize()
                for i in range(16):
                    self.b[i].setEnabled(False)
                return

            self.winL.setText("Machine already played ! \nHuman it's your Turn...Place your blue coin")
            self.winL.adjustSize()


    def minimaxBclicked(self):
        self.gameType = "MINIMAX"
        print("\n\n\n-------------------Mim=niMax Algo-------------------\n-------------------AI TURN---------------------")
        action = minimax(globalState)
        print("---- (as all action have same utility value, we choose one random) ----\n*******************************************************************\n\n\n")

        temp = random.choice([1, 2, 3, 4])
        self.b[temp-1].setIcon(QIcon("/Users/rachitrathore/PycharmProjects/AI3/green.png"))
        self.b[temp-1].setIconSize(QSize(50, 50))
        self.b[temp-1].setEnabled(False)
        coord = noToCoord(temp)
        globalState.machineCoord.append(coord)
        self.winL.setText("Machine played first! \nHuman it's your Turn...Place your blue coin")
        self.winL.adjustSize()
        self.minimaxB.setEnabled(False)
        self.alphabetaB.setEnabled(False)
        for i in range(16):
            self.b[i].setEnabled(True)

    def alphabetaBclicked(self):
        self.gameType = "ALPHABETA"
        print("\n\n\n-------------------ALPHA BETA PRUNING-------------------\n-------------------AI TURN---------------------")
        action = alphabeta(globalState)
        print("---- (as all action have same utility value, we choose one random) ----\n********************************************************************\n\n\n")
        temp = random.choice([1, 2, 3, 4])

        self.b[temp - 1].setIcon(QIcon("/Users/rachitrathore/PycharmProjects/AI3/green.png"))
        self.b[temp - 1].setIconSize(QSize(50, 50))
        self.b[temp - 1].setEnabled(False)
        coord = noToCoord(temp)
        globalState.machineCoord.append(coord)
        self.winL.setText("Machine played first! \nHuman it's your Turn...Place your blue coin")
        self.winL.adjustSize()
        self.minimaxB.setEnabled(False)
        self.alphabetaB.setEnabled(False)
        for i in range(16):
            self.b[i].setEnabled(True)


    def restartBclicked(self):
        globalState.machineCoord = []
        globalState.humanCoord = []
        for i in range(16):
            self.b[i].setEnabled(False)
            self.b[i].setIcon(QIcon())
        self.minimaxB.setEnabled(True)
        self.alphabetaB.setEnabled(True)
        self.winL.setText("Machine will move FIRST!!!")
        self.winL.adjustSize()

    def exitBclicked(self):
        self.close()

def window():
    app = QApplication(sys.argv)
    window = GUIDriver()


    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()



