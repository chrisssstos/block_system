#Launchpad tic tac toe using AI
#Christos Constantinou , 2021
from player_move import *
import sys
import random
from buttons import Buttons
from board import Board
try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        sys.exit("error loading launchpad.py")
class Game:
    def __init__(self):
        mode = None
        if launchpad.Launchpad().Check(0):
            self.lp = launchpad.Launchpad()
            if self.lp.Open(0):
                print("Launchpad Mk1/S/Mini")
                mode = "Mk1"
        if mode is None:
            print("Did not find any Launchpads, meh...")
            return

        print("QUIT: Push button 1 , RESET: Push button 2", "MODES: RIGHT BAR")

        self.dif=1 #difficlty 1=hard,2=easy,3=1v1
        self.frame = []
        self.X= []
        self.O=[]
        self.Xturn = random.getrandbits(1)
        self.board= Board(self.lp,self.frame)
        self.check = Check()
        self.player_move = Player_move(self.Xturn)
        self.ai_move = AI_move()
        self.buttons = Buttons()
#game loop
    def game_loop(self):
        events = self.lp.ButtonStateRaw()
        self.difficulty(events)
        Buttons.button_actions(self.buttons,events,self.lp,self.frame,self.X,self.O)
        Player_move.move(self.player_move,self.lp,self.frame,self.X,self.O,events,self.dif)
        Check.check_cases(self.check,self.lp,self.frame,self.X,self.O)
    def difficulty(self,events):
        if events == [205, True]:
            self.dif=1
        if events == [206, True]:
            self.dif=2
        if events == [207, True]:
            self.dif=3
if __name__ == "__main__":
    game = Game()
    while True:
        game.game_loop()