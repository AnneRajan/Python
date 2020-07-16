# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 09:00:21 2020

@author: Rajan
"""

import random
print("This is a dice rolling simulator:")
x="y"

while x=="y":
    num = random.randint(1,6)
    if(num==1):
        print("------")
        print("|    |")
        print("| O  |")
        print("|    |")
        print("|    |")
        print("------")
    elif(num==2):
        print("------")
        print("|    |")
        print("|O  O|")
        print("|    |")
        print("|    |")
        print("------")
    elif(num==3):
        print("------")
        print("|    |")
        print("|O  O|")
        print("| O  |")
        print("|    |")
        print("------")
    elif(num==4):
        print("------")
        print("|    |")
        print("|O  O|")
        print("|O  O|")
        print("|    |")
        print("------")
    elif(num==5):
        print("------")
        print("|    |")
        print("|O  O|")
        print("| O  |")
        print("|O  O|")
        print("------")
    elif(num==6):
        print("------")
        print("|     |")
        print("|O O O|")
        print("|     |")
        print("|O O O|")
        print("------")
    x=input("press y to continue: ")
        
        
        
    
    
