# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 20:05:00 2019

@author: vasto
"""

class Node(object):
   item = -1
   next = None

   def __init__(self, item, next):
       self.item = item
       self.next = next
       
def bubblesort(LL):
   temp = LL
   Sorted = True
   while Sorted != True:
       temp = LL
       Sorted == True
       while temp is not None :
           if temp.item <= temp.next.item:
               Sorted  == False
               tempNode = temp.item
               temp.item = temp.next.item
               temp.next.item = tempNode
           temp = temp.next
   while temp is not None :
       print(temp.item)
       temp = temp.next
       
def readfile(textfile, textfile2):
    file = open(textfile,'r')
    file2 = open(textfile2,'r')
    lines = []
    LL = None
    for i in file:
        lines.append(i)
    for i in file2:
        lines.append(i)
    for i in range(len(lines)):
        LL = Node(int(lines[i]), LL)
    return LL
        
def solution1(LL):
    
    arrList = []
    duplicates =[]
    temp = LL
    while temp is not None:
        arrList.append(temp.item)
        temp = temp.next
        
        
    for i in range(len(arrList)):
        for j in range(i+1,len(arrList)):
            if arrList[i] == arrList[j] and arrList[i] not in duplicates:
                duplicates.append(arrList[i])
    return duplicates

    

LL  = readfile("activision2.txt", "vivendi2.txt")      
print(solution1(LL))
bubblesort(LL)
    