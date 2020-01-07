# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 15:40:02 2020

@author: Pro
"""

'.........................................................................'
'''Type conversion...............'''
#####################################
# convert other type to int type
#complex ---> int 
#complex number cannt be converted to int type
# type Error TypeError: can't convert complex to int
# int type castiong
#################################################
int(10.9980)
float(10)
int(10+20j)
int(False)
int(True)
float(True)
''
# Str to int
#Str internally contains only intergral should be specified base10
int('15')  # Out[13]: 15
int('0b111')  # ValueError: invalid literal for int() with base 10: '0b111'
int('10.5')  # ValueError: invalid literal for int() with base 10: '10.5'

##################################################
# Foalt type conversion 
# int ---> float 
# complex ----> float
# bool ----> float
#str ---->float
##################################################
float(10)    # Out[15]: 10.0
float(0B000) # Out[16]: 0.0
float(0x11) # Out[17]: 17.0
float(0xface) # Out[18]: 64206.0

# Complex to Float Error
float(10+2j)   # TypeError: can't convert complex to float

# Bol to float
float(True)   # Out[23]: 1.0
float(False)  #Out[22]: 0.0

# Str to float
# note: internally string should either int or foalt value only in base10
float('10') # Out[24]: 10.0
float('20.6') # Out[25]: 20.6
float('oxface') # ValueError: could not convert string to float: 'oxface'
float('Raghu') # ValueError: could not convert string to float: 'Raghu'


############################
# complex number converstion
#Note: only with real value
#############################

complex(10)    # Out[28]: (10+0j)
complex(0b111)  # Out[29]: (7+0j)
complex(True)   # Out[30]: (1+0j)
complex(False)   # Out[31]: 0j
complex(10.5)   # Out[32]: (10.5+0j)
complex('10.5') Out[33]: (10.5+0j)
complex('ragi')  # ValueError: complex() arg is a malformed string
complex(10,20)   # Out[35]: (10+20j)
complex(10.5,16.7)  # Out[36]: (10.5+16.7j)
complex('10.5','16.7')  # TypeError: complex() can't take second arg if first is a string


############################
#  bool number converstion
#Note: ifstr is empty its its false
#############################

bool(20)    # int :arugment Out[38]: True
bool(0)     # int : Out[43]: False
bool(0.0)   #Foalt:  Out[39]: False 
bool(0.001)  # foalt: Out[40]: True

bool(0+0j)   # Complex: Out[41]: False
bool(1+0j)   # CompleOut[42]: True

bool('True')   #Out[46]: True
bool('Raghu') #Out[46]: True
bool('0')    #Out[46]: True
bool('False') #Out[47]: True
bool('')      Out[48]: False

 

############################
#  str  number converstion
#############################

str(10)    # Out[49]: '10'
str(0b111)  # Out[50]: '7'
str(10.9)   # Out[51]: '10.9'
str(True)   # Out[52]: 'True'
str(10+20J) # Out[53]: '(10+20j)'


##################################
#Immutable : non changable behavior
#note: once object created cannt make any changes to that obj only 
#       if try to make any change new obj will be created 
# Three ref obj pointing to same ref variable 
# memory untilization, perform 
##################################

x=10
print(id(x))        
x=x+1              # New Object is created(11)  and X point to there and  10 point to there 
print(id(x))


x=10
print(id(x))        
y=x              # New Object is created(11)  and X point to there and  10 point to there 
print(id(x))

# One obj three ref variable 
a = 10 
b = 11 
c = 10
print(id(a))
print(id(b))
print(id(c))
#140730524546160
#140730524546160
#140730524546160

# identity  
print (a is b )    # True

c = 'Raghu'
d = 'Sanju'
c is d 

#############################################################################
# All data type are immuteable
# E.g int,faolt,complex,bool,str


a = 1000
b = 1000

a is b 

a = 10
b = 10
a is b

a = 257
b =257
a is b 

#############################################################################
# List is mutable 
 l = [10.20,30]
 print(id(l))
 l[0]= 777
 #l = [777,20,30]
 print(id(l))   
 # output : 2719756206024
# output :2719756206024
 
# before and After changes in object index address  is same

# l1 and l2 point to same object, if any change in one list other list automatic changes 
l1 = [10,20,30,40]
l2 = l1
print(l1)
print(l2)

l1[0] = 777
print(l1)
print(l2)
l2[1]=999
print(l1)
print(l2)
  
 
    
    

