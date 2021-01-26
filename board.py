import random
import time
import copy
import constants

class Board:
    def __init__(self,lp_out):
        #launchpad output
        self.lp_out = lp_out
        #state
        self.X= []
        self.O= []
        self.avail_move = []
        self.Xturn = random.getrandbits(1)
        self.dif = 1

    def resetBoard(self,X,O):
        X.clear()
        O.clear()


    def checkWIN(self,symbol):
        self.symbol = symbol
        if all(i in symbol for i in constants.winH1):
            return True
        if all(i in symbol for i in constants.winH2):
            return True
        if all(i in symbol for i in constants.winH3):
            return True
        if all(i in symbol for i in constants.winV1):
            return True
        if all(i in symbol for i in constants.winV2):
            return True
        if all(i in symbol for i in constants.winV3):
            return True
        if all(i in symbol for i in constants.winD1):
            return True
        if all(i in symbol for i in constants.winD2):
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
        if all(i in symbol for i in constants.winH1):
            return constants.winH1
        if all(i in symbol for i in constants.winH2):
            return constants.winH2
        if all(i in symbol for i in constants.winH3):
            return constants.winH3
        if all(i in symbol for i in constants.winV1):
            return constants.winV1
        if all(i in symbol for i in constants.winV2):
            return constants.winV2
        if all(i in symbol for i in constants.winV3):
            return constants.winV3
        if all(i in symbol for i in constants.winD1):
            return constants.winD1
        if all(i in symbol for i in constants.winD2):
            return constants.winD2

    #actions after win case
    def check_cases(self):
        if self.checkWIN(self.X) == True:
            filled = self.fill(self.returnWIN(self.X))
            self.lp_out.dispwin(filled,"X")
            time.sleep(1)
            self.lp_out.disptext("X WINS!")
            self.lp_out.initPad()
            self.resetBoard(self.X,self.O)
        if self.checkWIN(self.O) == True:
            filled = self.fill(self.returnWIN(self.O))
            self.lp_out.dispwin(filled,"O")
            time.sleep(1)
            self.lp_out.disptext("O WINS!")
            self.lp_out.initPad()
            self.resetBoard(self.X,self.O)
        if len(self.X)==5 or len(self.O)==5:
            time.sleep(1)
            self.lp_out.disptext("DRAW")
            self.lp_out.initPad()
            self.resetBoard(self.X,self.O)