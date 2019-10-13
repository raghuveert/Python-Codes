# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 13:43:04 2019

@author: Pro
"""
"""Tibits"""
'''--------------------------------------------------------------------------------'''

#multiple assignemt 
a=b=c=10             #same value to multiple variable
 # multiple value to multiple variable
x,y,z=,10,20,30      # multiple value to multiple variable

x,y = 25,50
print(x,y)
x,y=y,x             #swaping  values
print(x,y)
print(x,y)
50 25
print(x)
50

a,b,c= 5,10,7
b,c,a=a+1,b+2,c-1   # Evaluate from left to Right and assigned in same order 
print(a,b,c)        
6 6 12

x,x =20,30
y,y=x+30,x+20
print(x,y)

x,y =2,6
x,y=y,x+2
print(y)
'''----------------------------------------------------------------------------'''
X,Y=7
TypeError: cannot unpack non-iterable int object
a,b =12,13
c,b = a*2,a/2
print(a,b,c)
# output 12 6.0 24
x,y = 20,60
y,x,y =x,y-10,x+10
print(x,y)
#output 50,30

x=40
y=x+1
x=20,y+x
print(x,y)
# output (20, 81) 41


######################################
print(v)
v=20             #NameError: name 'v' is not defined
print(v) 
# Variable is defined only when assigned some value to it using undefined variable in an expression/statement causes name error
v=0
print(v)
v=20             #NameError: name 'v' is not defined
print(v) 
'''--------------------------------------------------------------------------------'''

Data Types
a=12345
b=1,2345
type(a)
type(b)    #Out[48]: tuple
'''--------------------------------------------------------------------------------'''
'''Dynamic Typing
A variable pointing to value of certain type can be made to point to value/object of different type (Dynamic typing) 
by deafult input/print function accept/display  datatpe as str
with print(),the Objects/iterms that you are given must be covertible to string type
'''
X = 10
print(X)
X = "Hello World"
print(X)

age = input("what is your age?")
print(type(age))
age + 1 
'''
what is your age?16
<class 'str'>
'''

age =int(age)

#simple statement
age = int(input("what is your age?"))

True+True+True+True
Out[79]: 4


#Program to read a number n and print nsrq,ncude,
x = int(input("Enter the value of n"))
x=x**4
print(x)


 
 
'''
True == 1 
Out[93]: True

False == 0 
Out[94]: True

True + True
Out[95]: 2
'''

