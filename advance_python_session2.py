# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 09:17:39 2023

@author: Dell
"""

#zip function \IMP
#zip function is use to integrate entity
name=['kaka','mama','dada']
info=[1990,1798,7868]
for nm,inf in zip(name,info):
    print(nm,inf)
#############################    
#drowback of zip function
name=['kaka','mama','data','baba','dada']
info=[1990,1798,7868]
for nm,inf in zip(name,info):
    print(nm,inf)
######################################
#zip_longest
#remove drowback of zip function
from itertools import zip_longest
name=['kaka','mama','data','baba','dada']
info=[1990,1798,7868]
for nm,inf in zip_longest(name,info):
     print(nm,inf)   
######################################     
#use fillvalue insted of None
#fill value=0 when we use CSV file at that time some data value is 0 so we dont want that vale
from itertools import zip_longest
name=['kaka','mama','data','baba','dada']
info=[1990,1798,7868]
for nm,inf in zip_longest(name,info,fillvalue=0):
     print(nm,inf)
##############################################
#use all(),if all the values are true  then it will produce output else useless
lst=[2,3,6,8,9]
if all(lst):
    print("all values are true")
else:
    print("useless")
##################################
lst=[0,2,3,6,8,9]
if all(lst):
   print("all values are true")
else:
       print("useless") 
############################################
#use of any, if any one is positive
#any check any non zero value
lst=[0,0,0,-8,0]
if any(lst):
    print('it has some value')
else:
    print('useless')  
##############################################
#all function is exactly oposite to count
lst=[0,0,0,0,0]
if any(lst):
    print('it has some value')
else:
    print('useless')
################################ 
#count=it is use for measure the entity
#it is use in IOT application
#it is also ues in image processing
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))   
######################################
#start from 1
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter)) 
#######################################
#cycle
#suppose you have repeated tasks  to be done, then can use this method
import itertools
instructions=("eat","code","sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)
#######################################
#reapet
#repeat()
from  itertools import repeat
for msg in repeat("keep pationts",times=3):
    print(msg)
########################################
#combination-way of selecting items from collection
#permutation=arranging all the members of set into some sequence or order.
from itertools import combinations
players=['jani','john','janardhan']
for i in combinations(players,2):
        print(i)
        '''
        ('jani','jani')
        ('john','janardhan')
        ('jani','janardhan')
        '''
#######################################        
from itertools import permutations
players=['jani','john','janardhan']  
for seat in permutations(players,2):
    print(seat)
    '''
    ('jani', 'john')
    ('jani', 'janardhan')
    ('john', 'jani')
    ('john', 'janardhan')
    ('janardhan', 'jani')
    ('janardhan', 'john')
    '''
###############################################    
#product()
from itertools import product
team_a=['rahit','pandya','bumrah']
team_b=['virat','manish','sami']
for pair in product(team_a,team_b):
    print(pair)
    '''
    ('rahit', 'virat')
    ('rahit', 'manish')
    ('rahit', 'sami')
    ('pandya', 'virat')
    ('pandya', 'manish')
    ('pandya', 'sami')
    ('bumrah', 'virat')
    ('bumrah', 'manish')
    ('bumrah', 'sami')
    '''
######################################################  
#filter 
age=[27,17,21,19]
adults=filter(lambda age:age>=18,age) 
print([age for age in adults])  #list comprehension_
####################################
#IMP 
#shalwo copy and deep copy
#simple program
list_a=[1,2,3,4,5]
list_b=list_a
list_a[0]=-10
print(list_a)
print(list_b)
######################################
#shallow copy
#shallow copy create separet instence
#meance when we change the element of list b then shallow copy change only that element.
import copy
list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)
list_b[0]=-10
print(list_a)
print(list_b)
#####################################################
#but with nested object,modifying on level 2 or deeper does affect the
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.copy(list_a)
list_a[0][0]=-10
print(list_a)
print(list_b)
#########################################
#deep copy
#full independent clones . use copy 
#deep copy function of copy modules
import copy
list_a =[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.deepcopy(list_a)
list_a[0][0]=-10
print(list_a)
print(list_b)
######################################
#write a python program to create iterator
# from several ieterables in a sequence and 
#display the type and element of the new iterator
#use in deep learning machine learing and NLP also
from  itertools import chain
def chain_func(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
#list
result= chain_func([1,2,3],['a','b','c','d'],[4,5,6,7,8,9])
print("type of new iterator:")
print(type(result))
print("element of new iterators")
for i in result:
    print(i)
############################################
#tuple
from  itertools import chain
def chain_func(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
#tuples
result= chain_func((1,2,3),('a','b','c','d'),(4,5,6,7,8,9))
print("type of new iterator:")
print(type(result))
print("element of new iterators")
for i in result:
    print(i)
#############################################
#write python program that gegerates the running product
#of element in an iterable
#itertools feature acumulate
from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)
#list
result=running_product([1,2,3,4,5,6,7])
print("running the product of the list") 
for i in result:
    print(i) 
############################################### 
#apply same for tuple
from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)
#list
result=running_product((1,2,3,4,5,6,7))
print("running the product of the list") 
for i in result:
    print(i) 
#########################################
#write python program to construct infinite iterator 
#that return evenly base value starting with a specified number and step.
import itertools as it
start=10
step=1 
print("starting the number is",start,"and step is",step)
my_counter = it.count(start,step)
#my_counter loop will run ever
print("the said function print never-ending items:")
for i in my_counter:
    print(i)
############################################
#write python program to gegerate infinit cycle of element from an iterable
#iter-set,tupel
import itertools as it
def cycle_data(iter):
    return it.cycle(iter)
#follow loop will run for ever
#list
result=cycle_data(['A','B','C','D'])
print("the said function print never ending items") 
for i in result:
    print(i)
#string
result = cycle_data('python itertools')
print("the said function print never- ending items:")   
for i in result:
    print(i)
#########################################
# write a python program to make an iterator that drops
#the element from the iterable as soon as an element
#dropwhile-
import itertools as it
def drop_while(nums):
     return it.dropwhile(lambda x:x<0,nums)
nums=[-1,-2,-3,4,-10,2,0,5,12]
print("original list:",nums)
result=drop_while(nums)
print("Drops element from the iterable when a positive number arises\n",list(result))
for i in result:    
    print(i)
####################################################    