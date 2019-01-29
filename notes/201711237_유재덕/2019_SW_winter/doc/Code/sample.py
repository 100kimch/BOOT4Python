import game
import os
import time
import random

rain=game.rain()

def gotoxy(x,y,str): 
    print ("%c[%d;%df" % (0x1B, y, x),end=str)

def print_words():    #출력 함수
    tmp=rain.root
    while tmp.next_node:
        gotoxy(tmp.y,tmp.x,tmp.data)

def change_height():  #y축 하강 함수
    tmp=rain.root
    while tmp.next_node:
        tmp.y-=1

def clear():
    os.system('clear')

clear()
for a in range(10):     #10번 실행
    rain.push_node()    #단어를 push
    print_words()   #좌표에 따라 출력
    change_height() #높이 변경
    time.sleep(2)       #대기