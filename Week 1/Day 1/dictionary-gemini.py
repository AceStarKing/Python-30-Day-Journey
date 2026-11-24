student_profile = {
    "name": "Maya",
    "year": 1,
    "major": "Computer Science",
    "gpa": 3.4
}

# Dictionary Exemplar with GeminiGPT:

# Your 3 Tasks

# 1 - Add a new key-value pair for "club" with the value "Robotics".
# 2 - Update "gpa" to 3.7 (and let me know whether this adds a key or modifies an existing one).
# 3 - Remove "year" using .pop(), 
# 4 - save the removed value in a variable called old_year, 
# 5 - and print both the updated student_profile and old_year.

student_profile["club"] = "Robotics"
# This adds a new key-value pair for dictionary "student_profile". It is new because their is no existing
# key for "club" and it has been specified to pair with value:"Robotics"

student_profile["gpa"] = 3.7
# This does not add a new key, it modifies the existing "gpa" key and updates the existing value to 3.7

old_year = student_profile.pop("year")
# Using the .pop(key) on dictionary "student_profile" removes it from the dictionary, and assigns
# it to object "old_year"

print(student_profile)
print(old_year)


# Exercise 2:

course_info = {
    "code": "COMPENG201",
    "credits": 15
}

# Tasks:
# 1 - Use .get() to safely read "lab_room" from "course_info", returning "TBD" if
#                   "lab_room" is missing, and store it in "lab"

# 2 - Use .pop() to safely remove "tutor" from "course_info", returning "None" if 
#                   "tutor" is missing, and store it in "removed_tutor"

# 3 - print "lab", "removed_tutor", and "course_info", and explain in your comments why
#                   neither lines crashes even though lab_room and tutor aren't in course_info

if "lab_room" not in course_info:
    lab = course_info.get("lab_room", "TBD")

if "tutor" not in course_info:
    removed_tutor = course_info.pop("tutor", None)

print(lab)
print(removed_tutor)
print(course_info)

# Note: I am not sure if I should have used "if" statements to complete this exercise, the reason why
# I instinctively used the if statement is from the task itself "If (...) is missing", hence 
# why I ended up just using the if statement to check if it was there or not, despite me explicitly knowing
# it's not there. Just me following instructions.

# Neither line crashes even though lab_room and tutors aren't in course_info. The reason behind this is because
# of the fallback? (can't remember what it's called) condition value we assigned to the stored variables.
# From our lesson earlier, if the key does not exist without the fallback value, it will crash saying KeyError or some type of error.

# Exercise 3: List & Dictionary Finisher:
print('\n\n'"This is Exercise 3")
lab_station = {
    "station_id": "FPGA-04",
    "tools": ["oscilloscope", "logic_analyzer", "multimeter"]
}

# Tasks:
# 1 - Append "soldering_iron" to the "tools' list inside "lab_station".
# 2 - Pop the last tool from "tools" into a variable called "last_tool".
# 3 - Print "last_tool" and "lab_station". Explain in your comments why mutating
#     "tools" changes "lab_station" even though you didn't write lab_stations["tools"] again.

# Task 1 - 
lab_station["tools"].append("soldering_iron")

# Appended soldering iron into tools turns dictionary lab_station to:
# lab_station = {
#     "station_id": "FPGA-04"
#     "tools": ["ossiliscope", "logic_analyzer", "multimeter", "soldering_iron"]
# }

# Task 2 -
last_tool = lab_station["tools"].pop()

# Removing last tool from lab_station[tools]
# lab_station = {
#     "station_id": "FPGA-04"
#     "tools": ["ossiliscope", "logic_analyzer", "multimeter"]
# }


# 3 - Print "last_tool" and "lab_station", and explain in your comments why 
# Mutating "tools" changes "lab_station" even though you didn't write lab_station["tools"] = ... again.

print(last_tool)
print(lab_station)

# Mutating inner list "tools" changes lab_station because the key already exists for "tools". Hence it just popped the last value
# of the "tools" list value without having to explicitly write "lab_station["tools"] = ... again."
# If key "tools" didn't exist, it would create a new key-value pair if it was assigned a value.