original = [10, 20, 30]

copied = original

copied.append(40)

print(original)
print(copied)

original1 = [10, 20, 30]

copied1 = original1.copy()

copied1.append(40)

print(original1)
print(copied1)

# Your challenge
# Answer these four questions without running the code first:
# 1. In the first example, why does modifying copied also affect original?
# 2. In the second example, why does modifying copied NOT affect original?
# 3. What is the difference between copied = original and copied = original.copy()?
# 4. Does .copy() create an entirely independent copy of everything inside a list, including nested lists? We'll explore this last question together.

# 1 - Modifying copied also affects the original as "copied" is a makes reference to the same object, hence anything affecting the list will be mirrored to all objects referencing to that object
# 2 - The .copy() function makes a shallow copy of the object and doesn't reference to the same object, hence it won't affect its reference.
# 3 - The difference between copied = original and copied = original.copy(), this I am not 100% sure. My assumption is regarding its difference is the fact that its not referencing the object
#     it directly creates a shallow copy of the content within the object, but any changes made to that new object is independent from its referenced and mirrored object.
# 4 - I am unsure, but I think it is entirely independent copy of everything within the list, including nested lists as well. 