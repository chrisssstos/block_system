import math
from check import Check
import copy
import random
class AI_move:
    def __init__(self):

        self.check = Check()
        self.avail_move=[]
        self.diction={}
        self.moves = [0,3,6,
                      48, 51, 54,
                      96, 99, 102
                      ]
#ai move
    def ai_move(self,X,O,dif):
        best_score= -math.inf
        move=None
        bombMove=None
        for i in self.avail_move:
            nextA=copy.deepcopy(self.avail_move)
            O.append(i)
            #bombmove is used on the easy difficulty to check if the final move wins
            if Check.checkWIN(self.check, O):
                bombMove=i
            nextA.remove(i)
            score=self.minimax(X,O,nextA,0,False,-math.inf,math.inf)
            # print(i,":",score)
            O.remove(i)
            nextA.append(i)
            if score>best_score:
                best_score=score
                move=i
        #return best move :minmax
        if dif==1:
            return move
        #easy AI: first move always random, final move always optimal, inbetween has 33% chance of choosing randomly
        elif dif==2:
            if O==[]:
                return self.avail_move[random.randrange(0,len(self.avail_move))]
            if bombMove!= None:
                return bombMove
            else:
                ranMove=[move,move,self.avail_move[random.randrange(0,len(self.avail_move))]]
                return random.choice(ranMove)

#minmax algorith with alpha beta pruning
    def minimax(self,X,O,avail_move,depth,isMax,alpha,beta):
        if Check.checkWIN(self.check,X):
            skore=-10
            return skore
        if Check.checkWIN(self.check,O):
            skore=10
            return skore
        if len(X)==5 or len(O)==5:
            skore=0
            return skore
        else:
            if isMax:
                best_score = -math.inf
                for i in avail_move:
                    nextA= copy.deepcopy(avail_move)
                    nextO = copy.deepcopy(O)
                    nextO.append(i)
                    nextA.remove(i)
                    score = self.minimax(X,nextO,nextA,depth+1,False,alpha,beta)
                    nextO.remove(i)
                    nextA.append(i)
                    if score > best_score:
                        best_score = score
                    alpha= max(alpha,score)
                    if beta<=alpha:
                        break
                return best_score
            else:
                best_score = math.inf
                for i in avail_move:
                    nextX = copy.deepcopy(X)
                    nextA = copy.deepcopy(avail_move)
                    nextX.append(i)
                    nextA.remove(i)
                    score = self.minimax(nextX,O,nextA,depth+1,True,alpha,beta)
                    nextX.remove(i)
                    nextA.append(i)
                    if score < best_score:
                        best_score = score
                    beta= min(score,beta)
                    if beta<=alpha:
                        break
                return best_score