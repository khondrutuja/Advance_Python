# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:19:31 2023

@author: Dell
"""
#IMP list comprehenssion
#it is for code optimaization
#normal lst program
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)
###############################################
#list comprehension    
lst=[num for num in range(0,20)]
print(lst)
###########################################
#add the content in  to the list
names=['data','mama','kaka']
lst=[name.capitalize() for name in names]
print(lst)
########################################
#how to use if statment in list comprehension
#if statment are write at right side of for loop in list comprehension
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)
####################################
#display no  like 00,01,02
#loop inside loop for loop
#initially x=0y=0 then right hand side loop exicute first
 
lst=[f"{x}{y}"for x in range(3) for y in range(3)]
print(lst)
#########################################
#set comprehension
#not use mostly set comprehension, we use mostly list comprehension
# use dectionary comprehension when we use JSON file
set_one={x for x in range(3)}
print(set_one)
#################################################
#Dectionary comprehension squre no display \IMP
dict={x:x*x for x in range(3)}
print(dict)
#########################################
#Generator
#it is another way of creating iterator means iterating like 0,1,2,3
#Generator are implemented using function
#it return multiple value
#insted of writing return keyword in function gerator use "yield" keyword
#tuple comprehention return object
#gen:-object created
#when we are going to use tuple comprehension one object will be created and you can access values of that object using for loop
gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)
########################################
#generator method-next(gen ) method
#it is going to show you out put step by step
gen=(x for x in range(3))
next(gen)
next(gen)
next(gen) # dict,set,list no create object but tuple create object 
#########################################
#function which return multiple value \this function work as a generator
def range_even(end):
    gen=(x for x in range(0,end,2))
    print(gen)
    for num in range(0,end,2): # 
        yield num #yield create multiple value
for num in range_even(6):
    print(num)        
##########################################  
#diffrence bet   tuple as gerator and function as genrator
 # tuple create object and function not create object
 # suppose want multiple value
 #now insted of using for loop we can write our own gerator
gen=range_even(6)
next(gen)
next(gen)
##########################################
#changing generator
#ele* comprases the multiple values
#ele*'*'-converted in to *
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
passwords=["not-good","give'm-pass","00100=100"]
for password in hide(lengths(passwords)):
    print(password)        
############################################################
#Enumerate-same like dictionary
#printing list with index
lst=['milk','egg','bread']
for index in range(len(lst)):
    print(f'{index}{lst[index]}')
###############################################    
#same code can be implemented using enumerate
lst=["milk","Egg","bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index}{item}")
#################################################
import 
 #password picker 
adjectives=['sleepy','slow','smelly','wet','fat','red','orange','yellow','green','blue','purpal','fiuffy','white','proud','brave'] 
#pic out the none
nouns=['apple','ball','dianasor','toster','goat','dragon','hammer','duck','panda']
#pick the words
import random
adjectives = random.choice(adjectives)
nouns = random.choice(nouns)
#select the number
number=random.randrange(0,100)
#select a special character
special_char = random.choice(string.punctuation)
#create new secure password
passwords = adjectives + nouns + str(number) + special_char
print('your new password is:%s'%passwords)    
def lengths(itr):
     for ele in itr:
         yield len(ele)
def hide(itr):
     for ele in itr:
         yield ele*'*'
psw=passwords
for password in hide(lengths(psw)):
     print(password,end='')  
#####################################################
#find all the numbers from 1 to 1000   which is divisible by 7 
div7=[n for n in range(1,1000) if n%7==0]
print(div7)  
##################################################
#find all no from 1 to 1000 that have no 3 in them
lst=[n for n in range(1,1000) if '3' in str(n)]
print(lst)
#################################################
#count the no of spaces in the string
some_string='the slow solid squid swam sumptuously through the slimy swamp'
spaces=[s for s in some_string if s==' ']
print(len(spaces))
#####################################################
#create a list of all consonent in the string
#yellow yaks like yelling and yawing and yesturday they yoled while eating yuki yams
sentence='''yellow yaks like yelling and yawing and yesturday they yoled while eating yuki yams '''
result=[letter for letter in sentence if letter not in 'a,e,i,o,u" "']

print(result)
###############################################
#find the commam no in two list without using tuple or set
list_a=[1,2,3,4]
list_b=[2,3,4,5]
comman=[a for a in list_a if a in list_b]
print(comman)
###################################
# \IMP get only the number in sentence like 
#"In 1984 there were 13 instance of a protest with over 1000"
sentence="In 1984 there were 13 instance of a protest with over 1000"
words=sentence.split()
result=[number for number in words if not number.isalpha()]
print(result)
#isalpha return true if string containe alphabet
############################################
'''
given numbers= range(20),produce a list containing 
the words'even'for the no is even otherwise print odd
'''
#if else condition write left side and only 
#if condition weite on right ##retry

result=[]
for n in range(20):
    if n%2==0:
          result.append('even')
    else:
         result.append('odd')
         print(result)
result=['even' if n%2==0 else 'odd' for n in range(20)]
print(result)        
#######################################
#produce a list of tuple consisting only match
#list_a=[1,2,3,4,5,6,7,8,9],list_b=[]

#assignment try this for same words in two string-
## not exicute
list_a=[1,2,3,4,5,6,7,8,9]
list_b=[2,7,1,12]
result=[(a,b) for a in list_a,(a,b) for b in list_b if a==b]
print(result)
############################
#find all of the words in a string that are less 
#than 4 letter
sentence='on a summer day Ramnath sonar wentswimming in the sun and his red skin stung'
examine = sentence.split()
result=[word for word in examine if len(word)>=4]
print(result)
########################################
#write python program to print a specified list 
#after removing the 0th,4th,and 5th element
# x= value   i= index
color=['Red','Green','White','black','pink','Yellow']
color=[x for (i,x) in enumerate(color)if i not in (0,4,5)]
print(color)
########################################
#write python program that generator function 
#that yields ofcube of no from 1 to n accept n from user 
def cube_generator(n):
    for i in range(1,n +1):
        yield i**3
        
# Accept input from the user
n=int(input("Input a number:"))
#create generator object
cubes = cube_generator(n)
#iterate over generator and print the cube
print("the cube of number from 1 to",n)
for num in cubes:
    print(num)
 #######################
#write python program to implement a generator that 
#generates random no with in given range
import random
def random_number_generator(start,end):
     while True:
         yield random.randint(start,end)
#Accept input from user
start=int(input("input a number:"))
end=int(input("enter the number"))
#create the generator 
random_numbers=random_number_generator(start,end)       
print('random number between ',start,'and',end)
for _ in range(10):
    print(next(random_numbers))
#############################################
    #list comprehension for multidimensional array
 #two [][]-two diamentional
#[][][]-three diamentional
[][][][]-Tensor   
#write a python program to  generate 3*4*6 3D array 
#whose each element is *.
#3-row,4-col,6-col
array=[[['*' for col in range(6)]for col in range(4)] for row in range(3)]    
print(array)
##################################
#write a python program to print the no of specified 
# list after removing even number from it.
num=[7,8,120,25,44,20,27]
num=[x for x in num if x%2!=0]
print(num)
###################################
#by using list comprehensioin
sta1='hello everyone today is monday '
sta2='hello everyone tommorow is holiday'
str1=sta1.split()
str2=sta2.split()
result=[x for x in str1 if x in str2]
print(result)
######################################
