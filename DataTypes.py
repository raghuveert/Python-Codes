# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 11:28:19 2020

@author: Pro
"""
''' Data types  two types
immutable = strings,numbers,Tuples   ,VALUES CANNOT  BE CHANGED
mutable = List, Dictionaries ,Sets  , VALUES CAN BE CHANGED 

'''
a = 'salary'
b = 200
c = 12.2
print(type(a))
print(type(b))
print(type(c))


str1 = 'Hello-World'
str2 = 'Interpat'
print(str1[0])
print(str2[-1])
# Extrat sub string#
print(str1[0:5])

# Find module
str = 'Attachment'
str.find('me')

str.replace('me','m')
str.replace('ment','')

#split
split_word = "word1,word2,word3"
split_word.split(",")


#Return the count of character in the string 
str2 = "Intellipaat"
str2.count("I")

'''Upper().....'''
#upper() - Converts the character/string to uppercase 
str= 'Intellipaat'
str4 = str.upper()
str4.count('I')

''' max()/min() ASCII value.............'''
str5 = '1cdD0kzZ-+'
max(str5)
min(str5)

'.........................................................................'
#Tuple are group of values within()

 mygroup = ('a','b','c','d')
 
#concatenation # Add two string/charater TWO MORE TUPLE
 
 mygroup += ('f',)
 print(mygroup)
 
 #Repetation in Tuple
 mygroup*2

# indexing show the indexed character/string
 mygroup[2]

# slicing specific set of string between 1 to 4
 mygroup[1:5]
 
 
'.........................................................................'
# List  are mutable object

list1 = ['a',123.4,14,'jhon']
list2 = ['python',20]
list3=list2+list1
print(list3)
print(list2)
#Repeataton
list1*2
#Slicing 
list3[1:5]

#Append

#Single Element at end of list
#append adds its argument as a single element to the end of a list.
#The length of the list itself will increase by one.
#Whatever the object is, whether a number, a string, another list, or something else, 
# it gets added onto the end of my_list as a single entry on the list.

x = [1, 2, 3]
x.append([4, 5])
print (x)

 my_list = ['foo', 'bar']
 my_list.append('baz')
 my_list
#output ['foo', 'bar', 'baz']
 
another_list = [1, 2, 3]
my_list.append(another_list)
my_list
#output ['foo', 'bar', 'baz', [1, 2, 3]]

>>> another_list = [1, 2, 3]
>>> my_list.append(another_list)
>>> my_list
['foo', 'bar', 'baz', [1, 2, 3]]
                     #^^^^^^^^^--- single item at the end of the list.


# extend iterates over its argument adding each element to the list, extending the list
# The length of the list will increase by however many elements were in the iterable argument.

# Extend
# All  Element from the irrtrable list tupable  at end of list
#    
                     
x = [1, 2, 3]
x.extend([4, 5])
print (x)

my_list.extend('baz')
my_list
['foo', 'bar', 1, 2, 3, 'b', 'a', 'z']


# Append n Extend difference
# single Element at the end of the list
# list is increase by 1 
a = [1,2,4]
a.append('hello')
a
len(a)
# each itrable character added at end of list
#lit is increase by 2 
a.extend('amul')
a
len(a)
'.........................................................................'




 




