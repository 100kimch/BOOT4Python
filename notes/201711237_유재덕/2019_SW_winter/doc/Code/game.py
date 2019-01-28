import os
import time
import random
sentence=('a','b','c','d','e','f','g') #튜플 자료형으로 문장들 입력

def gotoxy(x,y,str): 
    print ("%c[%d;%df" % (0x1B, y, x),end=str)

class Node:
    def __init__(self,next=None):
        self.data = ''
        self.x=0
        self.y=0
        self.next_node=next
    
    def get_word(self):
        return self.data
    
    def get_x(self):
       self.x=random.randrange(8,26)#게임 크기 대입
  
    def get_y(self):
        self.y=70
        

class rain:     
    def __init__(self):
        self.words=Node()   #초기 노드
        self.root=self.words

    def push_node(self):            #새로운 노드 생성
        next=Node()
        next.data=random.choice(sentence)
        next.get_x()
        next.get_y()
        self.words.next_node=next
        self.words=self.words.next_node

    
    def delete_node(self,input):    #노드 탐색 및 삭제
        pre_node=self.words
        next_node=self.words.next_node
        while next_node:
            if input == next_node.word:
                tmp=next_node.next_node
                pre_node.next_node=tmp
            pre_node=pre_node.next_node
            next_node=next_node.next_node
