#!/usr/bin/env python
# coding: utf-8

# In[ ]:




get_ipython().set_next_input('Q3. How do class decorators overlap with metaclasses for handling classes');get_ipython().run_line_magic('pinfo', 'classes')

get_ipython().set_next_input('Q4. How do class decorators overlap with metaclasses for handling instances');get_ipython().run_line_magic('pinfo', 'instances')


# # Q1. What is the concept of a metaclass?

# A metaclass in Python is a class of a class that defines how a class behaves. A class is itself an instance of a metaclass. A class in Python defines how the instance of the class will behave. In order to understand metaclasses well, one needs to have prior experience working with Python classes. Before we dive deeper into metaclasses, let's get a few concepts out of the way.
# 
# A metaclass in Python is a class of a class that defines how a class behaves. A class is itself an instance of a metaclass. A class in Python defines how the instance of the class will behave. In order to understand metaclasses well, one needs to have prior experience working with Python classes.

# In[1]:


class TestMyClass:
    pass
mytest_class=TestMyClass()
print(mytest_class)


# In[9]:


type(TestMyClass)


# In[11]:


TestMyClass = type('DataCamp', (), {})
print(TestMyClass)
print(TestMyClass())
#In the above example TestMyClass is the class name while TestMyClass is the variable that holds the class reference. 
#When using type we can pass attributes of the class using a dictionary as shown below:


# In[12]:


PythonClass = type('PythonClass', (), {'start_date': 'August 2018', 'instructor': 'John Doe'} )
print(PythonClass.start_date, PythonClass.instructor)
print(PythonClass)


# # Q2. What is the best way to declare a class&#39;s metaclass?

# ANS :A class defines the properties and available actions of its object and also it acts as a factory for object creation. Let’s understand the process by creating a class using type directly. The exact class that is used for class instantiation is called type. Normally, we define a class using a special syntax called the class keyword, but this syntax is a substitute for type class. Let’s illustrate with an example:

# In[13]:


class meta(type):
    pass
class class_meta(metaclass=meta):
    pass
print(type(meta))
print(type(class_meta))


# # Q3. How do class decorators overlap with metaclasses for handling classes ?

# Ans: Anything you can do with a class decorator, you can of course do with a custom metaclasses (just apply the functionality of the "decorator function", i.e., the one that takes a class object and modifies it, in the course of the metaclass's __new__ or __init__ that make the class object!).

# # Q4. How do class decorators overlap with metaclasses for handling instances?

# Ans: Anything you can do with a class decorator, you can of course do with a custom metaclass (just apply the functionality of the "decorator function", i.e., the one that takes a class object and modifies it, in the course of the metaclass's __new__ or __init__ that make the class object!).

# In[ ]:




