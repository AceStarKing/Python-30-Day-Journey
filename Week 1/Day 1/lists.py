fruits = ["Apple", "Banana", "Orange", "Mango"]

print(fruits[0])
print(fruits[-1])

fruits.append("Grapes")
fruits[1] = "Watermelon"

print(fruits)
print(len(fruits))

# Answer these questions:
# 1. What does fruits[0] return?
# 2. What does fruits[-1] return?
# 3. What happens when we execute fruits[1] = "Watermelon"?
# 4. What does len(fruits) do?
# 5. Why can we modify fruits[1] without creating an entirely new list?
# Try predicting first, then run it in VS Code and compare.

# 1. - fruits[0] returns "Apple" - reason being, Python uses a zero based indexing, hence it will return the first thing on the list
# 2. - fruits[-1] returns "Mango" - reason being, Python can use reverse indexing, hence it will return the last thing on the list.
# 3. - fruits[1] returns list index #1 to be changed from "Banana" to "Watermelon", this is a case of reassignment
# 4. - What does len(fruits) do? len allows us to see the length or the amount of items we have in the list, hence it will print how many is in the list
# 5. - We can modify fruits[1] without creating an entirely new list because lists are mutable objects in Python, so they can be changed and manipulated.

#Expected resutls:
# "Apple"
# "Mango"
# "Apple, Watermelon, Orange, Mango, Grapes"
# 5

### Section 2: List Slicing and Iteration

# Exercise 1: Predict the output

print('\n'"This is Exercise 1 Section")

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])
print(numbers[:3])
print(numbers[-2:])
print(numbers[::-1])

# Answer these questions:
# 1. What does numbers[1:4] return?
# [20,30,40] - list slicing uses the start:stop method, however, the stop index value is referenced, but not included when slicing during hence only 3 numbers are printed

# 2. What does numbers[:3] return?
# [10, 20, 30] - this print does not index the start function, hence it will start from index 0, the value of the stop index is referenced, but not included when printing.

# 3. What does numbers[-2:] return?
# [50, 60] - The -ve starting index accesses the list in reverse, and the value of that -ve value starts how many steps from the end of the list to start
# since there is no stop index value, it will print until the list is iterated.

# 4. What does numbers[::-1] return?
# [60, 50, 40, 30, 20, 10] - This prints the list reversed. The start and stop index values are default, so it will print the whole entire list. The third index value is the step value,
# which is -1, hence it will print the list in reverse order, it is also the step size.

# Exercise 2: Understanding Mutations
# What will the final list look like?

print('\n'"This is Exercise 2 Section")
fruits2 = ["Apple", "Banana", "Orange"]

fruits2.append("Grapes")
fruits2.insert(1, "Mango")
fruits2.remove("Orange")

removed_fruit = fruits2.pop()

print(fruits2)
print(removed_fruit)

# Answer these questions:
# Explain what is happening in each step.

# Line 1: Object "fruits2" gets initialzied into a list containing ["Apple", "Banana", "Orange"]
# Line 2: fruits2.append("Grapes") reassigns fruits2 lists and adds "Grapes" into the last value of the list, so the list looks like: ["Apples", "Banana", "Orange", "Grapes"]
# Line 3: fruits2.insert(1, "Mango") reassigns fruit2 lists and adds "Mango" into index value [1]. So the list looks like: ["Apple", "Mango", "Banana", "Orange", "Grapes"]
# Line 4: fruits2.remove("Orange") reassigns fruit2 lists and removes "Orange" within the list, it looks for its match and removes it. So the list looks like: ["Apple," "Mango", "Banana", "Grapes"]
# Line 6: removed_fruit = fruits2.pop() removes the last index value from list "fruits2" and initializes removed_fruit into the object containing the contents of that removed value

# print(fruits) - ["Apple", "Mango", "Banana"]
# print(removed_fruit) - "Grapes"

# Exercise 3: Independent coding

# Create a list containing five numbers of your choice.

# Write a program that:
# 1. Prints the entire list.
# 2. Prints the first two elements using slicing.
# 3. Prints the last two elements using negative indexing.
# 4. Adds another number to the list.
# 5. Removes one number from the list.
# 6. Iterates through the list and prints every remaining number.
# Bonus: Print the sum of all the numbers using Python's built-in sum() function.

print('\n'"This is Exercise 3 Section")

my_list = [3, 7, 13, 16, 21, 23]

print('\n'"This is my list:",my_list)
print('\n'"This is the first two elements using slicing of my list:", my_list[:2:])
print('\n'"This is the last two elements using negative indexing:", my_list[-2:])

my_list.append(25)
my_list.remove(13)

for i in range(len(my_list)):
    print('\n'"I am printing my list, here is my current value:", my_list[i])


print('\n'"The sum of my list is:" , sum(my_list))

popped_value = my_list.pop(-1)

print('\n'"I removed this value from my list:", popped_value)
print('\n'"I have added a bonus section of pop, my new summation of my list is:", sum(my_list))
