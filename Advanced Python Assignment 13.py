#!/usr/bin/env python
# coding: utf-8

# Q1. Can you create a programme or function that employs both positive and negative indexing? Is there any repercussion if you do so?

# In[3]:


list1 =[1,2,3,4,78,9,89,100,6,98,200]
def positive_negative_indexing(list1,position):
    return (list1[position])
print('positive indexing--->',positive_negative_indexing(list1,5))
print('negative indexing -->',positive_negative_indexing(list1,-2))


# Q2. What is the most effective way of starting with 1,000 elements in a Python list? Assume that all elements should be set to the same value.

# In[9]:


#using for loop we can set same value to no of elements 
list1=[1 for ele in range(0,1001)]
print(list1)


# Q3. How do you slice a list to get any other part while missing the rest? (For example, suppose you want to make a new list with the elements first, third, fifth, seventh, and so on.)

# In[16]:


my_list = [x for x in range(1,15)]
print(f'my_list -> {my_list}')
sliced_list = my_list[::2]
print(f'sliced_list -> {sliced_list}')


# Q4. Explain the distinctions between indexing and slicing ?

#  Indexing is used when we have to work on index level. While slicing are used over a range of items.

# In[17]:


my_list = [x for x in range(1,15)]
print(f'my_list -> {my_list}')
print(f'Example of indexing -> {my_list[1], my_list[5]}')
print(f'Example of slicing -> {my_list[1:5]}')


# Q5. What happens if one of the slicing expression's indexes is out of range?

# if one of the slicing expression's index is out of range will return empty list 

# In[20]:


print(my_list[14:])


# Q6. If you pass a list to a function, and if you want the function to be able to change the values of the list—so that the list is different after the function returns—what action should you do?

# In[23]:


def modify(in_list):
    in_list.append(200)
    in_list.remove(1)
    return(in_list)
in_list=[1,2,3]
modify(in_list)


# Q7. What is the concept of an unbalanced matrix?

# A matrix is balanced if all cells in the matrix are balanced and a cell of the matrix is balanced if the number of cells in that matrix that are adjacent to that cell is strictly greater than the value written in this cell. 
# Adjacent cell means cells in the top, down, left, and right cell of each cell if it exists. 

# Q8. Why is it necessary to use either list comprehension or a loop to create arbitrarily large matrices?

#  List comprehension or a Loop helps creation of large matrices easy. it also helps to implemeent and avoid manual errors. it also makes reading code easy. Also lot of time for manual feeding is reduced.

# In[ ]:




