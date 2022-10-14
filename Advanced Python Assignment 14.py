#!/usr/bin/env python
# coding: utf-8

# Q1. Is an assignment operator like += only for show? Is it possible that it would lead to faster results at the runtime?

# A=A+1 evaluates to finding A, adding 1 to it. Then storing the value again in variable A. This expression makes Python to look for memory holder of a twice. But A+=1 simply means value of A is to incremented by 1. As memory address has to be identified once, += leads to faster operation.

# Q2. What is the smallest number of statements you'd have to write in most programming languages to replace the Python expression a, b = a + b, a?

# we reuquire 4 lines 
# 2 lines for assigning initials values to a,b 
# and 2 lines for assigning a=a+b and b=a

# Q3. In Python, what is the most effective way to set a list of 100 integers to 0?

# In[2]:


list1=[0 for ele in range(0,101)]
print(list1)


# Q4. What is the most effective way to initialise a list of 99 integers that repeats the sequence 1, 2, 3? S If necessary, show step-by-step instructions on how to accomplish this.

# In[6]:


a=[1,2,3]
list1=a*33
print(list(list1))


# Q5. If you're using IDLE to run a Python application, explain how to print a multidimensional list as efficiently?

# In[19]:


mylist1=[[1,1],[2,2],[3,3],[4,4]]
for x in range(len(mylist1)):
    for y in range(len(mylist1[x])):
        print(mylist1[x][y] ,end=" ")


# Q6. Is it possible to use list comprehension with a string? If so, how can you go about doing it?

# In[20]:


str1="Welcome to data science bootcamp"
str2=[ele for ele in str1]
print(str2)


# Q7. From the command line, how do you get support with a user-written Python programme? Is this possible from inside IDLE?

# Get support with a user-written Python Programme: Start a command prompt (Windows) or terminal window (Linux/Mac). If the current working directory is the same as the location in which you saved the file, you can simply specify the filename as a command-line argument to the Python interpreter.
#     
# Get support with a User-written Python Program from IDLE: You can also create script files and run them in IDLE. From the Shell window menu, select File → New File. That should open an additional editing window. Type in the code to be executed. From the menu in that window, select File → Save or File → Save As… and save the file to disk. Then select Run → Run Module. The output should appear back in the interpreter

# Q8. Functions are said to be “first-class objects” in Python but not in most other languages, such as C++ or Java. What can you do in Python with a function (callable object) that you can't do in C or C++?

#  The tasks which can be performed with the functions in python are:
# 
# A function is an instance of the Object type.
# You can store the function in a variable.
# You can pass the function as a parameter to another function.
# You can return the function from a function.
# You can store them in data structures such as hash tables, lists,

# Q9. How do you distinguish between a wrapper, a wrapped feature, and a decorator?

#  So, wrappers are the functionality available in Python to wrap a function with another function to extend its behavior. Now, the reason to use wrappers in our code lies in the fact that we can modify a wrapped function without actually changing it. They are also known as decorators
#     

#  Wrappers Around the functions are known as Decrators.

# Q10. If a function is a generator function, what does it return?

# Unlike regular functions, generator functions return generator objects. Meaning, when you call a generator function, it doesn't run the function. Instead, it gives you back a generator object

# Q11. What is the one improvement that must be made to a function in order for it to become a generator function in the Python language?

# Ans: Generator is a written as normal function but uses yield keyword to return values instead of return keyword.

# Q12. Identify at least one benefit of generators.

# Ans: return statement sends a specified value back to its caller whereas yield statment can produce a sequence of values. We should use generator when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.

# In[ ]:




