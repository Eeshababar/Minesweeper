# ==============================CS-199==================================
# FILE:         MyAI.py
#
# AUTHOR:       Justin Chung
#
# DESCRIPTION:  This file contains the MyAI class. You will implement your
#               agent in this file. You will write the 'getAction' function,
#               the constructor, and any additional helper functions.
#
# NOTES:        - MyAI inherits from the abstract AI class in AI.py.
#
#               - DO NOT MAKE CHANGES TO THIS FILE.
# ==============================CS-199==================================
 
from cgitb import reset
from operator import rshift
from re import X
from AI import AI
from Action import Action
 
counter = 0
 
class MyAI( AI ):
 
    def __init__(self, rowDimension, colDimension, totalMines, startX, startY):
        self.__rowDimension = rowDimension
        self.__colDimension = colDimension
        self.__startX= startX
        self.__startY= startY
        self.__board = [[-1 for i in range(self.__colDimension)] for j in range(self.__rowDimension)]
        self.store = []
 
    def printTile(self):
            for j in self.__board:
                for i in j:
                    print(i,end = " ")
                print()
            print()
 
    def checkLabelIs0(self, r, c) -> "list":
        if(r -1 >= 0 and c +1 < self.__colDimension and self.__board[r-1][c+1] == 0):
            return [r-1, c+1]
        elif(r  -1 >= 0 and self.__board[r-1][c] == 0):
            return [r-1, c]
        elif(r -1 >= 0 and c -1 >=0 and self.__board[r-1][c-1] == 0):
            return [r-1,c-1]
        elif( c+1 < self.__colDimension and self.__board[r][c+1] == 0):
            return [r,c+1]
        elif( c -1 >=0 and self.__board[r][c-1] == 0):
            return [r, c-1]
        elif(r + 1 < self.__rowDimension and c +1 < self.__colDimension and self.__board[r+1][c+1] == 0):
            return [r+1,c-1]
        elif(r + 1 < self.__rowDimension and  self.__board[r+1][c] == 0):
            return [r+1,c]
        elif(r + 1 < self.__rowDimension and c -1 >= 0  and self.__board[r+1][c-1] == 0):
            return [r+1,c-1]
        else:
            return []

    def storeLabel_1(self, r, c) -> "list":
        around_1 = []
        if(r -1 >= 0 and c +1 < self.__colDimension and self.__board[r-1][c+1] == -1):
            around_1.append([r-1, c+1])
        if(r  -1 >= 0 and self.__board[r-1][c] == -1):
            around_1.append([r-1, c])
        if(r -1 >= 0 and c -1 >=0 and self.__board[r-1][c-1] == -1):
            around_1.append( [r-1,c-1])
        if( c+1 < self.__colDimension and self.__board[r][c+1] == -1):
            around_1.append( [r,c+1])
        if( c -1 >=0 and self.__board[r][c-1] == -1):
            around_1.append( [r, c-1])
        if(r + 1 < self.__rowDimension and c +1 < self.__colDimension and self.__board[r+1][c+1] == -1):
            around_1.append( [r+1,c+1])
        if(r + 1 < self.__rowDimension and  self.__board[r+1][c] == -1):
            around_1.append([r+1,c])
        if(r + 1 < self.__rowDimension and c -1 >= 0 and self.__board[r+1][c-1] == -1):
            around_1.append( [r+1,c-1])
        return around_1
 
    def findSum (self, r, c) -> int:
        sum = 0
        if(r  -1 >= 0 ):
            if(c-1>= 0):
                sum += self.__board[r-1][c-1]
            if(c+1 < self.__colDimension):
                sum += self.__board[r-1][c+1]
            sum += self.__board[r-1][c]
        if(r+1 < self.__rowDimension):
            if(c-1>= 0):
                sum += self.__board[r+1][c-1]
            if(c+1 < self.__colDimension):
                sum += self.__board[r+1][c+1]
            sum += self.__board[r+1][c]
        if(c-1>= 0):
            sum += self.__board[r][c-1]
        if(c+1 < self.__colDimension):
            sum += self.__board[r][c+1]
 
        return sum
   
    def checkOver_1(self) -> "int":
        count = 0
        for i in self.__board:
            for j in i:
                if(j > -1):
                    count += 1
        return count
 
    def checkAllLabel1Near(self, r, c) -> "bool":
        count = 0
        if(r-1>= 0 and r+1 < self.__rowDimension and c-1 >= 0 and c+1 < self.__colDimension):
            if(r -1 >= 0 and c +1 < self.__colDimension and self.__board[r-1][c+1] == 1):
                count += 1
            if(r  -1 >= 0 and self.__board[r-1][c] == 1):
                count += 1
            if(r -1 >= 0 and c -1 >=0 and self.__board[r-1][c-1] == 1):
                count += 1
            if( c+1 < self.__colDimension and self.__board[r][c+1] == 1):
                count += 1
            if( c -1 >=0 and self.__board[r][c-1] == 1):
                count += 1
            if(r + 1 < self.__rowDimension and c +1 < self.__colDimension and self.__board[r+1][c+1] == 0):
                count += 1
            if(r + 1 < self.__rowDimension and  self.__board[r+1][c] == 0):
                count += 1
            if(r + 1 < self.__rowDimension and c -1 >= 0  and self.__board[r+1][c-1] == 0):
                count += 1
            if(count == 8):
                return True
            else:
                return False
        elif((r== 0 and c == 0) or (r == 0 and c == self.__colDimension -1) or (r== self.__rowDimension-1 and c==0) or (r== self.__rowDimension-1 and c==self.__colDimension)):
            if(r -1 >= 0 and c +1 < self.__colDimension and self.__board[r-1][c+1] == 1):
                count += 1
            if(r  -1 >= 0 and self.__board[r-1][c] == 1):
                count += 1
            if(r -1 >= 0 and c -1 >=0 and self.__board[r-1][c-1] == 1):
                count += 1
            if( c+1 < self.__colDimension and self.__board[r][c+1] == 1):
                count += 1
            if( c -1 >=0 and self.__board[r][c-1] == 1):
                count += 1
            if(r + 1 < self.__rowDimension and c +1 < self.__colDimension and self.__board[r+1][c+1] == 0):
                count += 1
            if(r + 1 < self.__rowDimension and  self.__board[r+1][c] == 0):
                count += 1
            if(r + 1 < self.__rowDimension and c -1 >= 0  and self.__board[r+1][c-1] == 0):
                count += 1
            if(count == 3):
                return True
            else:
                return False
        elif((r== 0 and 0<c and c<self.__colDimension -1) or (r== self.__rowDimension -1 and 0<c and c<self.__colDimension -1) or (0<r and r< self.__rowDimension-1 and c == 0) or (0<r and r< self.__rowDimension-1 and c == self.__colDimension -1)):
            if(r -1 >= 0 and c +1 < self.__colDimension and self.__board[r-1][c+1] == 1):
                count += 1
            if(r  -1 >= 0 and self.__board[r-1][c] == 1):
                count += 1
            if(r -1 >= 0 and c -1 >=0 and self.__board[r-1][c-1] == 1):
                count += 1
            if( c+1 < self.__colDimension and self.__board[r][c+1] == 1):
                count += 1
            if( c -1 >=0 and self.__board[r][c-1] == 1):
                count += 1
            if(r + 1 < self.__rowDimension and c +1 < self.__colDimension and self.__board[r+1][c+1] == 0):
                count += 1
            if(r + 1 < self.__rowDimension and  self.__board[r+1][c] == 0):
                count += 1
            if(r + 1 < self.__rowDimension and c -1 >= 0  and self.__board[r+1][c-1] == 0):
                count += 1
            if(count == 5):
                return True
            else:
                return False
 

    def getAction(self, number: int) -> "Action Object":
        self.__board[self.__startX][self.__startY] = number  #0,1
        if (len(self.store)> 0):
            rowCol = self.store.pop()
            self.__startX = rowCol[0]
            self.__startY = rowCol[1]
            return Action(AI.Action.UNCOVER, rowCol[0], rowCol[1])
        
        for r in range(0,self.__rowDimension,1):
            for c in range(0, self.__colDimension ,1):
                if (self.__board[r][c] == 0):
                    if(self.checkOver_1()>=self.__colDimension*self.__rowDimension -1):
                        return Action(AI.Action.LEAVE)
                    else:
                        if(len(self.storeLabel_1(r,c)) > 0):
                            rc = self.storeLabel_1(r,c)
                            for i in rc:
                                self.store.append(i)
                            if (len(self.store)> 0):
                                rowCol = self.store.pop()
                                self.__startX = rowCol[0]
                                self.__startY = rowCol[1]
                                return Action(AI.Action.UNCOVER, rowCol[0], rowCol[1])

                        elif(len(self.checkLabelIs0(r,c))> 0):
                            rc = self.checkLabelIs0(r,c)
                            self.__startX = rc[0]
                            self.__startY = rc[1]
                            continue
                elif (self.__board[r][c] == -1):
                    if(self.checkAllLabel1Near(r,c)):
                        return Action(AI.Action.LEAVE)
                    else:
                        storeSum = []
                        sumRC = self.findSum(r, c)
                        infoRCS = [r,c,sumRC]
                        storeSum.append(infoRCS)
                        findLabel_1 = self.storeLabel_1(r,c)
                        if(len(findLabel_1)>0 and len(findLabel_1)<3):
                            for i in findLabel_1:
                                sum = self.findSum(i[0],i[1])
                                info = [i[0], i[1],sum]
                                storeSum.append(info)
                            if(len(storeSum) > 1):
                                min = storeSum[0][2]
                                num = 0
                                for i in range(len(storeSum)):
                                    if(min > storeSum[i][2]):
                                        min = storeSum[i][2]
                                        num = i
                                self.__startX = storeSum[num][0]
                                self.__startY = storeSum[num][1]
                                return Action(AI.Action.UNCOVER, self.__startX, self.__startY)
                        else:
                            continue
        return Action(AI.Action.LEAVE)
                                
                                
                            

