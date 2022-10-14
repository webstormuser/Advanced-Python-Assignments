#!/usr/bin/env python
# coding: utf-8

# 1.What are the new features added in Python 3.8 version?

# Assignment expressions.
# 
# Positional-only parameters.
# 
# Parallel filesystem cache for compiled bytecode files.
# 
# Debug build uses the same ABI as release build.
# 
# f-strings support = for self-documenting expressions and debugging.
# 
# PEP 578: Python Runtime Audit Hooks.
#     
# PEP 587: Python Initialization Configuration.

# 2.	What is monkey patching in Python?

# In Python, the term monkey patch refers to dynamic (or run-time) modifications of a class or module. In Python, we can actually change the behavior of code at run-time. We use above module (monk) in below code and change behavior of func() at run-time by assigning different value
# Monkey Patching is an exciting topic of Python. Monkey-patching is a term that refers to modifying a class or module at a run time. In simple words, a class or module's work can be changed at the runtime

# In[12]:


class A:
    def func(self):
        print("func is calling")
def monkey_fun(self):
        print("monkey_func is calling")
A.func=monkey_fun
obj=A()
obj.func()


# 3.	What is the difference between a shallow copy and deep copy?

# The Differences between a Shallow Copy and deep copy are as follows:
# 
# When an object is copied using copy(), it is called shallow copy as changes made in copied object will also make corresponding changes in original object, because both the objects will be referencing same address location.
# 
# When an object is copied using deepcopy(), it is called deep copy as changes made in copied object will not make corresponding changes in original object, because both the objects will not be referencing same address location.

# In[17]:


from copy import deepcopy,copy
l1=[1,2,3,[4,5,6],7]
l2=deepcopy(l1)
l3=l1
print(f'Original list is-->{l1}')
l2[2]=10
print(f'Deep copied list -->{l2}')
l3[4]=8
print(f' Original list-->{l1}')
print(f' Shallow copied  list -->{l3}')


# In[18]:


from copy import deepcopy, copy
l_one = [1,2,[3,4],5,6]
l_two = deepcopy(l_one)
l_three = l_one
print(f'Original Elements of each List\n{l_one}\n{l_two}\n{l_three}')
l_two[0] = 10
l_three[-1] = 20
print(f'New Elements of each List\n{l_one}\n{l_two}\n{l_three}')


# 4.	What is the maximum possible length of an identifier?

#  In Python, the highest possible length of an identifier is 79 characters. Python is a high level programming language. It’s also a complex form and a collector of waste.
# 
# Python, particularly when combined with identifiers, is case-sensitive.
# When writing or using identifiers in Python, it has a maximum of 79 characters.
# Unlikely, Python gives the identifiers unlimited length.
# However, the layout of PEP-8 prevents the user from breaking the rules and includes a 79-character limit.

# 5. What is generator comprehension?

#  A generator comprehension is a single-line specification for defining a generator in Python.
# 
# It is absolutely essential to learn this syntax in order to write simple and readable code.
# Generator comprehension uses round bracket unlike square bracket in list comprehension.
# The generator yields one item at a time and generates item only when in demand. Whereas, in a list comprehension, Python reserves memory for the whole list. Thus we can say that the generator expressions are memory efficient than the lists.

# In[20]:


in_list = [x for x in range(10)] # List Comprehension
print(in_list)
out_gen = (x for x in in_list if x%2 == 0) # Generator Comprehension
print(out_gen) # Returns a Generator Object
for ele in out_gen:
    print(ele, end=" ")


# In[ ]:




