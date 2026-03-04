# Data Structure (List,tuple,set, and dictionaries)

# List (ordered data, changeable/mutable, []used, duplicate values)
# Tuple (ordered, immutable, ()used, duplicate values)
# Dictonaries (key:value, , no duplicate values, changeable but keys will remain unique, unordered) QKV(query key value-like AI)
# set (unordered, unique values, {}used, immutable, no duplicate values)

# Tasks:

# Q1: Create a list of 8 colors. Print: First color, Last color & Third color
color=["red","blue","pink","grey","black","white","yellow","golden"]
print(color[0],color[7],color[2])

# Q2: A list is given: fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"] Print:
# • "Mango" using indexing
# • "Apple" using negative indexing
# • "Grapes" using negative indexing
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print(fruits[2])
print(fruits[-5])
print(fruits[-1])

# Q3: Create a list of 6 numbers. Print:
# • Second number
# • Second last number
# • Middle number
import statistics
numbers=[2,4,6,8,10,12]
mid_num=statistics.median(numbers)
print("second number is:",numbers[1])
print("second last number is:",numbers[4])
print("Middle number is:",mid_num)

# Q4: data = [5, 10, 15, 20, 25] What will be the output of?
# For print(data[1]) output will be 10
# For print(data[-3]) output will be 15
# For print(data[0]) output will be 5

# Q5: A given list is: numbers = [1, 2, 3, 4, 5]
# • Change 3 to 30
# • Change last element to 50
# • Print updated list
numbers=[1,2,3,4,5]
numbers[2]=30
numbers[4]=50
print("Updated list=",numbers)

# Q6: Create an empty list called numbers. Add 5 integers using append() function and print the list.
numbers=[]
for i in range(1,6):
    numbers.append(i)
print(numbers)

# Q7: Here is the given list: fruits = ["Apple", "Banana", "Mango"] Insert four more fruits in the list using insert() function and then print the final list
# Syntax of insert():
# Insert(“index”, “value”)
fruits = ["Apple", "Banana", "Mango"]
fruits.insert(3,"Grapes")
fruits.insert(4,"Plums")
fruits.insert(5,"Melon")
fruits.insert(6,"Orange")
print(fruits)

# Q8: Make a list of different datatypes and using remove function remove all the integers present in the list.
list = ["abc", 34, True, 40.1, 99, "Female", 67]
for i in list:
    if type(i) is int:
        list.remove(i)
print(list)

# Q9: Create a tuple named numbers with 5 integers. Print the tuple, first element and the last element using the negative indexing.
numbers=(5,10,15,20,25)
print("first element is:",numbers[0],"\nlast element is:",numbers[4])
      
# Q10: Given tuple: marks = (90, 80, 70, 90, 60, 90) Count how many times 90 appears
marks = (90, 80, 70, 90, 60, 90)
num=marks.count(90)
print(num)

# Q11: Given tuple is data = (10, 20, 30, 40, 50, 60)
# • Print the second last element using negative indexing.
# • Print the middle element (without counting manually).
# • Print the sum of the first and last element.
data = (10, 20, 30, 40, 50, 60)
import statistics
middle_term=statistics.median(data)
sum = data[0]+data[5]
print("Second last element is:",data[4],"\nMiddle element is:",middle_term,"\nSum is:",sum)

# Q12: Given list is data = [5, 15, 25, 35, 45]
# • Multiply the first and last element
# • Add the result to the list
# • Print the updated list
data = [5, 15, 25, 35, 45]
multiply=data[0]*data[4]
data.append(multiply)
print(data)

# Q13: Given list is values = [1, 2, 3, 4, 5, 6, 7, 8]
# • Print the first half of the list
# • Print the second half
# • Print elements from index 2 to 5
# • Reverse the list using slicing
values = [1, 2, 3, 4, 5, 6, 7, 8]
print("First half of list is:",values[0:4],"\nSecond half of list is:",values[4:])
print("Index from 2 to 5 is:",values[1:5])
print("Reversed list is:",values[::-1]) 

# Q14: Given list is numbers = [2, 4, 6, 2, 8, 2, 10]
# • Count how many times 2 appears
# • Find the index of the first 8
# • Add the count value at the end of the list
numbers = [2, 4, 6, 2, 8, 2, 10]
print(numbers.index(8))
print(numbers.count(2))
numbers.append(numbers.count(2))
print(numbers)