# Exercise A - Predict the Output:

a = 10
b = 3.5
c = "10"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Predict the Output:
# Write Answers here:
# a - <class = 'int'>
# b - <class = 'float'>
# c - <class = 'str'>
# d - <class = 'bool'>

# Exercise B:

age = 25
age = "25"

print (age + age)

# What Happens?
# Write answers here:
# Answer: '2525'

# I am not certain, but with concatenation, you can do this? I am thinking this
# an example of reassignment and contatenation. It gets reassinged on Line 2 but
# since it is a string, it will output as 2525


# Exercise 3 - Find the Error

height = 164.5
weight = "91.3"

bmi = weight / (height / 100) ** 2

print(bmi)

# Write answers here:
# I don't think this program will execute successfuly, due to a TypeError,
# height is considered an integer, whereas weight is considered a string, hence it would stop
# executing at the arithmetic line. In order to fix it, you need to remove the quotation marks from 
# variable "weight". You can also use the type conversion tool where you can change it to:
# weight = float(weight), this can convert it to a float as well

# Exercise D - Apply what you've learned
# Create four variables representing a person:
# Name, Age, Height in cm, Wether they're currently learning Python

name = "user"
age = 25
height = 170
is_learning_python = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_learning_python))

print(name)
print(age)
print(height)
print(is_learning_python)

