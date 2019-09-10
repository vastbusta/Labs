# -*- coding: utf-8 -*-
"""
Author: Ruben Bustamante
Instructor: Diego Aguirre
TA: Gerardo Barraza
Course: CS 2302
Assigment: Lab 1B: crack passwords using recursion
Date of last modification: 09/09/2019

"""
import hashlib


def hash_with_sha256(str):
    
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def brute_force(current, unused, Min, Max):
    
    lines = {} # empty set
    with open('password_file.txt') as text_file:# reads file
        
        for file in text_file:
            lines=(file.strip().split(","))# splits text file into a set
    
    passWords =' ' 
    hashed = ''
    
    if len(unused)==0: # base case
        
        return current # return current set of strings
    
    for item in unused:
        
        new_curr = current.copy()# copy of set
        new_unused = unused.copy()# copy rest of the set
        new_curr.append(item)# adding the numbers to new set
        new_unused.remove(item)#popping the used digits
        
        if len(new_curr) >= Min or len(new_curr)<=Max:
            
            passWords = new_curr
            hashed  = hash_with_sha256( str(passWords)+lines[2])
            print("generating: " ,hashed)  
                
            if hashed==lines[2]:# if two values match
                print("Found", hashed) # print user name and pw
                     
        brute_force(new_curr, new_unused,Min, Max)# recurive call
            
def main():
    List = [0,1,2,3,4,5,6,7,8,9]#list of nummvers
    my_set = []# empay list
       
    print(brute_force(my_set, List,3,7))
   
    
main()