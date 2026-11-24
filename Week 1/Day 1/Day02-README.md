# Day 02 – Frustration with Lists
*22-11-2026*

Today's session was a continuation on lists, tuples and dictionaries. Covering list manipulation such as moving within a list, using for loops, and also
understanding the loops tools such as the start:, stop: and also step size counter too.

I'm getting a little bit more comfortable with writing on Git Bash and locating my files from machine to machine. I purposefuly use three different workstations
and version control each via Git Bash, making sure to check previous git commits using "git log", fetching and pulling the newest version,  as well as 
commiting and commenting noteworthy commits for version control.

---

## What I learnt

Today was a little touch up upon different data types, consisting of strings, integers, floating point numbers as well as booleans.
I learnt about converting each to another using the respective conversion like str(), int(), float() bool().
My exercises regarding this topic above is on the "type_conversion.py" script file. It is commented with the exercise and my expected outputs.

We also continued up upon lists and I remembered about mutable and immutable objects.
The whole lists topic consisted of using list tools such as .append(), .remove() .pop() and also list slicing and indexing using the start: stop: stepsize: commands.
Nested lists as well were covered, not into depth, but loops such as a small for loop was introduced.

I learnt as well regarding the syntax of for loops within Python, quite similar to C if you choose it to be, but it can also be written more easier.
I prefer using a counter variable similar to C, maybe just because of habit, but I think this will be helpful for debugging in the future as well.


## What confused me

Lists, Lists, Lists.

**LISTS**, genuinely getting a little bit frustrated, especially with differentiating the differences when it comes to reassignments or making shallow copies.
I learnt that when you assign, or reassign an object, that it becomes a mirrored reference to that specific object.

For example
``` python

a = [100,200]
b = a

a.append(40)
print(a)
print(b)

# I learnt that the output of both of these were going to be:
# a = [100,200,40]
# b = [100,200,40]
```
HOWEVER, one thing that I genuinely don't understand now is when using the .copy() command with lists and then list manipulation through indexing.
The specific thing that I don't understand is how to differentiate what gets mirrored and what becomes separate from each list

One example of this is Exercise 3 from Claude this time around:

```python
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
```

The code above was my expected result, however when running the program through the terminal, the output for both for both (p) and (q) turn out to be:
print(p) = [[1,2], [3,4]]
print(q) = [[1,2,7], [3,4]]

My initial thought thinking was because I thought that the += means "adds its existing self" so basically in this case:
My thought process: q[0] += [7] -> q[0] = q[0] + [7]

Apparently its different in Python as it was that in C.

When Claude did the exact same question but with different variables, it was written as "a[i] = a[i] + [b]", which I thought would be the same as += but apparently not
and then the outcome from the terminal ended it becoming:
print(p) = [[1,2,7], [3,4]]
print(q) = [[1,2,7], [3,4]]

Another exercise that I genuinely got so confused with was this below:

```python

a = [[1, 2], [3, 4]]

b = a.copy()

b[0] = [100, 200]
b[1].append(5)

print(a)
print(b)
```
This was the test given to me by ChatGPT and I didn't couldn't differentiate again similar to exercises above, what gets mirrored and what stays the same.
I have written the my thought process in "lists.py" as well as GPT's reply and Claude's reply to have a different thought process when solving these types of exercises.


**Note to Self: Re-read up upon list manipulation, know the difference between how different lists work**