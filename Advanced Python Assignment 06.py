#!/usr/bin/env python
# coding: utf-8

# # Q1. Describe three applications for exception processing.

# ANS:Exception Processing is used in Various Applications of which few examples are:
# 
# Checking Appropriate use of input in an application
# Checking for Arithmetic exceptions in mathematical executions
# Checking File I/O exceptions during File handling

# # Q2. What happens if you don&#39;t do something extra to treat an exception?

# ANS :If you don't handle an exception, it will propagate up the call stack up to the interpreter, which will then display a traceback and exit.

# # Q3. What are your options for recovering from an exception in your script?

# ANS :using try ,except and finaaly block to recover from exception 

# # Q4. Describe two methods for triggering exceptions in your script.

# ANS :Two methods for triggering exception are using try raise and using assert statement 

# In[1]:


# Example of raise
x = 10
raise Exception(f'X Value Should not exceed 5 The Provided Value of X is {x}')


# In[2]:


# Example of assert
assert(2==4), "2 is not equal to 4"


# # Q5. Identify two methods for specifying actions to be executed at termination time, regardless of whether or not an exception exists.

# ANS :Python Provides else and finally blocks for specifying actions to be executed at termination time, regardless of whether an exceptions exists or not.

# In[ ]:




