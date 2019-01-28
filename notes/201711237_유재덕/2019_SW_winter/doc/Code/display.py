import os
import time
import random
import getpass
People_Num=20
People=[]
   
class Person:
   def __init__(self,id,password,score):
      self.id=id
      self.password=password
      self.score=score
   def getId(self):
      return self.id
   def getPassword(self):
      return self.password
      
def gotoxy(x,y,str): 
    print ("%c[%d;%df" % (0x1B, y, x),end=str) 
  
def menu():
   gotoxy(50,17,"-                       1. Game Start                           -")
   gotoxy(50,19,"-                       2. Rank                                 -")
   gotoxy(50,20,"-                                                               -")
   gotoxy(50,21,"-                       3. Finish                               -")
   gotoxy(73,26,"Choose  Menu:")
   menu=input()
   return menu
def clear():
   os.system('clear')
def main():
         
         login()
         num = menu()
         if num == "1":
            game_start()
         
         elif num == "2":
            show_rank()
         elif num == "3":
            print("게임을 종료합니다...")
            return
         else:
            gotoxy(80,26,"잘못 입력하셨습니다")
            time.sleep(1)

def game_start():
   clear()
   korean=['전적으로 제 안목을 믿으셔야 합니다','당신은 너무 조바심을 내는 것 같아요','보이는 게 전부가 아니라는거','그거 열등감이고 피해의식이야','교육을 하신게 아니라 사육을 하셨군요']
   english=['Have to believe entirely my eye',"You're so anxious I guess","'It's not all that you see", "That's an inferiority complex",'Education to farming, not you']
   num1=len(korean)
   for i in range(0,num1):
      gotoxy(10,6+i*4,korean[i])
      gotoxy(10,8+i*4,english[i])
   time.sleep(5)
   
   
      
def print_words():
   game_words=['entirely','fully','completely','totally','eager','intent','inferiority','complex']
   num2=len(game_words)
   for i in range(0,num2): 
      rand_x=random.randint(0,40)
      rand_y=random.randint(0,20)
      gotoxy(60+rand_x,10+rand_y,game_words[i])
      time.sleep(1)
      
      
def login():
   gotoxy(46,8,"■■■  ■   ■ ■    ■   ■■■   ■   ■■■ ■■■ ■     ■■■ ")
   gotoxy(46,9,"■      ■  ■    ■■     ■     ■  ■ ■       ■   ■     ■")
   gotoxy(46,10,"■■■  ■■       ■      ■     ■■■ ■■■   ■   ■     ■■■ ")
   gotoxy(46,11,"    ■  ■  ■     ■      ■     ■  ■     ■   ■   ■     ■")
   gotoxy(46,12,"■■■  ■   ■    ■      ■■■ ■  ■ ■■■   ■   ■■■ ■■■ ")
   gotoxy(50,14,"-----------------------------------------------------------------")
   gotoxy(50,15,"-                                                               -")
   gotoxy(50,16,"-                                                               -")
   gotoxy(50,17,"-                                                               -")
   gotoxy(50,18,"-                                                               -")
   gotoxy(50,19,"-                                                               -")
   gotoxy(50,20,"-                                                               -")
   gotoxy(50,21,"-                                                               -")
   gotoxy(50,22,"-                                                               -")
   gotoxy(50,23,"-                                                               -")
   gotoxy(50,24,"-----------------------------------------------------------------")
   People.append(Person("hello","1234",0))
   num=len(People)
   flag=1
   while flag:
      gotoxy(70,17,"     Id:  ")
      id=input()
      num=len(People)
      for i in range(0,num):
         if(People[i].getId()==id):
            usernum=i
            gotoxy(70,20,"Password: ")
            password=input()
            if(password==People[usernum].getPassword()):
               flag=0
               break
            else:
               gotoxy(70,17," "*20)
               time.sleep(1)
               gotoxy(70,20," "*20)
               flag=1
         elif(i==num-1):
            gotoxy(65,17,"No Id found. Sign Up?(yes/no) ")
            answer=input()
            if(answer=="yes"):
               signup()
            elif(answer=="no"):
               gotoxy(65,17," "*20)
               continue
      
      
def signup():
      gotoxy(65,17,"            Sign Up                        ")
      gotoxy(70,20,"ID:        ")
      id=input()
      gotoxy(70,22,"Password:     ")
      password=input()
      People.append(Person(id,password,0))
      gotoxy(65,17," "*20)
      gotoxy(70,20," "*20)
      gotoxy(70,22," "*20)
main()