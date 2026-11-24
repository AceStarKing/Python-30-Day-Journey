# Exercise 1 - Predict the Output:

print('\n'"This is Exercise 1")
student = {
    "name": "Alex",
    "age": 25,
    "course": "Computer Systems Engineering"
}

print(student["name"])
print(student["age"])

student["age"] = 26
student["grade"] = "A"

print(student)

# Tell me what each print statement produces.
# print(student["name"]) -> Alex
# print(student["age"]) -> 25
# print(student["age"]) -> 26
# print(student) (name: "Alex", 26, 'course:Computer Systems Engineering", 'grade:"A"')

# Exercise 2: Dictionary Manipulation:

print('\n'"This is Exercise 2")
car = {
    "brand": "Honda",
    "model": "CR-V",
    "year": 2004
}

# Tasks:
# 1 - Print the car's brand.
# 2 - Change the year to 2020.
# 3 - Add a "colour" key with the value "Black".
# 4 - Remove the "model" key.
# 5 - Print the final dictionary.

# 1 - Print the Car's brand
print(car["brand"])

# 2 - Change the year to 2020.
car["year"] = 2020

# 3 - Add a "colour" key with the value "Black".
car["colour"] = "Black"

# Remove the "model" key.
car.pop("model")

print(car)

# Exercise 3 - Independent Coding

# Create a dictionary representing an AI / ML project with these keys:
# project_name
# language
# framework
# status

# print each value individually

# Bonus: check whether "framework" exists before acessing it.

print('\n'"This is Bonus Exercise")
project_AI_ML = {
    "project_name" : None,
    "language" : None,
    "framework" : None,
    "status" : None
}

print(project_AI_ML)

if "framework" in project_AI_ML:
    print("Framework exists")
else:
    print("Framework does note exist")

# The code above satisfies the exercise in its entirety above, though I know this is not expected, I took everything literally. 
# I will do bonus section for myself here with values (you did not assign values so yeah)

# Extra:
# Add a "projects" value for "project_name" with the value "Robotics" , "Forgery_Detection", "Object_Detection".
# Add languages "Python and Java into languages"
# Add Tensorflow and PyTorch into framework
# Change status to "In Progress"
# Add new key-value pair of OS as Windows
# Append "Email_Fraud_Detection" into project_name
# Remove the last language in "languages and store it into "removed languages"
# Using .pop(), remove "framework" from "project_AI_ML".
# Print the removed languages
# Check if framework still exists
# Print the new dictionary

print('\n'"This is Bonus Bonus Exercise")
project_AI_ML["project_name"] = ["Robotics","Forgery_Detection", "Object_Detection"]
project_AI_ML["language"] = ["Python", "Java"]
project_AI_ML["framework"] = ["Tensorflow", "PyTorch"]
project_AI_ML["status"] = ["In Progress"]
project_AI_ML["OS"] = ["Windows"]

project_AI_ML["project_name"].append("Email_Fraud_Detection")
removed_languages = project_AI_ML["language"].pop()
project_AI_ML.pop("framework")

if "framework" not in project_AI_ML:
    framework = project_AI_ML.get("framework", "Framework TBD")

print(removed_languages)

print(framework)

print(project_AI_ML)