"""
    list, index

    -> you can get any eliment from the list by using the index of that eliment
"""
# students = ["Hermione", "Harry", "Ron"]
# print(students[0])
# print(students[1])
# print(students[2])


# students = ["Hermione", "Harry", "Ron"]
# for student in students:
#     print(student)


"""
    len : length function
"""

# students = ["Hermione", "Harry", "Ron"]
# # print(len(students))

# for i in range(len(students)):
#     print(i+1 , students[i])



"""
    dict -> dictionary : a data structure allows me to associate one value with another,
    like a dictionary in human world it's a bunch of words and definitions.
    but here, dict describe as key's and value's. something associated with something else. 
"""

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

#to get the house of hermione , use the key (hermione) rather than index to get the value of the key.
#print(students["Hermione"])

#if you use a for loop to iterate over a dictionary, it iterates over all the keys
# for student in students:
#     print(student)

# To get the value of the key's , use it as indexes to get the value

# for student in students:
#     print(student, students[student], sep=", ")


######################################################



students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Gryffindor", "patronus": None} # special keyword in puthon and that literarly means None
]

for student in students:
    print(student["name"], 
    student["house"],
    student["patronus"],
    sep=", ")


#Go to mario.py