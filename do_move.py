from ai_move import AI_move
import constants
class Do_move:
    def __init__(self,board,lp_out):
        self.board = board
        self.lp_out=lp_out
        self.ai_move = AI_move(board)

#X and O moving
    def move(self,events):
        self.events=events
        if not self.board.X and not self.board.O:
            self.board.avail_move = constants.moves.copy()
        for i in range(constants.range):
            if self.board.Xturn:
                if i in constants.moves and i not in self.board.X and i not in self.board.O:
                    if self.events == [i, True]:
                        self.lp_out.dispmove(i,"X")
                        self.board.X.append(i)
                        self.board.avail_move.remove(i)
                        self.board.Xturn=False
            elif not self.board.Xturn and self.board.dif==1 or self.board.dif ==2:
                if self.board.avail_move != []:
                    j = self.ai_move.next_move()
                    if j not in self.board.X and j not in self.board.O and self.board.checkWIN(self.board.X) != True :
                        self.lp_out.dispmove(j,"O")
                        self.board.O.append(j)
                        self.board.avail_move.remove(j)
                        self.board.Xturn = True
            elif not self.board.Xturn and self.board.dif==3:
                if i in constants.moves and i not in self.board.X and i not in self.board.O:
                    if self.events == [i, True]:
                        self.lp_out.dispmove(i,"O")
                        self.board.O.append(i)
                        self.board.avail_move.remove(i)
                        self.board.Xturn = True

        self.board.check_cases()