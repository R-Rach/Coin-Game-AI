"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


class State:

    def __init__(self, humanCoord, machineCoord):
        self.humanCoord = humanCoord
        self.machineCoord = machineCoord

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return "Human - " + str(self.humanCoord) + " Machine - " + str(self.machineCoord)