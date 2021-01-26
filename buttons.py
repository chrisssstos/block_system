

class Buttons:
    def __init__(self,board,lp_out):
        self.board=board
        self.lp_out=lp_out
    def button_actions(self,events):
        #close/reset
        if events == [200, True]:
            self.lp_out.closePad()
        if events == [201, True]:
            self.lp_out.initPad()
            self.board.resetBoard(self.board.X,self.board.O)

        #modes
        if events == [205, True]:
            self.lp_out.disptext("HARD")
            self.lp_out.initPad()
            self.board.resetBoard(self.board.X, self.board.O)
        if events == [206, True]:
            self.lp_out.disptext("EASY")
            self.lp_out.initPad()
            self.board.resetBoard(self.board.X, self.board.O)
        if events == [207, True]:
            self.lp_out.disptext("1v1")
            self.lp_out.initPad()
            self.board.resetBoard(self.board.X, self.board.O)

        #difficulty
        if events == [205, True]:
            self.board.dif=1
        if events == [206, True]:
            self.board.dif=2
        if events == [207, True]:
            self.board.dif=3