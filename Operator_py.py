# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 08:42:22 2020

@author: Pro
"""

# 6 digit Random otp########
from random import randint
print(randint(0.9))
dir(randint)

######Operator#########

print(ord('a'))

print(chr(97))
print(chr(68))


#Assigning single value to a variable…#
a = 10
name = 'Victor'
salary = 2000.23
isEmployed = True

a = 10

print("The value", a, "has type", type(a))
print(name)
print(salary)
print(type(a))
print(type(name))
print(type(salary))
print(type(isEmployed))

The value 10 has type <class 'int'>
Victor
2000.23
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>

#######################################################################
#Special Literals: None
val1 = 10
val2 = None
Val2 = 12

print(val2)
print(Val2)

print(id(val1))
print(id(val2))
print(type(val2))


#######################################################################

Logical Operators: and, or, not
 We can apply for all types.
For boolean Types Behaviour:
and  If both arguments are True then only result is True
or  If atleast one arugemnt is True then result is True
not  Complement
True and False  False
True or False  True
not False  True
For non-boolean Types Behaviour:
0 means False
non-zero means True
empty string is always treated as False
x and y:
If x is evaluates to false return x otherwise return y
Eg:
10 and 20
0 and 20
If first argument is zero then result is zero otherwise result is y


10 and 20
0 or 2
10 or 20


print(4&5) 

print(True & True)


We can apply bitwise operators for boolean types also

print(True & False) 
print(True | False) 
print(True ^ False) 
print(~True) 
print(True<<2) 
print(True>>2) 


#######################################################################
#Q) Program for Maximum of 3 Numbers

a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
max=a if a>b and a>c else b if b>c else c
print("Maximum Value:",max)


##############Identity Operators
# We can use identity operators for address comparison.
# There are 2 identity operators are available

1) is
2) is not
 r1 is r2 returns True if both r1 and r2 are pointing to the same object.
 r1 is not r2 returns True if both r1 and r2 are not pointing to the same object.
Eg:
1) a=10
2) b=10
3) print(a is b) True
4) x=True
5) y=True
6) print( x is y) True 

#############################################################################

2)Membership Operators:
 We can use Membership operators to check whether the given object present in the
given collection. (It may be String, List, Set, Tuple OR Dict)
 In  Returns True if the given object present in the specified Collection
 not in  Retruns True if the given object not present in the specified Collection
Eg:
1) x="hello learning Python is very easy!!!"
2) print('h' in x) True
3) print('d' in x) False
4) print('d' not in x) True
5) print('Python' in x) True
Eg:
1) list1=["sunny","bunny","chinny","pinny"]
2) print("sunny" in list1) True
3) print("tunny" in list1) False
4) print("tunny" not in list1) True 
    

#############################################################################
1)Identity Operators
 We can use identity operators for address comparison.
 There are 2 identity operators are available
1) is
2) is not
 r1 is r2 returns True if both r1 and r2 are pointing to the same object.
 r1 is not r2 returns True if both r1 and r2 are not pointing to the same object.
Eg:
1) a=10
2) b=10
3) print(a is b) True
4) x=True
5) y=True
6) print( x is y) True
Eg:
1) a="durga"
2) b="durga"
3) print(id(a))
4) print(id(b))
5) print(a is b)
Eg:
1) list1=["one","two","three"]
2) list2=["one","two","three"]
3) print(id(list1))
4) print(id(list2))
5) print(list1 is list2) False
6) print(list1 is not list2) True
7) print(list1 == list2) True
Note: We can use is operator for address comparison where as == operator for content
comparison.

################################################################################

#If multiple operators present then which operator will be evaluated first is decided by
#operator precedence.

#Eg:
#print(3+10*2)  23
#print((3+10)*2)  26
#The following list describes operator precedence in Python
#1) ()  Parenthesis
#2) **  Exponential Operator
#3) ~, -  Bitwise Complement Operator, Unary Minus Operator
#4) *, /, %, //  Multiplication, Division, Modulo, Floor Division
#5) +, -  Addition, Subtraction
#6) <<, >>  Left and Right Shift
#7) &  Bitwise And
#8) ^  Bitwise X-OR
#9) |  Bitwise OR
#10) >, >=, <, <=, ==, !=  Relational OR Comparison Operators
#11) =, +=, -=, *=...  Assignment Operators





