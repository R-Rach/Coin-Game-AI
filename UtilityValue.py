"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


from State import State
from TerminalTest import terminalTest
from CheckWinUtil import checkWin


def utilityValue(state):

    if terminalTest(state):

        if checkWin(state.machineCoord):
            return 1
        if checkWin(state.humanCoord):
            return -1
        return 0