#!/usr/bin/env python
# coding: utf-8

# # Q1. Which two operator overloading methods can you use in your classes to support iteration?
# ANS : __iter__ and __next are two operator overloading methods we can use to support iteration

# # Q2. In what contexts do the two operator overloading methods manage printing?
# ANS : _str__ and __repr__ are two operator overloading methods that manage printing.
# 
# In Short, the difference between both these operators is the goal of __repr__ is to be unambiguous and __str__ is to be readable.
# Whenever we are printing any object reference internally __str__ method will be called by default.
# The main purpose of __str__ is for readability. it prints the informal string representation of an object, one that is useful for printing the object. it may not be possible to convert result string to original object.
# __repr__ is used to print official string representation of an object, so it includes all information and development.

# In[13]:


class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        
S1=Student("Pooja",100)
print(str(S1))

class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def __str__(self):
        return f"Student's name :{self.name} and roll_no is:{self.roll_no}"
S2=Student("Meena",101)
print(str(S2))


from datetime import date
today=date.today()
u=repr(today) #converting date to string format
print(u)


# # Q3. In a class, how do you intercept slice operations?
# ANS :"setslice" and "delslice" are deprecated, if you want to do the interception you need to work with python slice objects passed to "setitem" and "delitem". 
#     
#     The __getitem__ method is used for accessing list items, array elements, dictionary entries etc. slice is a constructor in Python that creates slice object to represent set of indices that the range(start, stop, step) specifies. __getitem__ method can be implement in a class, and the behavior of slicing can be defined inside it.
#     Syntax:
# 
# __getitem__(slice(start, stop, step))
# 
# Parameter:
# 
# slice() : constructor to create slice object.
# start: An integer number specifying start index.It is optional and default is 0.
# stop: An integer number specifying end index.
# step: An integer number specifying the step of slicing. It is optional and
# default is 1.

# In[21]:


#let abcde is a string wanted to be sliced 
sliced='abcde'.__getitem__(slice(1,4,1))
print(sliced)

#inside class
class Sliced:
    def __getitem__(self,key):
        print(key)
        return key
s1=Sliced()
s1[1]
s1[1,2]
s1[1,2,3]


# # Q4. In a class, how do you capture in-place addition?
# ANS :Python in its definition provides methods to perform inplace operations, i.e doing assignment and computation in a single statement using “operator” module. For example,
# 
# x += y is equivalent to x = operator.iadd(x, y) 
# Some Important Inplace operations :
# 
# 1. iadd() :- This function is used to assign and add the current value. This operation does “a+=b” operation. Assigning is not performed in case of immutable containers, such as strings, numbers and tuples.
# 
# 2. iconcat() :- This function is used to concat one string at end of second.
# 3. isub() :- This function is used to assign and subtract the current value. This operation does “a-=b” operation. Assigning is not performed in case of immutable containers, such as strings, numbers and tuples.
# 
# 4. imul() :- This function is used to assign and multiply the current value. This operation does “a*=b” operation. Assigning is not performed in case of immutable containers, such as strings, numbers and tuples.
# 5. itruediv() :- This function is used to assign and divide the current value. This operation does “a/=b” operation. Assigning is not performed in case of immutable containers, such as strings, numbers and tuples.
# 
# 6. imod() :- This function is used to assign and return remainder . This operation does “a%=b” operation. Assigning is not performed in case of immutable containers, such as strings, numbers and tuples.
# 

# In[34]:


import operator
class Inplace:
    def __init__(self):
        pass
    def iadd(self,x,y):
        self.x=x
        self.y=y
        Z=operator.iadd(x,y)
        print("the resulf of addition using inplace:{}".format(Z))
    def iconcat(self,x,y):
        self.x=x
        self.y=y
        Z=operator.iconcat(x,y)
        print("the resulf of concatenation using inplace:{}".format(Z))
    def isub(self,x,y):
        self.x=x
        self.y=y
        Z=operator.isub(x,y)
        print("the resulf of subtraction using inplace:{}".format(Z))
    def imul(self,x,y):
        self.x=x
        self.y=y
        Z=operator.imul(x,y)
        print("the resulf of multiplication using inplace:{}".format(Z))
    def imod(self,x,y):
        self.x=x
        self.y=y
        Z=operator.imod(x,y)
        print("the resulf  using inplace:{}".format(Z))
    def truediv(self,x,y):
        self.x=x
        self.y=y
        Z=operator.itruediv(x,y)
        print("the resulf using inplace:{}".format(Z))
i=Inplace()
i.iadd(10,20)
i.iconcat("Welcome to ","iNeuron.ai")
i.isub(20,10)
i.imul(5,6)
i.imod(10,2)
i.truediv(40,4)


# # Q5. When is it appropriate to use operator overloading?
# ANS : The operator overloading in Python means provide extended meaning beyond their predefined operational meaning. Such as, we use the "+" operator for adding two integers as well as joining two strings or merging two lists. We can achieve this as the "+" operator is overloaded by the "int" class and "str" class

# In[35]:


class Book:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self,other):
        return self.pages+other.pages
b1 = Book(100)
b2 = Book(200)
print(f'Total Number of Pages -> {b1+b2}')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




