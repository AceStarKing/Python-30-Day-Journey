a = [[1, 2], [3, 4]]

b = a.copy()

b.append([9, 9])

b[0].append(7)


print(a)
print(b)

# What would be the output here?

# a = [[1,2], [3,4]]
# b = a.copy()
# b = [[1,2], [3,4]]

# b.append([9,9]) -> Add another house address onto phonebook analogy?

# b = [[1,2], [3,4], [9,9]] 

# b[0].append(7) -> Changes the shared house (adds a room '7' onto house index[0])? (not sure if analogy is correct)

# b = [[1,2,7], [3,4], [9,9]]
# a = [[1,2,7], [3,4]]

# Exercise 2: Prediction

x = [[1, 2], [3, 4]]
y = x.copy()
y[0] = y[0] + [7] # From Claude -> The + here makes a new list, rather than adding a room to the existing one.
print(x)
print(y)

# What would be the output here?
# Which of your two categories does that fall into when adding the new list?
# Add your reasoning

# x = [[1, 2], [3, 4]]
# y = x.copy()
# y = [[1, 2], [3, 4]]

# y[0] = y[0] + [7] 
# y = [[1,2,7], [3,4]] 
# (I believe this is the output of y because of the + 7, it basically appends to index[0] referenced by y[0])
# .append() would simply add the list onto the end of the object y.

# print(x) = [[1,2], [3,4]]
# print(y) = [[1,2,7], [3,4]]

# The reason why I believe x was not affected was because y was the shallow copy of (x) originally from using x.copy()
# However, the reasoning else above this simple point, I'm not too sure why. All I know is that it was a shallow copy, I'm not sure why
# it wasn't affected.
# In this case, for the analogy, y's address book was the only one affected to add a room to house index[0].

# Claude's answer response:

# Shallow copy isn't the reason "x" is safe. A shallow copy is exactly what makes inner lists shared.
# What protexts "x" here is what the line does:
# y[0] + [7] builds a brand new list [1,2,7]: a new house. It copies the contents of the old house
# and adds the 7. The old house [1,2] is not touched.
# y[0] = ... then writes the new house's address into y's own address book. Replacing the old address.

# x[0] still points at the old house [1,2], which nobody changed.

# Exercise 3:

print('\n'"This is Exercise 3")
p = [[1, 2], [3, 4]]
q = p.copy()
q[0] += [7]
print(p)
print(q)


# What do you expect the output to be:

# p = [[1,2], [3,4]]
# q = p.copy()
# q = [[1,2], [3,4]]

# q[0] += [7]

# q = [[1,2,7], [3,4]]

# print(p) = [[1,2], [3,4]]
# print(q) = [[1,2,7], [3,4]]