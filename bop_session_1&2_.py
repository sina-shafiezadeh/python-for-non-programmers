# -*- coding: utf-8 -*-
"""BoP_session_1&2 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Is88Sxxei5vfjoAjLy-7d-sYPRURA938

# BASICS OF PYTHON | SESSION 1&2

---
Sina Shafiezadeh | April 2023
---

# FAQ

1.   what is programming?

  Programming refers to the process of designing and writing instructions that a computer can understand and execute. It involves creating code using a specific programming language to create software programs, applications, and scripts that can perform various tasks.

2.   what is object-oriented programming?

  Object-oriented programming (OOP) is a programming paradigm that is based on the concept of objects, which can contain data and methods that act on that data. In OOP, objects are instances of classes, which define the structure and behavior of the objects.

3. what is Python?

  Python is a high-level, interpreted programming language that is widely used for web development, scientific computing, data analysis, artificial intelligence, and many other applications. It was created by Guido van Rossum and first released in 1991.

4. why should I learn Python?

*   Versatility: Python can be used for a wide range of applications, including web development, scientific computing, data analysis, artificial intelligence, machine learning, and many more.
*   Simplicity: Python has a simple syntax and is easy to read and write, making it a good choice for beginners.
*   Large community: Python has a large and active community of developers who create third-party libraries and tools, making it easy to find solutions to common problems.
*   Open-source: Python is free and open-source, which means that you can use it for any purpose without having to pay for it.
*   Simplicity

5. how can I install Python?

*   Go to the official [Python](https://www.python.org/downloads/) website and the [Anaconda](https://www.anaconda.com/) website.
*   Or using the [Google Colab](https://colab.research.google.com/).
*   Or any other tools that you want.

6. what is Google Colab?

  Google Colab (short for Collaboratory) is a free online platform provided by Google that allows users to run Python code and execute Jupyter notebooks directly in the cloud. It is a popular tool for data scientists, machine learning engineers, and researchers who want to develop and experiment with machine learning models without the need for specialized hardware.

7. Do you have more questions?

  Ask from [chatGPT](https://chat.openai.com/chat) as I asked to provide previous answers, connect with others in [stackoverflow](https://stackoverflow.com/), search your concerns in Google, and watch a lot of useful videos on Youtube for free!

# Content


*   Day 1:

  *   Create Variables
  *   Conditional Statements
  *   Loops

*   Day 2:

  *   Data Structure
  *   Algorithm

*   Day 3:

  *   Data Importing
  *   Data Cleaning
  *   Data Exploring

*   Day 4:

  *   Data Analysis
  *   Data Visualization
  *   Data Exporting

*   Day 5:

  *   Exam

LET'S START!

# 1.&nbsp;Create Variables

Create a variable with the name `course` and assign the value `"basic of python"` after using the `=` sign to the computer to remember information.
"""

course = "basic of python"

"""we can expand variable names with **Snake Case** format for naming that each word is separated by an underscore character."""

my_course = "basic of python"

"""or using **Camel Case** format for naming that each word, except the first, starts with a capital letter."""

myCourse = "basic of python"

"""or using **Pascal Case** format that each word starts with a capital letter."""

MyCourse = "basic of python"

"""Be careful! Python is a **case-sensitive** programming language, so `MyCourse` and `mycourse` are two different variables."""

mycourse

"""Besides, we can't use **space** for the variable's name."""

My Course = "basic of python"

"""However, it's better to choose a variable's name to help us understand what's inside a variable. In our case, it's easier to change the variable's name to `course_name`."""

course_name = "basic of python"

"""Finally, we can also define a variable name using **numbers**. It sometimes could be very useful."""

course_1_name = "basic of python"
course_2_name = "cognitive neuroscience"

"""Great! Let's look at the value on the right side. We store words in double quotes `"   "`, therefore it is a **string**. Strings can contain all sorts of letters and symbols."""

course_name = "Basic of python!"

"""We tell the computer to display a value by `print()` in the console, also known as the shell."""

print(course_name)

"""we can repeat `print()` as often as we want and display every value on a line."""

print("=================================")
print("The course's name is:")
print(course_name)
print("=================================")

"""Before continuing this part, let's look at an important point. Python is an **interpreted language** and It means code is run there line by line. Please correct the following code."""

print(universiy_name)
universiy_name = "university of padova"

"""We can use this point to update variables. Please guess what will display in the console before running the code.

"""

course_name = "cognitive neuroscience"
print(course_name)
course_name = "basic of python"
print(course_name)

"""We can add string values together with the `+` sign."""

print("course name: " + "basic of python")
print("course name: " + course_name)

"""Let's cross strings. We can store a **number** in a variable without using `"   "`."""

course_score = 80

"""Add numbers together by `+`."""

course_score = 80 + 10
print(course_score)

"""Subtract the numbers by `-`."""

course_score = 80 - 10
print(course_score)

"""Multiply numbers by `*`."""

course_score = 80 * 0.5
print(course_score)

"""Or divided by `/`."""

course_score = 80 / 8
print(course_score)

"""Modulus by `%`."""

course_score = 8 % 5
print(course_score)

"""Exponentiation by `**`."""

course_score = 8 ** 2
print(course_score)

"""And floor division is calculated by `//`."""

course_score = 8 // 5
print(course_score)

"""Keep the variable's value and change only the console by manipulating the `print()`."""

course_score = 80
print(course_score / 8)
print(course_score)

"""Calculate results and store them in variables. Notice when we want to print a string and a number together in the `print()`, we must use `,` instead of `+` or using f-strings like `f" {} "` to add a variable in a string."""

homework_1_score = 40
homework_2_score = 45
course_score = homework_1_score + homework_2_score
print("course score: " , course_score)
print(f"course score:  {course_score}")

"""Here is a question. How can we understand the type of our variable? the answer is using `type()`."""

course_score = 80
print(type(course_score))

course_score = 80.0
print(type(course_score))

course_score = "80"
print(type(course_score))

"""Another question: How can we specify a variable type? The answer is casting by `int()`, `float()`, and `str()`."""

course_1_score = int(80)   # will be 80
course_2_score = int(80.7) # will be 80 (not 81)
course_3_score = int("80") # will be 80

course_4_score = float(80)   # will be 80.0
course_5_score = float(80.7) # will be 80.7
course_6_score = float("80") # will be 80.0
course_7_score = float("80.2") # will be 80.2

course_8_score = str(80)   # will be '80'
course_9_score = str(80.7) # will be '80.7'

print("course_1_score:", course_1_score, "\t", type(course_1_score)) # "\t" add space between outputs
print("course_2_score:", course_2_score, "\t", type(course_2_score))
print("course_3_score:", course_3_score, "\t", type(course_3_score))
print("course_4_score:", course_4_score, "\t", type(course_4_score))
print("course_5_score:", course_5_score, "\t", type(course_5_score))
print("course_6_score:", course_6_score, "\t", type(course_6_score))
print("course_7_score:", course_7_score, "\t", type(course_7_score))
print("course_8_score:", course_8_score, "\t", type(course_8_score))
print("course_9_score:", course_9_score, "\t", type(course_9_score))

"""Before finishing this part, let's review two important general points. First, Python uses **indentation** to indicate a block of code. Indentation refers to the spaces at the beginning of a code line. Please correct the following code."""

course_score = 80
  print(course_score)

"""Secondly, we can use `#` to add **comments** to our code. This helps with the readability and documentation of our code."""

# the range of course scores is between 0 and 100
course_score = 80
print(course_score)

"""That's it! Let's try all the previous points to develop your first exercise.

## Exercise 1 part 1

---


Calculate your BMI score and show your name and score in the console.

*   Expected output 1: My name is Sara and my BMI score is 28.
*   Expected output 2: My name is John and my BMI score is 22.
"""

# BMI formula: weight (kg) / height**2 (m)

"""Good job!

Sometimes we need to show if a feature is switched on or off by useing `True` and `False` values.
"""

calculated_bmi = True
print(calculated_bmi)

calculated_bmi = False
print(calculated_bmi)

"""Besides, we need to compare two values."""

bmi_score = 28
print(bmi_score == 28) # equal
print(bmi_score != 28) # not equal
print(bmi_score > 28)  # greater than
print(bmi_score < 28)  # less than
print(bmi_score >= 28) # greater than or equal to
print(bmi_score <= 28) # less than or equal to

"""Maybe logical operators to combine conditional statements."""

bmi_score = 28
print(bmi_score > 20 and bmi_score > 30) # returns True if both statements are true
print(bmi_score > 20 or bmi_score > 30) # returns True if one of the statements is true
print(not(bmi_score > 20 and bmi_score > 30)) # reverse the result, returns False if the result is true

"""## Exercise 1 part 2

---


Check whether your BMI score is normal or not. 

*   Expected output 1: True
*   Expected output 2: False




"""

# normal range is from 18.5 to 24.9

"""# 2.&nbsp;Conditional Statements

We use the **if statement** to adapt to different situations. Notice to use `:` after the statement and indentation before `print()`.
"""

bmi_score = 28

if bmi_score < 18.8:
  print("BMI score is under weight.")
else:
  print("BMI score is not under weight.")

"""Maybe we have more than one condition."""

bmi_score = 28

if bmi_score > 18.5 and bmi_score < 24.9:
  print("BMI score is normal.")
else:
  print("BMI score is not normal.")

bmi_score = 28

if bmi_score < 18.5 or bmi_score > 24.9:
  print("BMI score is not normal.")
else:
  print("BMI score is normal.")

"""Or we have more than two situations."""

bmi_score = 28

if bmi_score < 18.8:
  print("BMI score is under weight.")
elif bmi_score > 18.5 and bmi_score < 24.9:
  print("BMI score is under normal.")
elif bmi_score > 25 and bmi_score < 29.9:
  print("BMI score is over weight.")
elif bmi_score > 30 and bmi_score < 39.9:
  print("BMI score is obesity.")
else:
  print("BMI score is extreme obesity.")

"""## Exercise 2

---


We want to predict the BMI score after doing sport routing over one year. Assume the one-month sport reduces the 0.38 value from the BMI score. What will happen to BMI score if someone does sports for 3, 6, 9, and 12 months?

*   Expected output 1: BMI score will be 27.76 after 3 months of sports.
*   Expected output 2: BMI score will be 24.91 after 12 months of sports




"""

# try with different values
bmi_score = 28.4
sport_duration = 9

"""# 3.&nbsp;Loops (while)

Using the `while` loop, we can execute a set of statements if a condition is true.
"""

bmi_score = 21.4

while bmi_score < 25:
  print(f"your BMI score is {bmi_score} (normal range).")
  bmi_score += 1 # bmi_score = bmi_score + 1

"""If the while condition is true, the `break` statement will prevent the loop from continuing indefinitely."""

bmi_score = 21.4

while bmi_score < 25:
  print(f"your BMI score is {bmi_score} (normal range).")
  bmi_score -= 1 # bmi_score = bmi_score - 1
  if bmi_score < 18.8:
    break

"""Or if the condition is no longer true, an `else` statement will run a block of code once."""

bmi_score = 21.4

while bmi_score > 18.8:
  print(f"your BMI score is {bmi_score} (normal range).")
  bmi_score -= 1
else:
  print(f"your BMI score is {bmi_score} (under weight).")

"""The `continue` statement lets us stop the current iteration and move on to the next."""

bmi_score = 19

while bmi_score < 25:
  bmi_score += 1
  if bmi_score == 22:
    continue
  if bmi_score >= 25:
    break
  print(f"your BMI score is {bmi_score} (normal range).")

"""## Exercise 3

---

We assumed the one-month sport reduce by 0.38 value from the BMI score. Now, write a `while` loop to calculate the maximum number of months to reach the normal range for BMI score.

*   Expected output 1: you need 3 months of sport
*   Expected output 2: you need 7 months of sport




"""

# try different BMI score
bmi_score = 28.6
sport_duration = 0

"""# 4.&nbsp;Loops (for)

Excellent! Let's look at the `for` loop.

Using the `for` loop means we know how many times we need to execute a statement, so we can use it when we know how many iterations there will be. In addition, `range()` returns a sequence of numbers starting from 0 and incrementing by 1 by default, and ending at a specified number. Although, we can change default values if we want.
"""

bmi_score = 19

for i in range(3):

  print(f"your BMI score is {bmi_score} (normal range).")
  bmi_score += 1

"""Besides, while loop's statements including the `break`, `continue`, and `else` could be used here as well."""

bmi_score = 19

for i in range(5):
  bmi_score += 1
  if bmi_score == 22:
    continue
  print(f"your BMI score is {bmi_score} (normal range).")

bmi_score = 19

for i in range(6):
  print(f"your BMI score is {bmi_score} (normal range).")
  bmi_score += 1
  if bmi_score == 25:
    break

bmi_score = 19

for i in range(6):
  print(f"your BMI score is {bmi_score} (normal range).")
  bmi_score += 1
else:
  print(f"your BMI score is {bmi_score} (under weight).")

"""## Exercise 4

---
 

Similar to the previous exercise we assumed the one-month sport reduce 0.38 value from the BMI score. Now, write a `for` loop to calculate finalized BMI score after 7 months of sports.

*   Expected output 1: your BMI score will be 21.93 after 7 months of sport
*   Expected output 2: your BMI score will be 26.77 after 7 months of sport


"""

# try different BMI score
bmi_score = 28.6
sport_duration = 7

"""# 5.&nbsp;Data Structure (string and list)

For organization, management, and storage data we need to know different data types and how to work with them. We familiarize ourselves with **integers**, **floats**, and **booleans** before.
"""

x = 18 # int
y = 24.9 # float
z = True # boolean

"""We are also familiarized with **string** but let's deep in a little bit on that."""

w = "this is a string"
print(type(w)) # get data type

print(len(w)) # get length

# access item by position
# note: position in Python starts at 0.
print("position 0 : ", w[0])
print("position 1 : ", w[1])
print("position -2: ", w[-2])
print("\n") # create a new line
print("range of position 1: ", w[1:3])
print("range of position 2: ", w[:3])
print("range of position 3: ", w[3:])
print("range of position 4: ", w[:])
print("range of position 5: ", w[-3:-1])
print("range of position 6: ", w[:-1])
print("range of position 7: ", w[-3:])

# check if item exists
if "this" in w:
  print("Yes, this is in w string.")

print(w.upper()) # upper case

print(w.lower()) # lower case

print(w.replace("this", "that")) # replace

print(w.split(" ")) # split by space

"""Perfect!

Let's continue with another data type. Using **lists**, we can store multiple items with any type of data in one variable by using `[]` and `,` between items.
"""

student = ["name", "Weight", "Height", 21.7, True]
print(student)

print(type(student)) # get data type

print(len(student)) # get length

# access item by index
# note: indexing in Python starts at 0.
print("index 0 : ", student[0])
print("index 1 : ", student[1])
print("index -2: ", student[-2])
print("\nrange of index 1: ", student[1:3]) # notice to \n
print("range of index 2: ", student[:3])
print("range of index 3: ", student[1:])
print("range of index 4: ", student[:])
print("range of index 5: ", student[-3:-1])
print("range of index 6: ", student[:-1])
print("range of index 7: ", student[-3:])

# check if item exists
if "Height" in student:
  print("Yes, Height is in the student list.")

# change item value by index
print(student)
student[3] = 21.4
student[1:3] = ["weight", "height"]
print(student)

# insert item value by index
student.insert(1, "surname")
print(student)

# append item value to the end of the list
student.append("age")
print(student)

# append items from another list to current list
education = ["course", "score"]
student.extend(education)
print(student)

# append and extend difference
list_one = [1, 3, 5, 7]
list_two = [9, 11]
list_one.append(list_two)
print("appended list: ", list_one)

list_one = [1, 3, 5, 7]
list_two = [9, 11]
list_one.extend(list_two)
print("extended list: ", list_one)

# remove by item value
student.remove("course")
print(student)

# remove by index
student.pop(-2)
print(student)

# the pop() method removes the last item if you don't specify the index
student.pop()
print(student)

# another way to remove by index
del student[1]
print(student)

# loop through a list
for i in student:
  print(i)

# loop through the index numbers
for i in range(len(student)):
  print(student[i])

# removes all the items from the list
student.clear()
print(student)

# looping using list comprehension (shortest syntax)
bmi = [21.31, 26.9, 24.1, 29.4]
student_bmi = [i+1 for i in bmi]
print(student_bmi)

# sort items
student_bmi.sort() # ascending
print(student_bmi)
student_bmi.sort(reverse = True) # descending
print(student_bmi)

"""## Exercise 5

---


1. Calculate the BMI score for all patients and store it in a list. (Hint: for loop)
2. Remove items in the normal range.  (Hint: if statement)
3. Sort items by descending.

*   Expected output:
        [28.202947845804992,
         27.517517248785204,
         25.342529883586657]


"""

patient_name = ["Georgia", "Oscar", "Juliet", "Lily", "William"]
patient_weight = [54.7, 79.6, 81.2, 51.9, 102.5] # kg
patient_height = [152, 168, 179, 161, 193] # cm
patient_bmi = []

# start from here...

"""# 6.&nbsp;Data Structure (tuple, set and dictionary)

We can group together closely-related data unchangeable using **tuples**. We create them similarly to lists but using parentheses `()` instead of brackets.
"""

thistuple = ("Georgia", 54.7, 152, False)
print(type(thistuple))

print(len(thistuple))

tuple_one_item = ("Georgia",)
print(type(tuple_one_item))

# it is NOT a tuple
tuple_one_item = ("Georgia")
print(type(tuple_one_item))

# access item by index
print("index 0 : ", thistuple[0])
print("index 1 : ", thistuple[1])
print("index -2: ", thistuple[-2])
print("=================================")
print("range of index 1: ", thistuple[1:3])
print("range of index 2: ", thistuple[:3])
print("range of index 3: ", thistuple[1:])
print("range of index 4: ", thistuple[:])
print("range of index 5: ", thistuple[-3:-1])
print("range of index 6: ", thistuple[:-1])
print("range of index 7: ", thistuple[-3:])

# check if item exists
if "Georgia" in thistuple:
  print("Yes, Georgia is in thistuple.")

"""Tuples are **unchangeable**, therefore we should convert them to a list to change, add, or remove an item."""

thislist = list(thistuple) # convert to a list
thislist[0] = "Oscar" # change an item
thislist.append("Brown") # add an item
thislist.remove(152) # remove an item
thistuple = tuple(thislist) # convert to a tuple
print(thistuple)

"""The next data type is **set**. We use a set like a list but use `{}` to make sure values can't have any **duplicates**."""

thisset = {"Georgia", 54.7, 152, False, False}
print(type(thisset))

print(len(thisset)) # remove duplicated False

"""We can not refer to set items by index or key, because sets are **unordered** and they can appear in a different order each time you use them."""

print(thisset)

"""Although we can't change values, we are able to **add** or **remove** new values."""

thisset.add("Brown")
thisset.remove(54.7)
print(thisset)

"""Let's familiarize ourselves with another data type called **dictionary**. A dictionary consists of **keys** and **values** and is written in curly brackets `{}`."""

thisdict = {"name": ["Georgia"],
            "bmi": 21.5,
            "normal": True}
print(type(thisdict))

print(len(thisdict))

# get all the keys
print(thisdict.keys())

# get all the values
print(thisdict.values())

# get all the items in tuples
print(thisdict.items())

# access item by key name
print(thisdict["bmi"])

# check if key exists
if "name" in thisdict:
  print("Yes, name is one of the keys in the thisdict")

thisdict["name"] = "Oscar" # change an item
thisdict["surname"] = "Brown" # add an item
thisdict.pop("bmi") # remove an item
print(thisdict)

"""## Exercise 6

---


1. Calculate the BMI score for all patients and store their **name** and **BMI score** in patients_info dictionary.
2. Remove items in the normal range.

*   Expected output:
        patients_info = {"name": ["Oscar","Juliet","William"],
                          "bmi": [28,25,27]}

"""

patient_name = ["Georgia", "Oscar", "Juliet", "Lily", "William"]
patient_weight = [54.7, 79.6, 81.2, 51.9, 102.5] # kg
patient_height = [152, 168, 179, 161, 193] # cm
patients_info = {"name":[]
                 ,"bmi":[]}

# start from here...

"""# 7.&nbsp;Data Structure (module and array)

The last data type we want to know is an **array**. However, we need to know about the **module** first to work with arrays in Python easier.

Modules group related classes and methods to be accessible from one place.

In the following, we import the [numpy](https://numpy.org//) package and modify its name into np to use easier later. Numpy is the fundamental package for scientific computing with Python.
"""

import numpy as np

"""We can access an array's values by referring to its index number, and arrays can hold many values."""

# set the seed for reproducibility
np.random.seed(42)

# generate 20 random float values between 18 and 32
bmi_array = np.random.uniform(18, 32, size=20)

print(type(bmi_array))

print(bmi_array)

print(len(bmi_array))

# access item by index
print("index 0 : ", bmi_array[0])
print("index 1 : ", bmi_array[1])
print("index -2: ", bmi_array[-2])
print("=================================")
print("range of index 1: ", bmi_array[1:3])
print("\nrange of index 2: ", bmi_array[:3])
print("\nrange of index 3: ", bmi_array[1:])
print("\nrange of index 4: ", bmi_array[:])
print("\nrange of index 5: ", bmi_array[-3:-1])
print("\nrange of index 6: ", bmi_array[:-1])
print("\nrange of index 7: ", bmi_array[-3:])

# 1D array with 5 elements between 18 to 30
arr_1d = np.random.randint(18,30,size=(3))
print(arr_1d.shape)
print(arr_1d)

# 2D array with 3 rows and 4 columns
arr_2d = np.random.randint(18,30,size=(3, 2))
print("==================")
print(arr_2d.shape)
print(arr_2d)


# 3D array with 2 planes, 3 rows, and 2 columns
arr_3d = np.random.randint(18,30,size=(2, 3, 5))
print("==================")
print(arr_3d.shape)
print(arr_3d)

"""## Exercise 7

---


1. Create two arrays for weight and height with 5 float random values.
2. Calculate the BMI score and store it in a list called **calculated_bmi**, at the same time, indicate whether a BMI value is normal or not and store it in a list called **evaluated_bmi**.


*   Expected output 1:
        calculated_bmi:
        [23,28,25,20,27]

        evaluated_bmi:
        ["yes","no","no","yes","no"]

*   Expected output 2:
        calculated_bmi:
        [21,20,22,24,28]

        evaluated_bmi:
        ["yes","yes","yes","yes","no"]
"""

# select a reasonable weight and height range as you want
np.random.seed(42)

# start from here...

"""# 8.&nbsp;Algorithm (function)

**Algorithms** define a set of actions that must be performed in a specific step by step to produce the desired result.

**Functions** help us to implement algorithms. Functions are blocks of code that only run when they are called in situations where we want to reuse existing code without rewriting it.
"""

# define a function
def first_function():
  print("this is my first function.")

# call a function
first_function()

"""We can write our algorithm inside a function and pass value to it."""

def first_function(x):
  x = x + 3
  return x

first_function(x=4)

"""More than one argument we can use in functions."""

def first_function(x,y):
  z = x + y
  return z

first_function(x=4,y=2)

"""It's better to start a function name with a **verb** that explains what will happen in a function."""

def get_sum(x,y):
  z = x + y
  return z

get_sum(x=4first_function(x=4))

"""We can set a default value for arguments."""

def get_sum(x,y=3):
  z = x + y
  return z

get_sum(x=4)

def get_sum(x,y=3):
  z = x + y
  return z

get_sum(x=4,y=2)

"""We can also pass a list to the arguments."""

def get_sum(x,y):
  z = x + y
  return z

x = [3,2,7]
y = [1,4]
get_sum(x,y)

"""Or using loops and conditional statements inside functions."""

def get_square(x,y):
  z = x + y
  if len(z) == 0:
    print("your list is empty!")
  else:
    for i in z:
      j = i**2
      print(f"i = {i} and j = {j}")

x = [3,2,7]
y = [1,-4]
get_square(x,y)

"""## Exercise 8

---


1. Define a function to calculate BMI score.
2. Store BMI scores into the bmi_score list.
3. Sort items  by descending.

*   Expected output:
        bmi_score = [23.68, 28.20, 25.34, 20.02]
"""

# patient = [weight(kg), height(cm)]
patient1 = [54.7, 152]
patient2 = [79.6, 168]
patient3 = [81.2, 179]
patient4 = [51.9, 161]
bmi_score = []

# start from here...

"""# 9.&nbsp;Algorithm (class)

There are many properties and methods in an **object** in Python, and almost everything is an object. **Classes** are like object constructors; we use them to group data and functionality. Functions belonging to objects are called **methods**.
"""

def get_square(x,y):
  z = x + y
  if len(z) == 0:
    print("your list is empty!")
  else:
    for i in z:
      j = i**2
      print(f"i = {i} and j = {j}")

x = [3,2,7]
y = [1,-4]
get_square(x,y)

class Price:
  def __init__(self, value, discount):
    self.value = value
    self.discount = discount

  def summer(self):
    summer_price = round(self.value - (self.value * (self.discount/100)), 2)
    print(summer_price)

  def winter(self):
    winter_price = round(self.value - (self.value * (self.discount * 2/100)), 2) #double discount
    print(winter_price)

#create variables from the class (Price is a "definition" and shoes_price is an "instance")
shoes_price = Price(115, 18) # price 115 euro and 18% discount
shoes_price.summer()
shoes_price.winter()

"""## Exercise 9

---


1. Define a class called BMI and three methods including converting pound to kg, inch to cm, and calculating BMI score.
2. Calculate BMI score for 3 given patients and store them in the bmi_score list.

*   Expected output:
        bmi_score = [23.49, 27.98, 25.14, 19.86]
"""

# 1 pound ≈ 0.45 kg
# 1 inch ≈ 2.54 cm
# patient = [weight(pond), height(inch)]
patient1 = [120.59, 59.84]
patient2 = [175.49, 66.14]
patient3 = [179.02, 70.47]
patient4 = [114.42, 63.39]
bmi_score = []

# start from here...

"""# 10.&nbsp;Algorithm (error and exception)

If Python can't understand your code, we will get an **error**! However, we can find our error location by finding `^` in an error message.
"""

# syntax error
x = 5
if > 3:
  print("Hello")

# syntax error
x = 5
iif x > 3:
  print("Hello")

# missing indentation error
x = 5
if x > 3:
print("Hello")

"""On the other hand, sometimes Python understands our code, but can't execute it. Therefore, it raises an **exception**. The text in the console is called **traceback** and it helps us to **debug** our code."""

# name error
height = cm / 100

# type error
height = 100 + "56"

# zero division error
height = 156 / 0

# module not found error
import numpyy

"""Be careful! Sometimes a module exists but we need to install it."""

!pip install mne
import mne # package for human neurophysiological data analysis

# index error
height = [149, 187, 168]
height[3]

"""We can use errors and exceptions to debug our code. Besides, we can use them to avoid **unwanted issues**."""

# test 1: run the code and see the results
# test 2: add "184" to "student_height" and run the code
# test 3: remove "184" from "student_height" and change "179" into "0" and run the code

student_name = ["Georgia", "Oscar", "Juliet", "Lily", "William"]
student_weight = [54.7, 79.6, 81.2, 51.9, 102.5]
student_height = [152, 168, 179, 161, 193]
student_bmi = []

# make sure about data size
if len(student_weight) != len(student_height):
  raise Exception("There must be equal size for weights and hights")

for i in range(len(student_name)):
  # make sure height is not zero
  if student_height[i] == 0:
    raise ValueError("height can not be zero")

  student_bmi.append(round(student_weight[i] / ((student_height[i]/100)**2), 1))

print(student_bmi)

"""Sometimes we don't want to raise an exception and we want to handle it. For example, we want a `for` loop to continue at the end of the code by ignoring negative values for weight, therefore we can use `try` and `except`."""

student_name = ["Georgia", "Oscar", "Juliet", "Lily", "William"]
student_weight = [54.7, 79.6, 81.2, 51.9, 102.5]
student_height = [-152, 168, 0, 161, 193]
student_bmi = []


for i in range(len(student_name)):
  
  try:
    student_bmi.append(round(student_weight[i] / ((student_height[i]/100)**2), 1))
  
  except:
    continue

print(student_bmi)

"""## Exercise 10

---


1. Copy your exercise 9 code.
2. Set a **type error** to check the heights have float values.
3. Set a value error to make sure the BMI score is not negative.

"""

# 1 pound ≈ 0.45 kg
# 1 inch ≈ 2.54 cm
# patient = [weight(pond), height(inch)]
patient1 = [120.59, 59.84]
patient2 = [175.49, 66.14]
patient3 = [179.02, 70.47]
patient4 = [114.42, 63.39]
bmi_score = []

# past your code here...

"""Congratulations! You did it.

# References and Resources:

1. You can continue your learning by more complex data structure and algorithm tasks in [Leetcode](https://leetcode.com/). 

2. you can always have access to Python syntax and practical examples in [w3schools](https://www.w3schools.com/python/default.asp) and [geeksforgeeks](https://www.geeksforgeeks.org/python-programming-language/).

3. You can find everything about Numpy to work with arrays [HERE](https://numpy.org/doc/stable/index.html#) and you can also utilize all APIs and documents about Pandas to work with data frames [HERE](https://pandas.pydata.org/docs/index.html#).
"""