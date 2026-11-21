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