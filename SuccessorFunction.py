"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


import copy

from State import *

def nextStates(currState, action, currPlayerType):
    newState = copy.deepcopy(currState)

    if currPlayerType == "MAX":
        newState.machineCoord.append(action)
    elif currPlayerType == "MIN":
        newState.humanCoord.append(action)

    return newState



def possibleClicks(currState):
    clickArr = []

    #for col1
    for i in range(4):
        if currState.machineCoord.__contains__([i,0]) or currState.humanCoord.__contains__([i,0]):
            continue
        else:
            clickArr.append([i,0])
            break

    # for col2
    for i in range(4):
        if currState.machineCoord.__contains__([i, 1]) or currState.humanCoord.__contains__([i, 1]):
            continue
        else:
            clickArr.append([i, 1])
            break

    # for col3
    for i in range(4):
        if currState.machineCoord.__contains__([i, 2]) or currState.humanCoord.__contains__([i, 2]):
            continue
        else:
            clickArr.append([i, 2])
            break

    # for col4
    for i in range(4):
        if currState.machineCoord.__contains__([i, 3]) or currState.humanCoord.__contains__([i, 3]):
            continue
        else:
            clickArr.append([i, 3])
            break

    return clickArr