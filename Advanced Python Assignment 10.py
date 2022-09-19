#!/usr/bin/env python
# coding: utf-8

# # Q1. What is the difference between __getattr__ and __getattribute__?

# ANS :__getattr__()
#     Let’s start with __getattr__. This method will allow you to “catch” references to attributes that don’t exist in your object. Let’s see a simple example to understand how it works:

# In[5]:


class Dummy(object):
        pass
d=Dummy()
d.does_not_exitst #In this example, the attribute access fails (with an AttributeError) because the attribute does_not_exist doesn’t exist.


# In[10]:


class Dummy(object):
    def __getattr__(self,attr):
        return attr.upper()
e=Dummy()
e.does_not_exits


# In[11]:


d=Dummy()
d.what_to_do


# In[12]:


f=Dummy() #but if attribute does not exists then __getattr__ method will not be invoked
f.value='Python'
print(f.value)


# __getattribute__
# __getattribute__ is similar to __getattr__, with the important difference that __getattribute__ will intercept EVERY attribute lookup, doesn’t matter if the attribute exists or not. Let me show you a simple example:

# In[16]:


class Dummy(object):
    def __getattribute__(self,attr):
        return "You See Me?"
d=Dummy()
d.value='Python'
print(d.value)
# instead of printing Python it has taken value passed to getattribute () method because getattribute () will intercept every attribute doesnt matter if the attribute exixts or not
print(d.__dict__)


# # Q2. What is the difference between properties and descriptors?

# Descriptor --> Descriptor gives us powerful technique to write reusable code in python that can be shared between classes.
# Descriptor is an object attribute with “binding behavior”. They establishes a connection among the attributes of classes. They are Python objects that implement a method of the descriptor protocol, which gives you the ability to create objects that have special behavior when they are accessed as attributes of other objects.A descriptor is a mechanism behind properties, methods, static methods, class methods and super().
# 
# In descriptors we used three different methods that are __getters__(), __setters()__, and __delete()__.
# Descriptor Protocol —
# Python doesn’t have a private variables concept, and descriptor protocol can be considered as a Pythonic way to achieve something similar. Descriptors are a new way to implement classes in Python, and it does not need to inherit anything from a particular object. To implement descriptors, easily in python we have to use at least one of the methods that are defined above. 
# 
# There are three protocol in python descriptor for setters, getters and delete method. They are —
# 
# gfg.__get__(self, obj, type=None) : This attribute is called when you want to retrieve the information (value = obj.attr), and whatever it returns is what will be given to the code that requested the attribute’s value.
# gfg.__set__(self, obj, value) : This method is called to set the values of an attribute (obj.attr = 'value'), and it will not return anything to you.
# gfg.__delete__(self, obj) : This method is called when the attribute is deleted from an object (del obj.attr)
#     Descriptors are invoked automatically whenever it receives the call for a set() method or get() method.
#     Important points to remember :
# 
# Descriptors are invoked by the __getattribute__() method.
# Overriding __getattribute__() prevents automatic descriptor calls.
# object.__getattribute__() and type.__getattribute__() make different calls to __get__().
# Data descriptors always override instance dictionaries.
# Non-data descriptors may be overridden by instance dictionaries.
# 

# In[23]:


class Descriptor(object):
    def __init__(self,name=" "):
        self.name=name
    def __get__(self,obj,objtype):
        return "{} for {} ".format(self.name,self.name)
    def __set__(self,obj,name):
        if isinstance(name,str):
            self.name=name
        else:
            raise TypeError("Input value should be String")


# In[24]:


class GFG(object):
    name=Descriptor()
g=GFG()
g.name="Baby"
print(g.name)


# As a descriptor, it has binding behavior when it’s accessed using dot notation. In this case, the descriptor logs a message on the console every time it’s accessed to get or set a value:
# 
# When it’s accessed to .__get__() the value, it always returns the value 42.
# When it’s accessed to .__set__() a specific value, it raises an AttributeError exception, which is the recommended way to implement read-only descriptors.

# Python internally uses property. It logs a message to the console when it’s accessed. Calling property() is a succinct way of building a data descriptor that triggers function calls upon access to an attribute. 
# 
# Its signature is:property(fget=None, fset=None, fdel=None, doc=None) -> object
# 
# 
# property() returns a property object that implements the descriptor protocol. It uses the parameters — fget , fset and fdel for the actual implementation of the three methods of the protocol.
# 
# 
# 
# To see how property() is implemented in terms of the descriptor protocol, here is a pure Python equivalent:

# In[30]:


class Property(object):
    def __init__(self,fget=None,fset=None,fdel=None,doc=None):
        self.fget=fget
        self.fset=fset
        self.fdel=fdel
        if doc is None and fget is not None:
            doc=fget.__doc__
        self.__doc__=doc
    def __get__(self,obj,objtype):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("Unreadable Attribute")
        return self.fget(obj)
    def __set__(self,obj,value):
        if self.fset is None:
            raise AttributeError("cant set Attribute")
        return self.fset(obj,value)
    def __delete__(self,obj):
        if self.fdel is None:
            raise AttributeError("cant delete Attribute")
        return self.fdel(obj)


# Purpose of Descriptors
# Python descriptors are a way to create managed attributes. Among their many advantages, managed attributes are used to protect an attribute from changes or to automatically update the values of a dependent attribute.
# 
# Descriptors increase an understanding of Python, and improve coding skills.
# 
# Let’s define a class car that has three attributes, namely make, model, and fuel_cap. You will use the __init__() method to initialize the attributes of the class. Then, you will use the magic function __str__(), which will simply return the output of the three attributes that you will pass to the class while creating the object.
# 
# Note that the __str__() method returns the string representation of the object. It is called when print()or str() function is invoked on an object of the class.

# # Q3. What are the key differences in functionality between __getattr__ and __getattribute__, as well as properties and descriptors?

# ANS : The Key Differences between __getattr__, __getattribute__, Properties and Descriptors are:
# 
# __getattr__: Python will call this method whenever you request an attribute that hasn't already been defined
# 
# __getattribute__ : This method will invoked before looking at the actual attributes on the object. Means,if we have __getattribute__ method in our class, python invokes this method for every attribute regardless whether it exists or not.
# 
# Properties: With Properties we can bind getter, setter and delete functions together with an attribute name, using the built-in property function or @property decorator. When we do this, each reference to an attribute looks like simple, direct access, but involes the appropriate function of the object.
# 
# Descriptor: With Descriptor we can bind getter, setter and delete functions into a seperate class. we then assign an object of this class to the attribute name in our main class. When we do this, each reference to an attribute looks like simple, direct access but invokes an appropriate function of descriptor object.

# In[ ]:




