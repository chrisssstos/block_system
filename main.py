#Launchpad tic tac toe using AI and launchpad.py https://github.com/FMMT666/launchpad.py
#Christos Constantinou , 2021
from do_move import *
import sys
from buttons import Buttons
from board import Board
from launchpad_out import Launchpad_Out

try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        sys.exit("error loading launchpad.py")
class Game:
    def __init__(self):
        #offical launchpad.py way of initializing the launchpad
        mode = None
        if launchpad.Launchpad().Check(0):
            self.lp = launchpad.Launchpad()
            if self.lp.Open(0):
                print("Launchpad Mk1/S/Mini")
                mode = "Mk1"
        if mode is None:
            print("Did not find any Launchpads, meh...")
            return
        print("QUIT: Push button 1 , RESET: Push button 2, MODES: RIGHT BAR")
        ###

        self.lp_out= Launchpad_Out(self.lp)
        self.board = Board(self.lp_out)
        self.buttons = Buttons(self.board,self.lp_out)
        self.do_move = Do_move(self.board,self.lp_out)
#game loop
    def game_loop(self):
        events = self.lp.ButtonStateRaw()
        self.buttons.button_actions(events)
        self.do_move.move(events)



if __name__ == "__main__":
    #runs main once (initializes paramters,creates boardframe etc)
    game = Game()
    #loops the game
    while True:
        game.game_loop()