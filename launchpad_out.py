import random
import threading
import time



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
        # self.s1_0()
        # self.lp.LedCtrlRaw(201, 0, 3)
        # turn on launchpad top active buttons

    def chaos_off(self):
        for i in range(18,82,9):
            self.lp.LedCtrlRawByCode(i, 72)
        for i in range(11,92,11):
            self.lp.LedCtrlRawByCode(i, 72)
    # def chaos(self,no,col):
    #     self.lp.LedCtrlRawByCode(no,col)
    #     timer = threading.Timer(0.7,lambda : self.lp.LedCtrlRawByCode(no, 0))
    #     timer.start()  # after 60 seconds, 'callback' will be called
    def chaos_init(self):
        self.lp.LedCtrlRawByCode(72, 1)

        self.lp.LedCtrlRawByCode(22, 1)

        self.lp.LedCtrlRawByCode(77, 1)

        self.lp.LedCtrlRawByCode(27, 1)
    def chaos(self,col,move):
        # for i in range(22,79,50):
        #     self.lp.LedCtrlPulseByCode(i,col)
        #     self.lp.LedCtrlPulseByCode(i+5, col)


        for i in range(11,89,10):
            self.lp.LedCtrlRawByCode(i+move,col)

    def chaos_AAA(self, col,move):
        # move=random.randrange(0,6)
        for i in range(11, 89, random.randrange(1,10)):
            self.lp.LedCtrlRawByCode(i + move, col)

    def chaos_light(self, no, col):
        self.lp.LedCtrlRawByCode(no, col)


        # for i in range(33, 39):
        #     self.lp.LedCtrlRawByCode(i,col)
        # timer = threading.Timer(0.1, lambda: show(i))
        # timer.start()



    def fx_off(self):
        for i in range(0,121,17):
            self.lp.LedCtrlRaw(i, 3,0)
        for i in range(7,113,15):
            self.lp.LedCtrlRaw(i, 3,0)
    def fx(self,no,t):
        self.lp.LedCtrlRaw(no,3,0)
        if t:
            timer = threading.Timer(0.7,lambda : self.lp.LedCtrlRaw(no, 0,0))
            timer.start()  # after 60 seconds, 'callback' will be called

    def light_s(self, no, R,G):
        self.lp.LedCtrlRaw(no, R,G)

    def light(self, no, col):
        self.lp.LedCtrlRawByCode(no, col)

    def s1_0(self):
        # self.lp.LedCtrlPulseByCode(48,127)
        self.lp.LedCtrlPulseByCode(71, 72)

    def s1_0x(self):
        for i in range(61,82,10):
            self.lp.LedCtrlRawByCode(i,122)
        self.lp.LedCtrlRawByCode(51,109)
    def s1(self):
        self.s1_0x()
        self.lp.LedCtrlPulseByCode(82, 72)
        self.lp.LedCtrlPulseByCode(62, 72)
    def s1_1v1(self):
        self.lp.LedCtrlRawByCode(82, 122)
        self.lp.LedCtrlPulseByCode(62,72)
        self.lp.LedCtrlRawByCode(72, 109)
    def s1_1v2x(self):
        for i in range(61,82,10):
            self.lp.LedCtrlRawByCode(i, 122)
            self.lp.LedCtrlRawByCode(i+1,122)
        for i in range(51,53):
            self.lp.LedCtrlRawByCode(i,109)
    def s1_2(self):
        self.s1_1v2x()
        self.lp.LedCtrlPulseByCode(83,72)
    def s1_2x(self):
        self.s1_1v2x()
        self.lp.LedCtrlRawByCode(83, 122)
        self.lp.LedCtrlRawByCode(73, 109)

    def s1_3(self):
        self.s1_2x()
        self.lp.LedCtrlPulseByCode(63,72)

    def s1_3x(self):
        self.s1_1v2x()
        for i in range(61, 82, 10):
            self.lp.LedCtrlRawByCode(i + 2,122)
        self.lp.LedCtrlRawByCode(53, 109)

    def s1_4(self):
        self.s1_3x()
        self.lp.LedCtrlPulseByCode(84,72)
        self.lp.LedCtrlPulseByCode(64, 72)
    def s1_4x(self):
        self.s1_3x()
        for i in range(61, 82, 10):
            self.lp.LedCtrlRawByCode(i + 3, 122)
        self.lp.LedCtrlRawByCode(54, 109)
        big_no = 81
        for j in range(0,4):
            for i in range(big_no,big_no+4):
                self.lp.LedCtrlRawByCode(i,72)
                time.sleep(0.1)
            big_no=big_no-10

    def s2_0(self):
        self.s1_full()
        self.lp.LedCtrlPulseByCode(75, 67)


    def s2_0x(self):
        self.s1_full()
        for i in range(65, 87, 10):
            self.lp.LedCtrlRawByCode(i, 122)
        self.lp.LedCtrlRawByCode(55, 109)

    def s2_1(self):

        self.s2_0x()
        self.lp.LedCtrlPulseByCode(86, 67)
        self.lp.LedCtrlPulseByCode(66, 67)

    def s2_1v1(self):
        self.lp.LedCtrlRawByCode(86, 122)
        self.lp.LedCtrlPulseByCode(66,67)
        self.lp.LedCtrlRawByCode(76, 109)
    def s2_1v2x(self):
        self.s1_full()
        for i in range(65,87,10):
            self.lp.LedCtrlRawByCode(i, 122)
            self.lp.LedCtrlRawByCode(i+1,122)
        for i in range(55,57):
            self.lp.LedCtrlRawByCode(i,109)
    def s2_2(self):

        self.s2_1v2x()
        self.lp.LedCtrlPulseByCode(87,67)
    def s2_2x(self):
        self.s2_1v2x()
        self.lp.LedCtrlRawByCode(87, 122)
        self.lp.LedCtrlRawByCode(77, 109)

    def s2_3(self):
        self.s2_2x()
        self.lp.LedCtrlPulseByCode(67,67)

    def s2_3x(self):
        self.s2_1v2x()
        for i in range(65, 87, 10):
            self.lp.LedCtrlRawByCode(i + 2,122)
        self.lp.LedCtrlRawByCode(57, 109)

    def s2_4(self):
        self.s2_3x()
        self.lp.LedCtrlPulseByCode(88,67)
        self.lp.LedCtrlPulseByCode(68, 67)
    def s2_4x(self):
        self.s2_3x()
        for i in range(65, 87, 10):
            self.lp.LedCtrlRawByCode(i + 3, 122)
        self.lp.LedCtrlRawByCode(58, 109)
        big_no = 85
        for j in range(0,4):
            for i in range(big_no,big_no+4):
                self.lp.LedCtrlRawByCode(i,67)
                time.sleep(0.1)
            big_no=big_no-10


    def s3_0(self):
        self.s2_full()
        self.lp.LedCtrlPulseByCode(21,13)
        self.lp.LedCtrlPulseByCode(41, 13)
    def s3_0x(self):
        self.s2_full()
        for i in range(21,42,10):
            self.lp.LedCtrlRawByCode(i,122)
        self.lp.LedCtrlRawByCode(11,109)

    def s3_1(self):
        self.s3_0x()
        self.lp.LedCtrlPulseByCode(32, 13)


    def s3_1x(self):
        self.s3_0x()
        for i in range(22,43,10):
            self.lp.LedCtrlRawByCode(i, 122)
        self.lp.LedCtrlRawByCode(12, 109)

    def s3_2(self):
        self.s3_1x()
        self.lp.LedCtrlPulseByCode(33, 13)

    def s3_2x(self):
        self.s3_1x()
        for i in range(23,44,10):
            self.lp.LedCtrlRawByCode(i, 122)
        self.lp.LedCtrlRawByCode(13, 109)

    def s3_3(self):
        self.s3_2x()
        self.lp.LedCtrlPulseByCode(44, 13)

    def s3_3x(self):
        self.s3_2x()
        self.lp.LedCtrlRawByCode(44, 122)
        self.lp.LedCtrlRawByCode(34, 109)

    def s3_4(self):
        self.s3_3x()
        self.lp.LedCtrlPulseByCode(24, 13)
    def s3_4x(self):
        self.s3_3x()
        self.lp.LedCtrlRawByCode(24, 122)
        self.lp.LedCtrlRawByCode(34, 122)
        self.lp.LedCtrlRawByCode(14, 109)
        big_no = 41
        for j in range(0, 4):
            for i in range(big_no, big_no + 4):
                self.lp.LedCtrlRawByCode(i, 13)
                time.sleep(0.1)
            big_no = big_no - 10

    def s4_0(self):
        self.s3_full()
        self.lp.LedCtrlPulseByCode(35, 81)


    def s4_0x(self):
        self.s3_full()
        for i in range(15, 47, 10):
            self.lp.LedCtrlRawByCode(i, 122)
        self.lp.LedCtrlRawByCode(15, 109)

    def s4_1(self):
        self.s4_0x()
        self.lp.LedCtrlPulseByCode(26, 9)
        self.lp.LedCtrlPulseByCode(46, 59)

    def s4_1x(self):
        self.s4_0x()
        for i in range(16, 48, 10):
            self.lp.LedCtrlRawByCode(i, 122)
        self.lp.LedCtrlRawByCode(16, 109)

    def s4_2(self):
        self.s4_1x()
        self.lp.LedCtrlPulseByCode(37, 2)
    def s4_2x(self):
        self.s4_1x()
        for i in range(17, 49, 10):
            self.lp.LedCtrlRawByCode(i, 122)
        self.lp.LedCtrlRawByCode(17, 109)
    def s4_3(self):
        self.s4_2x()
        self.lp.LedCtrlPulseByCode(38, 2)
    def s4_3x(self):

        self.s4_1x()
        big_no0 = 45
        for j in range(0, 4):
            for i in range(big_no0, big_no0 + 4):
                self.lp.LedCtrlRawByCode(i, random.randrange(1,127))
                time.sleep(0.1)
            big_no0 = big_no0 - 10
        big_no = 81
        time.sleep(1)
        self.initPad()
        for j in range(0, 8):
            for i in range(big_no, big_no + 8):
                self.lp.LedCtrlRawByCode(i, 122)
            big_no = big_no - 10



    def s1_full(self):
        big_no = 81
        for j in range(0, 4):
            for i in range(big_no, big_no + 4):
                self.lp.LedCtrlRawByCode(i, 72)
            big_no = big_no - 10
    def s2_full(self):
        self.s1_full()
        big_no = 85
        for j in range(0, 4):
            for i in range(big_no, big_no + 4):
                self.lp.LedCtrlRawByCode(i, 67)
            big_no = big_no - 10
    def s3_full(self):
        self.s2_full()
        big_no = 41
        for j in range(0, 4):
            for i in range(big_no, big_no + 4):
                self.lp.LedCtrlRawByCode(i, 13)
            big_no = big_no - 10
    def extra(self,no,clicked):
        if clicked:
            self.lp.LedCtrlRaw(no, 3,1)
        else:
            self.lp.LedCtrlPulseByCode(no, 109)

