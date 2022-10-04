#!/usr/bin/env python
# coding: utf-8

# Q1. Does assigning a value to a string&#39;s indexed character violate Python&#39;s string immutability?

# A string is immutable because we can't change its value after defining it. Furthermore, once we assign a value to a string, it receives an id based on that value we assigned. Hence if we change the value of that string, it causes to change its id. Therefore, strings are immutable.

# Q2. Does using the += operator to concatenate strings violate Python&#39;s string immutability? Why or
# why not?

# It violates the rules of how ID values and += are supposed to work - the ID values produced with the optimization in place would be not only impossible, but prohibited, with the unoptimized semantics - but the developers care more about people who would see bad concatenation performance and assume Python sucks

# Q3. In Python, how many different ways are there to index a character?

# Indexing means referring to an element of an iterable by its position within the iterable. Each of a string’s characters corresponds to an index number and each character can be accessed using its index number. We can access characters in a String in Two ways :
# 
# Accessing Characters by Positive Index Number
# 
# 
# Accessing Characters by Negative Index Number

# In[6]:


str1="Welcome to iNeuron Data Science Bootcamp"
#positive indexing 
print(str1[0])
print(str1[12])
#Negative indexing 
print(str1[-2])
print(str1[-1])


# Q4. What is the relationship between indexing and slicing?

# Indexing: Indexing is used to obtain individual elements.
#     
# Slicing: Slicing is used to obtain a sequence of elements.
#     
# Indexing
# Indexing starts from 0. Index 0 represents the first element in the sequence.
# 
# Negative indexing starts from -1. Index -1 represents the last element in the sequence.

# In[11]:


str1="welcome to datascience certification program"
#indexing 
print(str1[0])
#slicing
print(str1[0:7])


# Q5. What is an indexed character&#39;s exact data type? What is the data form of a slicing-generated
# substring?

# ANS :The index indicates which character you want. It can be any integer expression so long as it evaluates to a valid index value. Note that indexing returns a string — Python has no special type for a single character. It is just a string of length 1
# 
# The data form of slicing generated substring is string itself since it is a sequence of characters sliced from original string 

# Q6. What is the relationship between string and character &quot;types&quot; in Python?

# The main difference between Character and String is that Character refers to a single letter, number, space, punctuation mark or a symbol that can be represented using a computer while String refers to a set of characters.

# Q7. Identify at least two operators and one method that allow you to combine one or more smaller
# strings to create a larger string.

# There are number of ways in python to concatenate the strig to create a larger string from smaller strings

# In[24]:


#Use of + operator to concatenate two strings 
str1="hello"
str2="world"
print(str1+str2)

#Use of * operator to concatenate two strings
str1="hello"
print(str1 * 3)


# #Using different methods 
# Methods available in python are join method,format(),using f'string,using StringIO

# In[29]:


#Using join()
str1="hello"
str2="World"
print(" ".join([str1,str2]))

#Using format ()

print("{} {}".format(str1,str2))

#Using f'string 

print(f"{str1} {str2} ")


# Q8. What is the benefit of first checking the target string with in or not in before using the index
# method to find a substring?

# It will not raise the expection Exception:  Raises ValueError if argument string is not found or index is out of range.

# Q9. Which operators and built-in string methods produce simple Boolean (true/false) results?

# in
# 
# not
# 
# <string>.isalpha()   
# <string>.isalnum()
# <string>.isdecimal()
# <string>.isdigit()
#     
# <string>.islower()
#     
# <string>.isnumeric()    
# <string>.isprintable()
#     
# <string>.isspace()
#     
# <string>.istitle()

# In[ ]:




