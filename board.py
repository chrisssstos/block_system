class Board:
    def __init__(self,lp,frame):
        self.lp=lp
        self.frame=frame
        #making the board frame and the interactive buttons
        for i in range(200):
            if (i-2)%16==0:
                self.lp.LedCtrlRaw(i, 0, 3)
                self.frame.append(i)
            if (i-5)%16==0:
                self.lp.LedCtrlRaw(i, 0, 3)
                self.frame.append(i)
        for i in range(32,40):
            self.lp.LedCtrlRaw(i, 0, 3)
            self.frame.append(i)
        for i in range(80,88):
            self.lp.LedCtrlRaw(i, 0, 3)
            self.frame.append(i)
        #launchpad side and top inactive buttons
        self.frame.append(8)
        self.frame.append(24)
        self.frame.append(40)
        self.frame.append(56)
        self.frame.append(72)
        self.frame.append(88)
        self.frame.append(104)
        self.frame.append(120)
        #launchpad top active buttons
        self.lp.LedCtrlRaw(200,2,0)
        self.lp.LedCtrlRaw(201,0,2)
        self.lp.LedCtrlRaw(205,2,0)
        self.lp.LedCtrlRaw(206,0,2)
        self.lp.LedCtrlRaw(207,2,2)

