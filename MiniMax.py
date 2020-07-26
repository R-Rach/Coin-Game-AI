"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


import math

from MinMaxValueFuction import *
from SuccessorFunction import possibleClicks, State, nextStates


def minimax(currState):

    value = -100
    currNodeType = "MAX"
    action = 0

    clickArrAction = []
    clickArrAction = possibleClicks(currState)
    print("possible action clicks",clickArrAction)
    temp = 0

    for i in clickArrAction:
        print(i)

        s = nextStates(currState,i,currNodeType)
        print("minimax state---",s)
        print("please wait, game tree on process.....")
        if terminalTest(s) and utilityValue(s) == 1:
            return i

        temp = min_value(s)
        print("uti val--> ",temp)
        print("---------------")
        if temp > value:
            value = temp
            action = i

    return action