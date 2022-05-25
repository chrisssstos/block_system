#BLOCK//SYSTEM launchpad.py https://github.com/FMMT666/launchpad.py
#Christos Constantinou , 2021
import random
import threading
import time
import tkinter as tk

import rtmidi
import sys

from launchpad_out import Launchpad_Out
from random import  choice

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
print(available_ports)

if available_ports:
    midiout.open_port(8)
else:
    midiout.open_virtual_port("SYS_B")
note_on = [0x90, 60, 112] # channel 1, middle C, velocity 112
note_off = [0x80, 60, 0]

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
        if launchpad.Launchpad().Check(1):
            self.lp = launchpad.LaunchpadMk2()
            if self.lp.Open(1):
                print("Launchpad Mk2")
                mode = "Mk2"
        #CHAOS
        if launchpad.Launchpad().Check(0):
            self.lp_chaos = launchpad.LaunchpadMk2()
            if self.lp_chaos.Open(0):
                print("Launchpad Mk2 CHAOS")
                mode = "Mk2"
        # EFFECT_S
        if launchpad.Launchpad().Check(0):
            self.lp_fx_s = launchpad.Launchpad()
            if self.lp_fx_s.Open(0):
                print("Launchpad S FX")
                mode = "Mk1"
        if mode is None:
            print("Did not find any Launchpads, meh...")
            return
        print("QUIT: Push button 1 , RESET: Push button 2, MODES: RIGHT BAR")
        ###
        self.lp_out= Launchpad_Out(self.lp)
        self.lp_out.s1_0()
        self.lp_chaos_out = Launchpad_Out(self.lp_chaos)
        self.lp_fx_s_out = Launchpad_Out(self.lp_fx_s)
        self.sequence = 0
        self.current = 0
        self.lines = ['Log  //  LP  //  TIME']
        self.start_time = 0
        self.start_once = True

        self.col = 72
        self.chaos_trigger = True
        self.chaos_trigger2 = True
        self.move = 0 - 1
        self.pads=list(range(11,89))
        self.pressed=99
        self.stutters=[22,27,72,77]
        self.chaos_pressed = True
        self.chaos_enable=True
        self.q4_col=False

        self.fx_trigger = True
        self.fx_trigger2 = True
        self.random_light = 11
        self.random_light_fx=1
        self.fxs=[]
        self.fxs_pressed = True
        for i in range(0,10):
            self.fxs.append(i)
        self.fx_enable = True

        self.root = tk.Tk()
        self.root.title('BLOCK // SYSTEM')
        canvas = tk.Canvas(self.root, height=400, width=400, bg="#0013FF")
        # canvas.pack()
        def task(no):
            self.lp_out.initPad()
            self.sequence=no
            print(self.sequence)

        def reset():
            self.lp_out.initPad()
            self.sequence = 0
            note_on = [0x90, 60, 127]
            note_off = [0x80, 60, 0]
            midiout.send_message(note_on)
            midiout.send_message(note_off)

        def current():
            # if self.sequence==0:
            #     self.lp_out.initPad()
            #     self.sequence=-10
            if self.sequence==1 or self.sequence==100:
                self.lp_out.initPad()
                self.lp_out.s1_0x()
                self.sequence=500
            if self.sequence==2:
                self.lp_out.initPad()
                self.lp_out.s1_1v2x()
                self.sequence=500
            if self.sequence==3:
                self.lp_out.initPad()
                self.lp_out.s1_2x()
                self.sequence=500
            if self.sequence==4:
                self.lp_out.initPad()
                self.lp_out.s1_3x()
                self.sequence=500
            if self.sequence==5:
                self.lp_out.initPad()
                self.lp_out.s1_full()
                self.sequence=500
            if self.sequence==6:
                self.lp_out.initPad()
                self.lp_out.s2_0x()
                self.sequence=500
            if self.sequence==7:
                self.lp_out.initPad()
                self.lp_out.s2_1v2x()
                self.sequence=500
            if self.sequence==8:
                self.lp_out.initPad()
                self.lp_out.s2_2x()
                self.sequence=500
            if self.sequence==9:
                self.lp_out.initPad()
                self.lp_out.s2_3x()
                self.sequence=500
            if self.sequence==10:
                self.lp_out.initPad()
                self.lp_out.s2_full()
                self.sequence=500
            if self.sequence==11:
                self.lp_out.initPad()
                self.lp_out.s3_0x()
                self.sequence=500
            if self.sequence==12:
                self.lp_out.initPad()
                self.lp_out.s3_1x()
                self.sequence=500
            if self.sequence==13:
                self.lp_out.initPad()
                self.lp_out.s3_2x()
                self.sequence=500
            if self.sequence==14:
                self.lp_out.initPad()
                self.lp_out.s3_3x()
                self.sequence=500
            if self.sequence==15:
                self.lp_out.initPad()
                self.lp_out.s3_full()
                self.sequence=500
            if self.sequence==16:
                self.lp_out.initPad()
                self.lp_out.s4_0x()
                self.sequence=500
            if self.sequence==17:
                self.lp_out.initPad()
                self.lp_out.s4_1x()
                self.sequence=500
            if self.sequence==18:
                self.lp_out.initPad()
                self.lp_out.s4_2x()
                self.sequence=500

        for i in range(0,19):
            if i in range(0,5):
                self.button_txt="s1_"+str(i)
                self.button_bg="#fc7272"
                self.button_col=i
                self.button_row = 1
            elif i in range(5,10):
                self.button_txt="s2_"+str(i-5)
                self.button_bg = "#90e5fc"
                self.button_col = i
                self.button_row = 1
            elif i in range(10,15):
                self.button_txt="s3_"+str(i-10)
                self.button_bg = "#fcfc9a"
                self.button_col = i-10
                self.button_row = 2
            elif i in range(15,19):
                self.button_txt="s4_"+str(i-15)
                self.button_bg = "#a3ffb7"
                self.button_col = i-10
                self.button_row = 2
            button = tk.Button(self.root, text=self.button_txt, padx=10, pady=10, bg=self.button_bg, command=lambda i=i: task(i))
            # button.pack(side=self.button_side)
            button.grid(row=self.button_row,column=self.button_col)
        def chaos_switch():
            if self.chaos_enable:
                self.chaos_enable=False
            else:
                self.chaos_enable=True
        def fx_switch():
            if self.fx_enable:
                self.fx_enable=False
            else:
                self.fx_enable=True
        self.v=tk.StringVar()
        self.con = tk.StringVar()
        self.fxon = tk.StringVar()
        self.start=False
        label=tk.Label(self.root, bg="#FFFFFF",textvariable= self.v)
        label.grid(row=0,column=0)
        conlabel = tk.Label(self.root, bg="#FFFFFF", textvariable=self.con)
        conlabel.grid(row=0, column=1)
        fxlabel = tk.Label(self.root, bg="#FFFFFF", textvariable=self.fxon)
        fxlabel.grid(row=0, column=2)
        reset = tk.Button(self.root, text="reset", padx=10, pady=10, bg="#FFFFFF", command=reset)
        reset.grid(row=1,column=13)
        # reset.pack()
        current = tk.Button(self.root, text="current state", padx=10, pady=5, bg="#FFFFFF", command=current)
        current.grid(row=2, column=13)
        chaos_on = tk.Button(self.root, text="chaos switch", padx=10, pady=5, bg="#FFFFFF", command=chaos_switch)
        chaos_on.grid(row=1, column=14)
        fx_on = tk.Button(self.root, text="fx switch", padx=10, pady=5, bg="#FFFFFF", command=fx_switch)
        fx_on.grid(row=2, column=14)
        # current.pack()



#game loop
    def game_loop(self):
        self.root.update()
        self.v.set(self.sequence)
        self.con.set("CS:"+ str(self.chaos_enable))
        self.fxon.set("FX:" + str(self.fx_enable))
        events = self.lp.ButtonStateRaw()
        if events == [71, 127]:
            if self.sequence==0:
                self.lp_out.s1_0x()
                # self.lp_out.extra(51,self.start)
                self.sequence = self.sequence + 100
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                midiout.send_message(note_on)
                midiout.send_message(note_off)

        # if events == [51, 127] and self.sequence==100:
        #         self.start=not self.start
        #         self.lp_out.extra(events[0],self.start)
        #         note_on = [0x90, events[0], 127]
        #         note_off = [0x80, events[0], 0]
        #         midiout.send_message(note_on)
        #         midiout.send_message(note_off)
        if self.sequence == 0:
            self.lp_out.s1_0()
        if self.sequence==1 or self.sequence==101:
            if self.sequence==1:
                self.lp_out.s1()
            if events == [82, 127] and self.sequence==1:
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                self.lp_out.s1_1v1()
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.sequence = self.sequence + 100

            if events == [62, 127] and (self.sequence==1 or self.sequence==101):
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                self.lp_out.s1_1v2x()
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.sequence = self.sequence + 101
        if self.sequence == 2:
            self.lp_out.s1_2()
            if events == [83, 127]:
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                self.lp_out.s1_2x()
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.sequence = self.sequence + 200
        if self.sequence == 3:
            self.lp_out.s1_3()
            if events == [63, 127]:
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                self.lp_out.s1_3x()
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.sequence = self.sequence + 300

        if self.sequence == 4:
            self.lp_out.s1_4()
            if events == [84, 127] or events == [64, 127]:
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.lp_out.s1_4x()
                self.sequence = self.sequence + 400
        if self.sequence == 5:

            self.lp_out.s2_0()
            if events == [75, 127]:
                self.col = 67
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                self.lp_out.s2_0x()
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.sequence = self.sequence + 400

        if self.sequence == 6 or self.sequence == 106:
            if self.sequence == 6:
                self.lp_out.s2_1()
            if events == [86, 127] and self.sequence == 6:
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                self.lp_out.s2_1v1()
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.sequence = self.sequence + 100
            if events == [66, 127] and (self.sequence==6 or self.sequence==106):
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                self.lp_out.s2_1v2x()
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.sequence = self.sequence + 101

        if self.sequence == 7:
            self.lp_out.s2_2()
            if events == [87, 127]:
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                self.lp_out.s2_2x()
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.sequence = self.sequence + 200

        if self.sequence == 8:
            self.lp_out.s2_3()
            if events == [67, 127]:
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                self.lp_out.s2_3x()
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.sequence = self.sequence + 300

        if self.sequence == 9:
            self.lp_out.s2_4()
            if events == [88, 127] or events == [68, 127]:
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.lp_out.s2_4x()
                self.sequence = self.sequence + 400


        if self.sequence == 10:

            self.lp_out.s3_0()
            if events == [21, 127] or events == [41, 127]:
                self.col = 13
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.lp_out.s3_0x()
                self.sequence = self.sequence + 500

        if self.sequence == 11:
            self.lp_out.s3_1()
            if events == [32, 127]:
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                self.lp_out.s3_1x()
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.sequence = self.sequence + 600

        if self.sequence == 12:
            self.lp_out.s3_2()
            if events == [33, 127]:
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                self.lp_out.s3_2x()
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.sequence = self.sequence + 700

        if self.sequence == 13:
            self.lp_out.s3_3()
            if events == [44, 127]:
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                self.lp_out.s3_3x()
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.sequence = self.sequence + 800

        if self.sequence == 14:
            self.lp_out.s3_4()
            if events == [24, 127]:
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.sequence = self.sequence + 900
                self.lp_out.s3_4x()

        if self.sequence == 15:
            self.lp_out.s4_0()
            if events == [35, 127]:
                self.col = 81
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                self.lp_out.s4_0x()
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.sequence = self.sequence + 1000

        if self.sequence == 16:
            self.lp_out.s4_1()
            if events == [26, 127] or events == [46, 127]:
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.lp_out.s4_1x()
                self.sequence = self.sequence + 1100

        if self.sequence == 17:
            self.lp_out.s4_2()
            if events == [37, 127]:
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                self.lp_out.s4_2x()
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.sequence = self.sequence + 1200

        if self.sequence == 18:
            self.lp_out.s4_3()
            if events == [38, 127]:
                note_on = [0x90, events[0], 127]
                note_off = [0x80, events[0], 0]
                midiout.send_message(note_on)
                midiout.send_message(note_off)
                self.sequence = self.sequence + 1300
                self.fx_enable=False
                self.chaos_enable=False
                self.lp_out.s4_3x()
        #close/reset
        # if events == [200, True]:
        #     self.lp_out.closePad()
        # if events == [201, True]:
        #     self.lp_out.initPad()
        #     self.sequence = 0
        #     note_on = [0x90, 60, 127]
        #     note_off = [0x80, 60, 0]
        #     midiout.send_message(note_on)
        #     midiout.send_message(note_off)

        # CHAOS LAUCHPAD
        events_chaos = self.lp_chaos.ButtonStateRaw()

        if self.sequence in range(0,4):
            self.col = 72
            self.q4_col = False
        elif self.sequence in range(6,10):
            self.col = 67
            self.q4_col = False
        elif self.sequence in range(11, 14):
            self.col = 13
            self.q4_col = False
        elif self.sequence in range(16, 20):
            self.q4_col=True

        if self.move>6:
            self.move=-1

        if self.sequence==0:
            self.lp_chaos_out.initPad()

        if self.sequence > 0 and self.chaos_enable:
            if self.chaos_trigger:
                self.lp_chaos_out.initPad()
                self.lp_chaos_out.chaos_init()
                if self.chaos_trigger2:
                    self.move=self.move+1
                else:
                    self.move = self.temp_chaos
                    self.lp_chaos_out.chaos_light(self.pressed,1)
                    self.lp_chaos_out.chaos_AAA(self.col, self.move)

                self.temp_chaos = self.move
                if self.chaos_trigger2:
                    self.lp_chaos_out.chaos(self.col,self.move)
                self.chaos_trigger = False

                def chaos_on(t):
                    if self.q4_col:
                        self.col=self.col+1
                        if self.col>127:
                            self.col=1
                    self.chaos_trigger = t

                timer = threading.Timer(0.2, lambda: chaos_on(True))
                timer.start()
            if len(events_chaos) == 2 and events_chaos[1]==127 and self.chaos_pressed==True and (events_chaos[0]==22 or events_chaos[0]==27 or events_chaos[0]==72 or events_chaos[0]==77) :
                self.chaos_trigger2 = False
                self.lp_chaos_out.chaos_light(events_chaos[0],1)
                self.pressed=events_chaos[0]
                if self.pressed==22:
                    self.stutter = 0
                elif self.pressed == 72:
                    self.stutter = 1
                elif self.pressed==27:
                    self.stutter = 2
                elif self.pressed==77:
                    self.stutter = 3
                # self.random_stutter = random.randint(0, 3)
                note_on = [0x91, self.stutters[self.stutter], 127]
                midiout.send_message(note_on)
                self.chaos_pressed = False
            if events_chaos == [self.pressed,0] and (self.pressed==22 or self.pressed==27 or self.pressed==72 or self.pressed==77):
                self.chaos_pressed = True
                self.chaos_trigger2 = True
                note_off = [0x91, self.stutters[self.stutter], 127]
                midiout.send_message(note_off)
        elif self.chaos_enable==False:
            self.lp_chaos_out.initPad()
            self.lp_chaos_out.chaos_off()
            if self.chaos_pressed==False:
                self.chaos_pressed = True
                self.chaos_trigger2 = True
                note_off = [0x91, self.stutters[self.stutter], 127]
                midiout.send_message(note_off)













        # FX_S LAUCHPAD

        events_fx = self.lp_fx_s.ButtonStateRaw()

        def ran(*r):
            num = []
            for n in r:
                num += [m for m in range(n[0], n[1] + 1)]
            return choice(num)


        if self.fx_enable:
            if self.fx_trigger and self.sequence>0:
                self.lp_fx_s_out.initPad()
                # self.random_light_fx=0
                if self.fx_trigger2:
                    self.random_light_fx = ran((0, 7), (16, 23), (32, 39), (48, 55), (64, 71), (80, 87), (96, 103),
                                            (112, 119))
                else:
                    self.random_light_fx=self.temp
                    self.lp_fx_s_out.light_s(self.random_light_fx, 0, 3)
                self.temp=self.random_light_fx
                if self.fx_trigger2:
                    self.lp_fx_s_out.fx(self.random_light_fx,self.fx_trigger2)
                self.fx_trigger = False

                def fx_on(t):
                    self.fx_trigger = t
                timer = threading.Timer(0.7, lambda: fx_on(True))
                timer.start()



            if events_fx == [self.random_light_fx, True] and self.fxs_pressed:
                self.fx_trigger2=False
                self.lp_fx_s_out.light_s(events_fx[0],3,3)
                self.random_fx=random.randint(5, 9)
                note_on = [0x92, self.fxs[self.random_fx], 127]
                midiout.send_message(note_on)
                self.fxs_pressed = False
            if events_fx == [self.random_light_fx, False]:
                self.fx_trigger2=True
                self.fxs_pressed = True
                note_off = [0x92, self.fxs[self.random_fx], 127]
                midiout.send_message(note_off)
        elif self.fx_enable==False:
            self.lp_fx_s_out.initPad()
            self.lp_fx_s_out.fx_off()
            if self.fxs_pressed==False:
                self.fxs_pressed = True
                self.fx_trigger2 = True
                note_off = [0x92, self.fxs[self.random_fx], 127]
                midiout.send_message(note_off)

        #LOGGING
        if self.sequence>0 and self.start_once:
            self.start_time = time.time()
            self.start_once = False
        elif self.start_once:
            self.start_time = time.time()

        if len(events)==2 and events[1]==127:
            self.pressedtime=time.time()-self.start_time
            self.lines.append("P    //  BS  //  "+ str(self.pressedtime))
        elif len(events)==2 and events[1]==0:
            self.releasedtime=time.time()-self.start_time
            if self.releasedtime-self.pressedtime>1.0:
                self.lines.append("PP    //  BS  //  " + str(time.time() - self.start_time))

        if len(events_chaos)==2 and events_chaos[1]==127:
            self.pressedtimeC = time.time() - self.start_time
            self.lines.append("P    //  CS  //  "+ str(time.time()-self.start_time))
        elif len(events_chaos)==2 and events_chaos[1]==0:
            self.releasedtimeC = time.time() - self.start_time
            if self.releasedtimeC - self.pressedtimeC > 1.0:
                self.lines.append("PP    //  CS  //  " + str(time.time() - self.start_time))

        if len(events_fx)==2 and events_fx[1]==True:
            self.pressedtimeF = time.time() - self.start_time
            self.lines.append("P    //  FX  //  "+ str(time.time()-self.start_time))
        elif len(events_fx)==2 and events_fx[1]==False:
            self.releasedtimeF = time.time() - self.start_time
            if self.releasedtimeF - self.pressedtimeF > 1.0:
                self.lines.append("PP    //  FX  //  " + str(time.time() - self.start_time))
        with open('log.txt', 'w') as f:
            for line in self.lines:
                f.write(line)
                f.write('\n')



if __name__ == "__main__":
    #runs main once (initializes paramters,creates boardframe etc)
    game = Game()
    #loops the game
    while True:
        game.game_loop()

