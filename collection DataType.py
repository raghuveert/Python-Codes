# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 16:18:53 2020

@author: Pro
"""

# Fundamental data type int,float,str,bool,complex hold single elememt

# Group of value or things is  collections  related data types
#list, tuple,set,frozenset,range,dict,byte,bytearray

#list of values
# order is important,Order is preerved
# dupliczte is allowed in list 
# hetogeomous object are allowed 
# list is indexin n slicing
# list is growable
# list is mutable (changable)
# add element in list append
# remove element from the list remove



[10,20,30]  #list 
(10,20,30)  #tuple 
{10,20,30} # set 
{100:'raghu',200:'ravi',300:'papau'} 


l = [10,'durga',19.05,'python',10]
print(type(l))    # <class 'list'>
print(l[1])
print(l[-1])
print(l[1:4])
 
list = []
print(type(list))
print(list[])

print(type(l))    # <class 'list'>

# Append

big_basket = ['apple','grapes','banana','jackfruit']
big_basket.append('mango')
print(big_basket)

######################################################################
#Tuple
#() 
#  all property is same except it mutaable
# Read only version of list is Tuple
#  hetrogenous
# append, remove get attribute Error 
k = (10,20,30,40,'raghu')
print(k)
print(k[2])
print(k[1:4])

# tuple immutable
k.remove(10)  # AttributeError: 'tuple' object has no attribute 'remove'
k.append(999) # AttributeError: 'tuple' object has no attribute 'append'

k[0] = 777   # AttributeError: 'tuple' object has no attribute 'append'

# Empty tuple
t = ()
print(type(t))   # <class 'tuple'>
t=(10)
print(type(t))   # <class 'int'>
t=(10,)
print(type(t))  # <class 'tuple'>


######################################################################
# set {obj }
# duplicate not allowed 
# order are required 
# indexing/slicing  not applicable
# hetrogenous object  allowed 
# append applicalbe for list , not for set , add method 
# remove of 30 
# set is growable 
# set in mutable


s = {1,2.3}
s = {2,3,1}
s = {3,2,1}

s = {10,20,30,40 ,10,20,'durga'}
type(s)   # Out[124]: set
print(s)     
s.add(50)
print(s)       # output: {40, 10, 'durga', 50, 20, 30}
print(s[0])    # TypeError: 'set' object does not support indexing
print(s[1:3])  # TypeError: 'set' object does not support indexing

s.add(50)      # add element anywhere in breacket 

s2=set()
print(type(s2))
 
###########################################################################
# dic of empty set 
#dic 
###################
set = {}
print(type(set))    #  out put : <class 'dict'>

###########################################################################
#forzeonset 
#note: its immutable set
######################################
s ={10,20,30,30,40 }
fs = frozenset(s)
print(type(fs))
print(fs)
fs.add(50)     # AttributeError: 'frozenset' object has no attribute 'add'
fs.remove(50)  # AttributeError: 'frozenset' object has no attribute 'add'


###############################################################################
# Dictornary 
# group of value pair then need to key value pair
#order not gantureed or important
# duplicate key not allowed but values are allowed 
# Hetogenous obj 
# its mutable 
# indexing slicing not appliable 

######################################################
d = { 100:'durga',200:'sunny',300:'chinny'}
print(type(d))      # <class 'dict'>

d ={}
d[100] ='durga'
d[200] ='ravi'
print(d)          #output:   {100: 'durga', 200: 'ravi'}
d[100] ='shiva'   #output: old value will be replace with new value
print(d)

###############################################################################
# Range datatype
# Range sequqnce of datanumber
# ordering is there
# Index/sclicing is there
# Range obj is immutable cnt change
#######################
r = range(10) # 0 to 9 
print(type(r)) # <class 'range'>
print(r)       # range(0, 10)

for x in r :
    print(x)
#out put    
0
1
2
3
4
5
6
7
8
9

# format 1 range(n)
from 0 to 

#format2 
r =range(1,10)
for x in r :
    print(x)

#format3 
r = range(1,21,5)
for x in  r:
    print(x)
    
# format 4 
r= range(20,1,-5)
for x in r:
    print(x)
    
#Rangee sclicing
#-----------------
 
r = range (10,21)
print(r[0])
r1=r[1:5]
for x in r1:
    print(x)

###############################################################################
#Byte Datatye
# uses in video files, audio file 
# values from 0 to 256
# immutable cnat change
##################################
    
l = [10,20,30,40,50]
b =bytes(l)
print(type(b))              # <class 'bytes'>

for x in b:
    print(x)
    
l = [10,20,30,40,50,256]

b=bytes(l)
print(l)           # ValueError: bytes must be in range(0, 256)

# Byte are immutable
l = [10,20,30,40,50]
b =bytes(l)
print(type(b))              # <class 'bytes'>
print(b[0])
b[0] = 100            # TypeError: 'bytes' object does not support item assignment



###############################################################################
#Bytearray Datatye
# uses in video files, audio file 
# values from 0 to 256
# mutable change
##################################
l = []
b = bytearray(l)

l = [10,20,30,40,50]
b =bytearray(l)
print(type(b))              # <class 'bytes'>
#print(b[0])
b[0] = 100            # TypeError: 'bytes' object does not support item assignment

for x in b:
     print(x)


###############################################################################
#None Data type
# None is Objet type 

#######################
def f1():
    return(10)

x = f1()
print(x)


def f1():
    print('Hello')

x = f1()
print(x)

#Hello
#None

a = None
print(id(a))               # 140730524060896
print(type(a))            # <class 'NoneType'>

a =None
b= None 
c= None 
d =None 
print(id(a),id(b),id(b),id(c)) 
 
#Output : 140730524060896 140730524060896 140730524060896 140730524060896

###############################################################################




