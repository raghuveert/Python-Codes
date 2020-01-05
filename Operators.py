# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 10:14:51 2020

@author: Pro
"""
''' 7 type od Operator
#  Arthemathic Operator
#  +,-,*,/,%
oprand (+ oprator ) Oprand 

# Assignment Oprator
# =, +=,-=,
'''
a= 10
a*=10
print(a)
100

'''comparission oprator.......'''
#<,>,<=,>=,!= 
# Output is either True or false

a=10
b=20
a >= b

#Out[10]: False

''' Logical Oprator...'''
# and or not 
# compaire two Operator...
a=10<10 and 2>1  # false and True
#output false 
print(a)

'''Bit wise Operator......''''
#convert 7 111,5 101 convert to bit wise and 

# &,!,>>,<<,`
7 | 5
#Out[14]: 7

7&5
#Out[20]: 5

~7
#Out[19]: -8

#Right shift
#------------
10>>2
#1010 shift 2 bit Right
#0010  
#Out[21]: 2
10<<2
#101000 
#Out[23]: 40
10<<3
#1010000
#Out[24]: 80

'''Identity Operator...'''
#is , is not
# output is True or False
x = 10
x is 10

x = 10 
x is not 10
#Out[26]: False

'''Member ship operator......'''
#in, not in
#  Test  wheater a value is a membership of a sequence or not
pets = ['dog','cat','rat']
'lion' in pets
#Out[28]: False

'dog' in pets 

