a = [[1, 2], [3, 4]]

b = a.copy()

b[0] = [100, 200]
b[1].append(5)

print(a)
print(b)

# Answer expected results here:

# a = [[1,2], [3,4]]
# b = a.copy()
# b = [[1,2], [3,4]]

# b[0] = [100,200]
# b = [[100,200], [3,4]]

# b[1].append(5)
# b = [[100,200], [3,4,5]]

# 1 - print(a)
# a = [[100,200] , [3,4]]

# 2 - print(b)
# b = [[100,200], [3,4,5]]

# 3 - b[0] is different to b[1] because of the function being used.
# when using the .copy() function, it creates a shallow copy of the entire object, the outer list is copied, however the inner or nested list (if any), are independent
# hence when using the reassignment of b[0] = [100,200], it mirrored the object reference from a, so it effectively reassigns both a and b objects.
# However, when using append, the original is unaffected because it modifies the outer list, which is independently copied?

# Guided Answer Response:
# The correct output is:

# a = [[1, 2], [3, 4, 5]]
# b = [[100, 200], [3, 4, 5]]

# Why?

# Operation #1
# b[0] = [100,200]
# This replaces the first element of the outer list (b)
# It does not modify the inner list that a[0] references.

# Operation #2
# b[1].append(5)

# This modifies the second inner list.
# Remember, a[1] and b[1] still reference the same inner list because we used a shallow copy.

# b[0] = [...] replaces an element in the outer list.
# b[1].append(...) modifies the shared inner list.
