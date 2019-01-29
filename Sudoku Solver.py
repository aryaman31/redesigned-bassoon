import copy
gameB = [["2"," "," "," "," ","7"," ","5"," "],
         [" "," "," "," "," "," ","3"," "," "],
         [" "," ","1","2"," ","8"," "," "," "],
         ["7"," "," "," "," ","3"," "," ","1"],
         [" "," ","2"," "," "," "," ","6"," "],
         [" ","6"," "," "," ","1","4"," "," "],
         [" "," ","4","1"," ","6"," "," ","8"],
         [" "," ","8"," "," "," ","7"," "," "],
         [" ","5"," "," "," "," "," ","9"," "]]


def disp(board):
    a = 0 
    for i in board:
        a = a + 1
        k = ""
        c = 0
        for j in i:
            c = c + 1
            try:
                k = k + "[" + j + "]"
            except:
                k = k + "[ ]"
            if c%3 == 0 and c != 9:
                k = k + "  "
        print(k)
        if a%3 == 0 and a != 9:
            print("")

def rawDisp(board):
    for i in board:
        print(i)

def possiblity(gameD):
    for i in range(0,9):
        for j in range(0,9):
            num = ["1","2","3","4","5","6","7","8","9"]
            if gameD[i][j] not in ["1","2","3","4","5","6","7","8","9"]:
                for k in range(0,9):
                    if gameD[i][k] in num:
                        num.remove(gameD[i][k])
                    if gameD[k][j] in num:
                        num.remove(gameD[k][j])
                gameD[i][j] = num
    return gameD

def boxCut(gameD):
    for i in range(0,7,3):  # Looping through Whole sectors
        for j in range(0,7,3):
            temp = []
            for k in range(0,3):  # Starts looping within sector
                for l in range(0,3):
                    if gameD[i+k][j+l] != " ":
                        temp.append(gameD[i+k][j+l])
            for k in range(0,3):  # Starts looping within sector
                for l in range(0,3):
                    if gameD[i+k][j+l] not in ["1","2","3","4","5","6","7","8","9"]:
                        temp1 = gameD[i+k][j+l][:]
                        for m in temp1:
                            if m in temp:
                                gameD[i+k][j+l].remove(m)
    return gameD

def checker(gameD,listLeft,update):
    listLeft = False
    for i in range(0,9):
        for j in range(0,9):
            if gameD[i][j] not in ["1","2","3","4","5","6","7","8","9"]:
                listLeft = True
                if len(gameD[i][j]) == 1:
                    update = True
                    gameD[i][j] = gameD[i][j][0]                  
    return gameD,listLeft,update

def secCheck(gameD):
    # Horizontal Check
    update = False
    for num in range(1,10):
        for i in range(0,9):
            c = 0
            loc = []
            for j in range(0,9):
                if gameD[i][j] not in ["1","2","3","4","5","6","7","8","9"]:
                    if str(num) in gameD[i][j]:
                        loc.append([i,j])
                        c = c + 1
            if c == 1:   # This is the only number in that line
                update = True
                gameD[loc[0][0]][loc[0][1]] = str(num)
        if update != True:
            for iv in range(0,9):
                c = 0
                loc = []
                for jv in range(0,9):
                    if gameD[jv][iv] not in ["1","2","3","4","5","6","7","8","9"]:
                        if str(num) in gameD[jv][iv]:
                            c = c + 1
                            loc.append([jv,iv])
                if c == 1: # This is the only number in the column 
                    update = True
                    gameD[loc[0][0]][loc[0][1]] = str(num)
        else:
            break
    return gameD, update

def innerplay(gameD):
    listLeft = True
    temp = []
    update = True
    a = 0
    while listLeft == True and update == True:
        update = False
        gameD = possiblity(gameD)
        gameD = boxCut(gameD)
        gameD,listLeft,update = checker(gameD,listLeft,update)
        if update == False:
            gameD,update = secCheck(gameD)
    return gameD,listLeft, update

def gameplay(gameD):
    gameD,listLeft, update = innerplay(gameD)
    if not(solveChecker(gameD)):
        gameD = bruteforceV2(gameD)
    return listLeft, update, gameD

def solveChecker(gameD):
    correct = True
    for i in range(0,9):
        numh = ["1","2","3","4","5","6","7","8","9"]
        numv = ["1","2","3","4","5","6","7","8","9"]
        for j in range(0,9):
            try:
                numh.remove(gameD[i][j])
                numv.remove(gameD[j][i])
            except:
                correct = False
    return correct

def bruteforceV2(game):
    solved = False
    for i in range(0,9):
        for j in range(0,9):
            if game[i][j] not in ["1","2","3","4","5","6","7","8","9"]:
                for k in range(0 , len(game[i][j]) ):
                    tempgame = copy.deepcopy(game)
                    tempgame[i][j] = game[i][j][k]
                    tempgame,listLeft, update = innerplay(tempgame)
                    if solveChecker(tempgame):
                        solved = True
                        return tempgame                        

def main(gameD):
    listLeft, update, gameD = gameplay(gameD)
    disp(gameD)
    
disp(gameB)
print("\n\n")
gameD = gameB[:]
main(gameD)
print("done")
