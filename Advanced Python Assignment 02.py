#!/usr/bin/env python
# coding: utf-8

# # Q1. What is the relationship between classes and modules?
# ANS:  Modules are files present inside a package, whereas a class is used to encapsulate data and functions together inside the same unit.
# A class can have its own instance, but a module cannot be instantiated. We use the ‘class’ keyword to define a class, whereas to use modules, we use the ‘import’ keyword. We can inherit a particular class and modify it using inheritance. But while using modules, it is simply a code containing variables, functions, and classes.

# # Q2. How do you make instances and classes?
# ANS :To create instances of a class, you call the class using class name and pass in whatever arguments its __init__ method accepts. 

# # Q3. Where and how should be class attributes created?
# 
# ANS :Class attributes are the variables defined directly in the class that are shared by all objects of the class.
# class Attributes Accessed using class name as well as using object with dot notation, e.g. classname.class_attribute or object.class_attribute.

# In[16]:


class Student:
    count = 0
    def __init__(self): 
        Student.count += 1     #here count is class attribute which will be shared by all instances created on same class and value will be reflected  


# In[17]:


std1=Student()
Student.count


# In[18]:


std2 = Student()
Student.count


# # Q4. Where and how are instance attributes created?
# ANS :Instance attributes are attributes or properties attached to an instance of a class. Instance attributes are defined in the constructor.
#     instance Attributes Accessed using object dot notation e.g. object.instance_attribute
# 

# In[19]:


class Student:
    def __init__(self, name, age): 
        self.name = name
        self.age = age


# In[20]:


std = Student('Bill',25)
std.name


# # Q5. What does the term &quot;self&quot; in a Python class mean?
# ANS :reference to the current instance of the class, and is used to access variables that belongs to the class.

# # Q6. How does a Python class handle operator overloading?
# 
# ANS :To perform operator overloading, Python provides some special function or magic function that is automatically invoked when it is associated with that particular operator. For example, when we use + operator, the magic method __add__ is automatically invoked in which the operation for + operator is defined.

# In[29]:


# Python Program illustrate how 
# to overload an binary + operator
class Sub:
    def __init__(self,A):
        self.A=A
    def __add__(self,B):
        return self.A+B.A
obj1=Sub(10)
obj2=Sub(20)
print(obj1+obj2)
obj3="Welcome"
obj4="to iNeuron"
print(obj3+obj4)


# # Q7. When do you consider allowing operator overloading of your classes?
# ANS :Consider that we have two objects which are a physical representation of a class (user-defined data type) and we have to add two objects with binary ‘+’ operator it throws an error, because compiler don’t know how to add two objects. So we define a method for an operator and that process is called operator overloading. We can overload all existing operators but we can’t create a new operator. To perform operator overloading, Python provides some special function or magic function that is automatically invoked when it is associated with that particular operator. For example, when we use + operator, the magic method __add__ is automatically invoked in which the operation for + operator is defined.

# # Q8. What is the most popular form of operator overloading?
# 
# 
# ANS :Operator overloading is the process of using an operator in different ways depending on the operands. You can change the way an operator in Python works on different data-types. A very popular and convenient example is the Addition (+) operator.
#     Just think how the ‘+’ operator operates on two numbers and the same operator operates on two strings. It performs “Addition” on numbers whereas it performs “Concatenation” on strings.
# 
# Operators in Python work for built-in classes, like int, str, list, etc. But you can extend their operability such that they work on objects of user-defined classes too.

# # Q9. What are the two most important concepts to grasp in order to comprehend Python OOP code?
# 
# ANS :Both inheritance and polymorphism are fundamental concepts of object oriented programming. These concepts help us to create code that can be extended and easily maintainable

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




