class Launchpad_Out:
    def __init__(self,lp):
        self.lp=lp
        self.initPad()

    def closePad(self):
        self.lp.Reset()
        self.lp.Close()
        print("bye ...")

    def initPad(self):
        self.lp.Reset()
        # turn on launchpad frame
        for i in range(200):
            if (i - 2) % 16 == 0:
                self.lp.LedCtrlRaw(i, 0, 3)
            if (i - 5) % 16 == 0:
                self.lp.LedCtrlRaw(i, 0, 3)
        for i in range(32, 40):
            self.lp.LedCtrlRaw(i, 0, 3)
        for i in range(80, 88):
            self.lp.LedCtrlRaw(i, 0, 3)
        # turn on launchpad top active buttons
        self.lp.LedCtrlRaw(200, 2, 0)
        self.lp.LedCtrlRaw(201, 0, 2)
        self.lp.LedCtrlRaw(205, 2, 0)
        self.lp.LedCtrlRaw(206, 0, 2)
        self.lp.LedCtrlRaw(207, 2, 2)

    def disptext(self,state):
        if state=="HARD" or state=="X WINS!":
            self.lp.LedCtrlString(state, 3, 0, direction=-1, waitms=20)
        if state=="EASY" or state=="DRAW":
            self.lp.LedCtrlString(state, 0, 3, direction=-1, waitms=20)
        if state=="1v1" or state=="O WINS!":
            self.lp.LedCtrlString(state, 3, 3, direction=-1, waitms=20)

    def dispmove(self,i,player):
        if player=="X":
            self.R=3
            self.G=0
        if player=="O":
            self.R=3
            self.G=3
        self.lp.LedCtrlRaw(i, self.R,self.G)
        self.lp.LedCtrlRaw(i + 1, self.R,self.G)
        self.lp.LedCtrlRaw(i + 16, self.R,self.G)
        self.lp.LedCtrlRaw(i + 16 + 1, self.R, self.G)

    def dispwin(self,filled,state):
        self.lp.LedAllOn(0)
        for i in range(len(filled)):
            if state == "X":
                self.lp.LedCtrlRaw(filled[i], 3, 0)
            elif state=="O":
                self.lp.LedCtrlRaw(filled[i], 3, 3)
