"""
Author:Ruben Bustamante
Instructor: Diego Aguirre
TA:Gerarado Barraza
Course: CS 2302
Assigment: Lab 2A
Date of last modification: 9/23/2019
Purpose of program: use linek list to find dupllicates in text file of ids
"""
import random
import time

class Node(object):
   item = -1
   next = None

   def __init__(self, item, next):
       self.item = item
       self.next = next
       
#function that read file and stores in a a linked list
def readfile(textfile, textfile2):
    
    file = open(textfile,'r')
    
    file2 = open(textfile2,'r')
    
    List_of_Ids = [] # empty list for ids
    
    LL = None #empty linked list
    
    for i in file:
        
        List_of_Ids .append(i)
        
    for i in file2:
        
        List_of_Ids .append(i)
        
    # store in the  Linked list    
    for i in range(len(List_of_Ids)):
        
        LL = Node(int(List_of_Ids [i]),LL)
        
    return LL

#mergesort function
def mergesort(arrList):
    
    merged_arr = []
    
    if len(arrList)<=1: #base case
        
        return arrList
    
    mid= len(arrList)//2 #mid point  of the list
    
    left = mergesort(arrList[:mid]) #left side of the mid point
    
    right = mergesort(arrList[mid:])#right side of the mid point

    l = 0 # left side index
    r = 0 # right side index
    
    while l <len(left) and r < len(right):
        
        if left[l] < right[r]:
            
            merged_arr.append(left[l])
            
            l +=1 # updating the left side counter
            
        else:
            merged_arr.append(right[r])
            
            r +=1 #updating the right side counter
            
    merged_arr += left[l:]#recusive call for the left sie
    
    merged_arr += right[r:]#recursive call for the right sie

    return merged_arr

def bubblesort(arrList):
    
    for i in range(len(arrList)):
            
            for j in range(0,len(arrList)-i-1):
                
                if arrList[j] > arrList[j+1]:
                    
                    arrList[j], arrList[j+1] = arrList[j+1], arrList[j]
                    
    return arrList  
 
# solution 1 that uses nest for loops to locate duplicates       
def solution1(LL):
    
    arrList = []
    duplicates =[]
    #temp var to store the Linked List(LL)
    temp = LL
    
    while temp is not None:
        
        arrList.append(temp.item)
        
        temp = temp.next
        
        
    for i in range(len(arrList)):
        
        for j in range(i+1,len(arrList)):
            
            if arrList[i] == arrList[j]:
                
                duplicates.append(arrList[i])
                
    if len(duplicates)==0:
      print('no duplicates')
    else:
        print('duplicates', duplicates)

#solutions 2 uses bublle sort to find duplicates
def solution2(LL):
    
    #temp var to store the Linked List(LL)
    temp =LL
    arrList = []
    
    while temp is not None:
        
        arrList.append(temp.item)
        
        temp = temp.next
        
    #print the sorted list
    print(bubblesort(arrList),end="")
    
    my_list = bubblesort(arrList)
    
    duplicates =[]
    
    #finds the duplicates
    for i in range(len(my_list)):
        
        for j in range(i+1,len(my_list)):
            
            if my_list[i] == my_list[j]:
                
                duplicates.append(my_list[i])
                
    if len(duplicates)==0:
      print('no duplicates')
    else:
        print("============================","duplicates", duplicates)
def solution3(LL):
    
    #temp var to store the Linked List(LL)
    temp =LL

    arrList = []
    
    
    while temp is not None:
        arrList.append(temp.item)
        temp = temp.next
        
    #megersort function that sort the list
    print(mergesort(arrList))
    
    duplicates=[]
    my_list = mergesort(arrList)
    
    #finds the duplicates
    for i in range(len(my_list)):
        
        for j in range(i+1,len(my_list)):
            
            if my_list[i] == my_list[j]:
                
                duplicates.append(my_list[i])
                
    if len(duplicates)==0:
      print('no duplicates')
    else:
        print("===============================","duplicates", duplicates)
                
        
    
    
# solution 4 uses boolean array to find duplicates 
def solution4(LL):
    
    #temp var to store the Linked List(LL)
    temp =LL 
    arrList =[]
    
    #boolean list with 6001 indices
    seen = [False]*500001
    
    while temp is not None:
        
        arrList.append(temp.item)
        
        temp =temp.next
        
    for i in arrList:
        
        if seen[i] is True:
            
            print('List contains duplicates',)
            
            return
        
        seen[i]=True
        
    print('no duplicates in the list')
    
def test_case(num):
    LL2=None
    num = num+1
    arrlist=[]
    
    for i in range(num):
        arrlist.append(random.randrange(1,num,1))
        
    for i in range(len(arrlist)):
        LL =Node(arrlist[i],LL2)
  
    return LL

def main():
    
    #Linked List
    LL  = readfile("activision.txt", "vivendi.txt") 
    #test  case
    LL2 = test_case(5000)   
    LL3 = test_case(10000)
    LL4 = test_case(100000)
    
    start_time = time.time()
    print('solution 1')
    print("Duplicates IDs")
    solution1(LL)
    print('time:', (time.time()-start_time))
    print("===================================================")
    
    start_time2 = time.time()
    print("bubblesort")
    solution2(LL)
    print('time:', (time.time()-start_time2))
    print("===================================================")
    
    start_time3 = time.time()
    print("mergesort")
    solution3(LL)
    print('time:', (time.time()-start_time3))
    print("===================================================")
    
    start_time4 = time.time()
    solution4(LL)
    print('time:', (time.time()-start_time4))
main()