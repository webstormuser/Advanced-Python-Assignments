#!/usr/bin/env python
# coding: utf-8

# # 1. What is the concept of an abstract superclass?
# ANS :An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class. A class which contains one or more abstract methods is called an abstract class. An abstract method is a method that has a declaration but does not have an implementation. While we are designing large functional units we use an abstract class. When we want to provide a common interface for different implementations of a component, we use an abstract class. 
#     By default, Python does not provide abstract classes. Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC. ABC works by decorating methods of the base class as abstract and then registering concrete classes as implementations of the abstract base. A method becomes abstract when decorated with the keyword @abstractmethod

# In[11]:


from abc import ABC ,abstractmethod
class polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass
class Triangle(polygon):
    def noofsides(self):
        return "Triangle has 3 sides"
class Sqaure(polygon):
    def noofsides(self):
        return "Sqaure has 4 sides"
class Pentagon(polygon):
    def noofsides(self):
        return "Pentagon has 5 sides"
class Hexagon(polygon):
    def noofsides(self):
        return "Hexagon has 6 sides"

#p=polygon() instance can't be created since it is containing abstract method
t=Triangle()
print(t.noofsides())
s=Sqaure()
print(s.noofsides())
p=Pentagon()
print(p.noofsides())
h=Hexagon()
print(h.noofsides())


# # 2. What happens when a class statement&#39;s top level contains a basic assignment statement?
# 
# ANS :When a class statement's top level contains a basic assignment statemnts it is treated as class attribute and it is shared by all instances created by class

# In[22]:


class Person:
    nature='Kind'
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        print(f'{self.name} is {self.gender}')
P=Person("Rashmi","Female")
print("she is ",P.nature)


# # 3. Why does a class need to manually call a superclass&#39;s __init__ method?
# ANS :  if a child class has __init__ method, then it will not inherit the __init__ method of the parent class. in other words the __init__ method of the child class overrides the __init__ method of the parent class. so we have to manually call a parent superclass's __init__ using super() method

# In[26]:


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age       
class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary
emp_1 = Employee('Rashmi',28,30000)
print(emp_1.__dict__)


# # 4. How can you augment, instead of completely replacing, an inherited method?
# ANS :super() method can be used to augment, instead of completely replacing, an inherited method.

# # 5. How is the local scope of a class different from that of a function?
# ANS :The concept of scope rules how variables and names are looked up in your code. It determines the visibility of a variable within the code. The scope of a name or variable depends on the place in your code where you create that variable
#     Local scope: The names that you define in this scope are only available or visible to the code within the scope.
#         A Variable which is defined inside a function is local to that function. it is accesible from the point at which it is defined until the end of the function, and exists for as long as the function is existing.
# 
# Similary a variable inside of a class also has a local variable scope. Variables which are defined in the class body (but outside all methods) are called as class level variables or class attributes. they can be referenced by there bare names within the same scope, but they can also be accessed from outside this scope if we use the attribute access operator (.). on a class or an instance of the class.

# In[39]:


def Hello(name):
    name=name
    print(f'You\'re  name is {name}')

Hello("Ashwini")
try: 
    name 
except NameError:
    print("name is not accessible outside of function scope")
class Person:
    nature="kind"
    def __init__(self):
        pass
print(Person.nature)
p=Person()
print(p.nature)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




