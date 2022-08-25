#!/usr/bin/env python
# coding: utf-8

# # Q1. What is the meaning of multiple inheritance?
# ANS :Multiple inheritance means inheriting the features from more than one super class.

# In[ ]:


class Father:
    pass
class Mother:
    pass
class Child(Father,Mother):
    pass


# # Q2. What is the concept of delegation?
# ANS :Delegation is an object oriented technique (also called a design pattern). Let's say you have an object x and want to change the behaviour of just one of its methods. You can create a new class that provides a new implementation of the method you're interested in changing and delegates all other methods to the corresponding method of x.

# In[43]:


class Faculty:
    def __init__(self,insem,pract,endsem):
        self.insem=insem
        self.pract=pract
        self.endsem=endsem
    def marks(self):
        return self.insem+self.pract+self.endsem

class Student:                  #Student class is container class 
    def __init__(self,name,year,insem,pract,endsem):
        self.name=name
        self.year=year
        self.Faculty_obj=Faculty(insem,pract,endsem)  # faculty class is a contained class 
    def Smarks(self):
        print("the overall score of student is ",self.Faculty_obj.marks())
S=Student("Pooja","Final year",35,19,45)
S.Smarks()

#Delegation is has a type of relationship


# In[ ]:


get_ipython().set_next_input('Q3. What is the concept of composition');get_ipython().run_line_magic('pinfo', 'composition')
ANS :Composition refers to part of relationship


# In[48]:


class Salary:
    def __init__(self,basic,bonus):
        self.basic=basic
        self.bonus=bonus
    def anual_Salary(self):
        return ((self.basic*12)+self.bonus)
class Employee:
    def __init__(self,empid,name,age,dept,basic,bonus):
        self.empid=empid
        self.name=name
        self.age=age
        self.dept=dept
        self.salary_obj=Salary(basic,bonus)
    def Emp_Tot_Salary(self):
        print("total Salary of employee is",self.salary_obj.anual_Salary()) 
e=Employee(1000,"Shruti",29,"IT",35000,1700)
e.Emp_Tot_Salary()


# # Q4. What are bound methods and how do we use them?
# ANS :  If a function is an attribute of class and it is accessed via the instances, they are called bound methods. A bound method is one that has self as its first argument. Since these are dependent on the instance of classes, these are also known as instance methods.
# A bound method is the one which is dependent on the instance of the class as the first argument. It passes the instance as the first argument which is used to access the variables and functions. In Python 3 and newer versions of python, all functions in the class are by default bound methods.

# In[67]:


class A :
    def fun(self,args):
        self.args=args
        print("Value of args",self.args)
A=A()
A.fun


class Car:
    # Car class created
    gears = 5
  
    # a class method to change the number of gears 
    @classmethod
    def change_gears(cls, gears):
        cls.gears = gears
  
  
# instance of class Car created
Car1 = Car()
  
print("Car1 gears before calling change_gears() = ", Car1.gears)
Car1.change_gears(6) 
print("Gears after calling change_gears() = ", Car1.gears)
  
# bound method
print(Car1.change_gears)


# # Q5. What is the purpose of pseudoprivate attributes?
# ANS :Pseudoprivate attributes are also useful in larger frameworks or tools, both to avoid introducing new method names that might accidentally hide definitions elsewhere in the class tree and to reduce the chance of internal methods being replaced by names defined lower in the tree. If a method is intended for use only within a class that may be mixed into other classes, the double underscore prefix ensures that the method won't interfere with other names in the tree, especially in multiple-inheritance scenarios
# 
# Pseudoprivate names also prevent subclasses from accidentally redefining the internal method's names,

# In[68]:


class Super:
    def method(self): # A real application method
        pass
class Tool:
    def _method(self): # becomes _Tool_method
        pass
    def other(self): # uses internal method
        self._method()
class Subl(Tool,Super):
    def actions(self):
        self.method()
class Sub2(Tool):
    def __init__(self):
        self.method = 99


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




