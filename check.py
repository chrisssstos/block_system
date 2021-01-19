from board import Board
import random
import time
import copy
class Check:
    def __init__(self):
        #winning cases
        self.winH1 = [0, 3, 6]
        self.winH2 = [48, 51, 54]
        self.winH3 = [96, 99, 102]
        self.winV1 = [0, 48, 96]
        self.winV2 = [3, 51, 99]
        self.winV3 = [6, 54, 102]
        self.winD1 = [0, 51, 102]
        self.winD2 = [6, 51, 96]
    #checking if win state is reached
    def checkWIN(self,symbol):
        self.symbol = symbol
        if all(i in symbol for i in self.winH1):
            return True
        if all(i in symbol for i in self.winH2):
            return True
        if all(i in symbol for i in self.winH3):
            return True
        if all(i in symbol for i in self.winV1):
            return True
        if all(i in symbol for i in self.winV2):
            return True
        if all(i in symbol for i in self.winV3):
            return True
        if all(i in symbol for i in self.winD1):
            return True
        if all(i in symbol for i in self.winD2):
            return True

    def fill(self,array):
        array2=copy.deepcopy(array)
        for i in range(0,3):
            array2.append(array[i]+1)
            array2.append(array[i] + 16)
            array2.append(array[i] + 17)
        return array2

    def returnWIN(self,symbol):
        self.symbol = symbol
        if all(i in symbol for i in self.winH1):
            return self.winH1
        if all(i in symbol for i in self.winH2):
            return self.winH2
        if all(i in symbol for i in self.winH3):
            return self.winH3
        if all(i in symbol for i in self.winV1):
            return self.winV1
        if all(i in symbol for i in self.winV2):
            return self.winV2
        if all(i in symbol for i in self.winV3):
            return self.winV3
        if all(i in symbol for i in self.winD1):
            return self.winD1
        if all(i in symbol for i in self.winD2):
            return self.winD2

    #actions after win case
    def check_cases(self,lp,frame,X,O):
        self.lp=lp
        self.frame=frame
        self.X=X
        self.O=O
        if self.checkWIN(self.X) == True:
            filled = self.fill(self.returnWIN(self.X))
            self.lp.LedAllOn(0)
            for i in range(len(filled)):
                self.lp.LedCtrlRaw(filled[i],3,0)
            time.sleep(1)
            self.lp.LedCtrlString("X WINS!", 3, 0, direction=-1, waitms=50)
            self.lp.Reset()
            self.board = Board(self.lp, self.frame)
            self.X.clear()
            self.O.clear()
        if self.checkWIN(self.O) == True:
            self.lp.LedAllOn(0)
            filled = self.fill(self.returnWIN(self.O))
            for i in range(len(filled)):
                self.lp.LedCtrlRaw(filled[i],2,2)
            time.sleep(1)
            self.lp.LedCtrlString("O WINS!", 3, 3, direction=-1, waitms=50)
            self.lp.Reset()
            self.board = Board(self.lp, self.frame)
            self.X.clear()
            self.O.clear()
        if len(self.X)==5 or len(self.O)==5:
            time.sleep(1)
            self.lp.LedCtrlString("DRAW", 0, 3, direction=-1, waitms=50)
            self.lp.Reset()
            self.board = Board(self.lp, self.frame)
            self.X.clear()
            self.O.clear()