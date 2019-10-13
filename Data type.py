# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 21:50:22 2019

@author: Pro
"""
"""
4 type 
   1 - Decimal  form (base10),  Default number system 
	1- Binary form (base 2)  , should be pre fixed with 0b, or 0B,     allowed digit 0 or 1 
	2- Octal form (base-8)  ,  should be pre fixed with 0o or 0O,      allow digit 0 to 7 
	3- Hex Decimal (base-16) , should be pre fixed with 0X or 0x,    allow digit 0 to 15  or A to F

    By Deafult Inter data type provide decimal output if required in other data type need to base conversion
    baseconversion function  
    bin() -->
    oct() -->
    hex() -->
    
"""
'''-------------------------------------------------------------------------'''
bool(0)
#bool(0)
#Out[98]: False

#bool(1)
#Out[99]: True


#a=0X10
#print(a)

a=0XFace
print(a)

#a=0XFace
#print(a)
#64206

# input  any datatype  to bin 

bin(0XFace)
Out[112]: '0b1111101011001110'

bin(15)
Out[114]: '0b1111'


# input  any datatype  to Oct 
oct(15)
Out[116]: '0o17'

oct(0X15)
Out[117]: '0o25'

# input  any datatype  to hex 

hex(0o34567)
hex(0o34567)
Out[118]: '0x3977'

# To convert into Decimal number system function not required 

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#  Floating  point 
# Floating point represent one in Deciaml form 
f =1.234
f= 0b1.1111    # not llowe
f=0o123.2222   # not allowed 
f=0.0x4555ef   # not allowed    

# Scienctifice notation
f=1.23e3
print(f)
f=123e3
print(f)

12000000000000000.0    #15  Zero
1.2e16

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
complex number mathaicl 

x = 10+20J
print(type(x))

jsqr = -1

#x = 10+20J
#print(type(x))
#<class 'complex'>

a+bj
a = real part 
b = imaginry part
print(x.real)
print(x.imag)

#Real part should be Decimal/Oct/bin/Hex/Float  or Int 
#image part should be in deciaml 

x = 0b1111011+20j # allowd
x= 0b111110+10.1J  #  allowed float in imag
x = 0x2d+0b111J # not allowed  bin i imagery

p = 1,q= 0
y = p<q
print(y)





""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

str(False)
#str(False)
#Out[100]: 'False'

str(True)
#str(True)
#Out[104]: 'True'


    
"""
# Titbits
True+True+True
#True+True+True
#Out[97]: 3
