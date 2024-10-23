NUMBER GUESSING GAME WITH PYTHON

import math
import random
num = int(input("Enter a number between 1 and 100:  "))
maxNum = 100
minNum = 0
random_num =  random.randint(minNum, maxNum)
playing = True

while playing == True:
    if num < random_num:
        print("Number is lower!!!")
        num = int(input("Enter a number between 1 and 100:  "))
    elif num > random_num:
        print("Number is higher!!!") 
        num = int(input("Enter a number between 1 and 100:  "))
    else: 
        print("Congratulations, your answer is correct!!!") 
        print(random_num)
        playing = False


