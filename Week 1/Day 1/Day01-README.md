# Day 01 – Back to the Basics
*18-11-2026*

Today's session was all about the pure fundamentals of Python: what Python is, what an interpreter does, the basics of programming, and a first look at variables, objects and data types.

I also spent some time getting comfortable with Git Bash again and setting up my environment in VSCode. I'm going to try to use Git Bash exclusively in the VSCode terminal, to simulate a work environment as best I can.

---

## What I learnt

I finally understand the difference between low-level and high-level programming. High-level languages abstract a lot away so they're easier for humans to read and write. Low-level languages give little to no abstraction, which means more direct control over hardware and memory and faster execution, but at the cost of being harder to read and maintain. High-level languages trade some raw speed for readability and easier maintenance.

Python being high-level, it was easy to jump back into. Today was about variables, which are how we store information.

## What confused me

Mutable vs immutable objects, and reassignment.

**Reassignment** doesn't change the original object. It points the name at a new one:

```python
a = 10
b = a

print(a)  # 10
print(b)  # 10

a = 20

print(a)  # 20
print(b)  # 10
```

Python doesn't modify the integer `10`. It binds `a` to a new object, `20`, and `b` keeps pointing at `10`. So reassigning `a` has no effect on `b`.

**Mutable vs immutable.** Immutable means you can't change the contents of an existing object, and mutable means you can.

- Immutable: integers, floats, strings, tuples
- Mutable: lists, dictionaries

This is the one that tripped me up:

```python
a = [10, 20, 30]
b = a

a.append(40)

print(a)  # [10, 20, 30, 40]
print(b)  # [10, 20, 30, 40]
```

`b = a` doesn't create a new, independent list. Both names refer to the same list object. `append` changes that object itself, and since `a` and `b` both point at it, both show the change.

Still to remember: reassigning a name and mutating an object are two different things.