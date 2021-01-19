from ai_move import AI_move
from check import Check
class Player_move:
    def __init__(self,Xturn):
        self.range=200
        self.check = Check()
        self.Xturn = Xturn
        self.ai_move = AI_move()
        self.moves = [0,3,6,
                      48, 51, 54,
                      96, 99, 102
                      ]
#X and O moving
    def move(self,lp,frame,X,O,events,dif):
        self.lp=lp
        self.frame=frame
        self.X=X
        self.O=O
        self.events=events
        if not X and not O:
            self.ai_move.avail_move = self.moves.copy()
        for i in range(self.range):
            if self.Xturn:
                if i in self.moves and i not in self.X and i not in self.O:
                    if self.events == [i, True]:
                        self.lp.LedCtrlRaw(i, 3, 0)
                        self.lp.LedCtrlRaw(i+1, 3, 0)
                        self.lp.LedCtrlRaw(i + 16, 3, 0)
                        self.lp.LedCtrlRaw(i + 16+1, 3, 0)
                        self.X.append(i)
                        self.ai_move.avail_move.remove(i)
                        self.Xturn=False
            elif not self.Xturn and dif==1 or dif ==2:
                if self.ai_move.avail_move != []:
                    j = AI_move.ai_move(self.ai_move,self.X,self.O,dif)
                    if j not in self.X and j not in self.O and Check.checkWIN(self.check,self.X) != True :
                        self.lp.LedCtrlRaw(j, 2, 2)
                        self.lp.LedCtrlRaw(j + 1, 2, 2)
                        self.lp.LedCtrlRaw(j + 16, 2, 2)
                        self.lp.LedCtrlRaw(j + 16 + 1, 2, 2)
                        self.O.append(j)
                        self.ai_move.avail_move.remove(j)
                        self.Xturn = True
            elif not self.Xturn and dif==3:
                if i in self.moves and i not in self.X and i not in self.O:
                    if self.events == [i, True]:
                        self.lp.LedCtrlRaw(i, 2,2)
                        self.lp.LedCtrlRaw(i + 1, 2, 2)
                        self.lp.LedCtrlRaw(i + 16, 2, 2)
                        self.lp.LedCtrlRaw(i + 16 + 1, 2, 2)
                        self.O.append(i)
                        self.ai_move.avail_move.remove(i)
                        # print(self.ai_move.avail_move)
                        self.Xturn = True
