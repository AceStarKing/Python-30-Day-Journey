# Small Independent Challenge
# Create a simple BMI Calculation using these starting values
# Remember to convert height from centimetres into metres first


# name = "Alex"
# age = "25"
# height = "164.5"
# weight = "91.3"

# Your program should:
# Convert age into an integer.
# Convert height and weight into floats.
# Calculate BMI using BMI = weight / (height)^2

# Print the person's name, age and BMI
# Print the data type of each converted variable.

name = "Alex"
age = "25"
height = "164.5"
weight = "91.3"

print("Before Conversion")
print(type(name)) 
print(name)
print(type(age))
print(age)
print(type(height))
print(height)
print(type(age))
print(weight ,'\n')


age = int(age)
height = float(height) / 100 # This converts height from cm to metres
weight = float(weight)

BMI = weight / (height * height) # This formula was given

print("After Conversion")
print(type(name))
print(name)
print(type(age))
print(age)
print(type(height))
print(height)
print(type(age))
print(weight)
print(type(BMI))
print("BMI for Alex is:", BMI)

#