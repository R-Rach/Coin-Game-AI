"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


from State import State
from SuccessorFunction import possibleClicks, nextStates
from TerminalTest import terminalTest
from UtilityValue import utilityValue

global abcountNodes
abcountNodes = 0

def abmax_value(currState, alpha, beta):
    if terminalTest(currState):
        return utilityValue(currState)

    value = -100
    currNodeTpye = "MAX"
    clickArr = []
    clickArr = possibleClicks(currState)
    global abcountNodes

    for i in clickArr:
        abcountNodes = abcountNodes + 1
        temp = abmin_value(nextStates(currState, i, currNodeTpye),alpha,beta)
        if temp > value:
            value = temp
        alpha = max(alpha,value)
        if alpha >= beta:
            break

    return value


def abmin_value(currState, alpha, beta):
    if terminalTest(currState):
        return utilityValue(currState)

    value = 100
    currNodeTpye = "MIN"
    clickArr = []
    clickArr = possibleClicks(currState)
    temp = 0
    global abcountNodes

    for i in clickArr:
        abcountNodes = abcountNodes + 1
        temp = abmax_value(nextStates(currState, i, currNodeTpye), alpha, beta)

        if temp < value:
            value = temp
        beta = min(beta,value)
        if alpha >= beta:
            break

    return value


def alphabeta(currState):
    value = -100
    currNodeType = "MAX"
    action = 0
    alpha = -100
    beta = 100

    clickArrAction = []
    clickArrAction = possibleClicks(currState)
    print("possible action clicks", clickArrAction)
    temp = 0
    global abcountNodes

    for i in clickArrAction:
        print(i)

        s = nextStates(currState, i, currNodeType)
        abcountNodes = abcountNodes + 1
        print("state---", s)
        print("please wait, game tree on process.....")
        if terminalTest(s) and utilityValue(s) == 1:
            return i

        temp = abmin_value(s,alpha,beta)
        print("uti val--> ",temp)
        print("---------------")
        if temp > value:
            value = temp
            action = i
        alpha = max(alpha,value)
        if alpha >= beta:
            break

    return action