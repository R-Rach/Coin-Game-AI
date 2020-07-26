"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


import math

from SuccessorFunction import possibleClicks, State, nextStates
from TerminalTest import terminalTest
from UtilityValue import utilityValue


def min_value(currState):

    if terminalTest(currState):
        return utilityValue(currState)

    value = 100
    currNodeTpye = "MIN"
    clickArr = []
    clickArr = possibleClicks(currState)
    temp = 0

    for i in clickArr:
        temp = max_value(nextStates(currState, i, currNodeTpye))

        if temp < value:
            value = temp

    return value


def max_value(currState):

    if terminalTest(currState):
        return utilityValue(currState)

    value = -100
    currNodeTpye = "MAX"
    clickArr = []
    clickArr = possibleClicks(currState)

    for i in clickArr:
        temp = min_value(nextStates(currState, i, currNodeTpye))
        if temp > value:
            value = temp

    return value