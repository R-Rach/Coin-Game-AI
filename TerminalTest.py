"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


from CheckWinUtil import checkWin


def terminalTest(state):
    if len(state.machineCoord) == 8 and len(state.humanCoord) == 8:
        return True
    if checkWin(state.machineCoord) or checkWin(state.humanCoord):
        return True

    return False