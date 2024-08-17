#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 22:21:04 2024

@author: nusratalam
This project is to show how nesting is done

"""


name=input ("Please type your name:")
print ("welcome",name,"to your adventure world")

answer=input("you are on a dirt road, it has come to an end and you can go left or right which way would you like to go? ").lower()

if answer == "left":
    answer = input("You came to a river, you can walk around it or swim accross it. Choose your verdict. ")
    if answer =="swim":
        print("You have to now swim accross")
    elif answer =="walk":
        print("you have to now walk")
    else: 
        print("not a valid option, you loose")
        

elif answer == "right":
     answer = input("This path has a bridge but you are unsure of crossing it, do you want to go back (yes/no?)")
     if answer=="yes":
         print("If you are going back please be careful of crossing the bridge")
     elif answer=="no":
         print("Well now you my friend loose this battle")
     else:
         print("not a valid option you loose my friend, see you later ")
         
        
        

 
   
      
      
    
    
 
    
