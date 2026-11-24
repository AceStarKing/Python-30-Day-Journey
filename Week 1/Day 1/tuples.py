coordinates = (10, 20, 30, 40, 50)

print(coordinates[0])
print(coordinates[-1])
print(coordinates[1:4])
print(len(coordinates))

# Exercise 1: Predict the output

# 1 - print(coordinates[0]) = 10
# 2 - print(coordinates[-1]) = 50
# 3 - print coordinates([1:4]) = (20, 30, 40)
# 4 - print(len(coordinates)) = 5

numbers = (10, 20, 30)

# numbers[1] = 100

print(numbers)

# Exercise 2 - Predict the output

# Answer here:
# Error - (TypeError?) unsure of the error type, however, the reason why it will output an error is because
# tuples are immutable objects, reassignment like such will not work, if it were to ever work, it will just
# print (10,20,30)

# Exercise 3 - Character creation 

# Create a tuple containing:
# - Your name
# - Your age
# - Your height
# - Your current learning goal
# Then print each element individually using indexing.

print('\n'"This is Exercise 3")

character = ("Ace", 25, 164.5, "Learning Python")

print("This on one line prints using indexing:")
print(character[:])

print("This prints using for loop and indexing using range and using length of tuple:")
for i in range(len(character)):
    print(character[i])
