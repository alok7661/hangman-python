#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 17:44:18 2021

@author: alok
"""
import os.path
import pandas as pd
import random
from Hangman_parts import parts #to call teh Hangman_parts file
from Hangman_words import words

    
picked_l = random.choice(words)

picked = picked_l.upper()

name = input('Enter your name:').upper()

score = 0
print( 'Hi',name,', Welcome to the Hangman game.')
print('Guess a name with two words,',len(picked) ,'letters including space.Type space to see the space position.')
right = ['_'] * len(picked)
wrong = []
def update():
    for i in right:
        print(i, end = ' ')
    print()
    
update()
parts(len(wrong))

def winners():
     
    df = pd.read_csv('/tmp/scorerecordAlo.txt', sep=",")
    group = df.groupby("name")["score"].sum()
    print(group.head(10))
    
 #Main loop for the game   
    
if __name__ == "__main__":

    while True:
        print("================")
        guess = input("Guess a letter: ").upper()
        
        if guess in picked:
            index = 0
            for i in picked:
                if i == guess:
                    right[index] = guess
                index += 1
            update() 
            print('Right guess!')
            
        else:
            if guess not in wrong:
                wrong.append(guess)
                parts(len(wrong))
                print('Wrong guess!')
            else:
                print('You already guess it.')
            print(wrong)
        if len(wrong) > 4:
            print('You lost the game.')
            print('Actual word is : ', picked)
            winners()
            break
        if '_' not in right:
            if os.path.exists('/tmp/scorerecordAlo.txt'):
                print("file exits")
            else:
                f=open('/tmp/scorerecordAlo.txt', 'w')
                f.write('name' + ',' + 'score'+ '\n')
                f.close()
            print('You win.')
            f = open('/tmp/scorerecordAlo.txt',"a", newline="")
            score = score + 10
            f.write(name +','+ str(score)+'\n')
            f.close()
            winners()
           
            break



