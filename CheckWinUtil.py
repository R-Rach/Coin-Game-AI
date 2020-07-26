"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


def checkWin(coord):
    for i in coord:
        #right-hori(works for left-hori also)
        if( isValid(i[0],i[1]) and isValid(i[0],i[1]+1) and isValid(i[0],i[1]+2) and coord.__contains__([i[0],i[1]]) and coord.__contains__([i[0],i[1]+1]) and coord.__contains__([i[0],i[1]+2]) ):
            return True

        #bottom/up - verti
        if( isValid(i[0],i[1]) and isValid(i[0]+1,i[1]) and isValid(i[0]+2,i[1]) and coord.__contains__([i[0],i[1]]) and coord.__contains__([i[0]+1,i[1]]) and coord.__contains__([i[0]+2,i[1]]) ):
            return True

        #diagonal-/
        if( isValid(i[0],i[1]) and isValid(i[0]-1,i[1]+1) and isValid(i[0]-2,i[1]+2) and coord.__contains__([i[0],i[1]]) and coord.__contains__([i[0]-1,i[1]+1]) and coord.__contains__([i[0]-2,i[1]+2]) ):
            return True

        #diagonal-\
        if( isValid(i[0],i[1]) and isValid(i[0]-1,i[1]-1) and isValid(i[0]-2,i[1]-2) and coord.__contains__([i[0],i[1]]) and coord.__contains__([i[0]-1,i[1]-1]) and coord.__contains__([i[0]-2,i[1]-2]) ):
            return True

    return False

def isValid(row, col):
    if row < 0 or row > 3:
        return False
    if col < 0 or col > 3:
        return False
    return True

def noToCoord(x):
    if x % 4 == 0:
        return [x//4 -1, 3]
    else:
        return [x//4, x%4 - 1]

def coordToNo(coord):
    return (coord[0]*4) + coord[1] + 1