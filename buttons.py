from board import Board

class Buttons:
    def __init__(self):
        pass
    def button_actions(self,events,lp,frame,X,O):
        self.X=X
        self.O=O
        if events == [200, True]:
            lp.Reset()
            lp.Close()
            print("bye ...")
        if events == [201, True]:
            lp.Reset()
            self.board = Board(lp, frame)
            self.X.clear()
            self.O.clear()
        if events == [205, True]:
            lp.LedCtrlString("HARD", 3,0, direction=-1, waitms=20)
            lp.Reset()
            self.board = Board(lp, frame)
            self.X.clear()
            self.O.clear()
        if events == [206, True]:
            lp.LedCtrlString("EASY", 0,3, direction=-1, waitms=20)
            lp.Reset()
            self.board = Board(lp, frame)
            self.X.clear()
            self.O.clear()
        if events == [207, True]:
            lp.LedCtrlString("1v1", 3,3, direction=-1, waitms=20)
            lp.Reset()
            self.board = Board(lp, frame)
            self.X.clear()
            self.O.clear()
