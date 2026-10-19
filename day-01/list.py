# skills = ["Ml", "Python", "Numpy"]

# # # print(skills[2])

# # skills[2] = "Pandas"
# # print(skills[2])

# # print(len(skills))

# # print("maths" not in skills)

# # skills.append("Maths")
# # print(skills)

# # skills.extend(["Calculus", "Stats", "Prob"])
# # print(skills)

# num = [10,30,20]
# sorted_num = sorted(num)
# print(sorted_num)

student = {
    "name": "Akif",
    "age": 20,
    "gpa": 3.94
}

# for key, value in student.items():
#     print(key, ":", value)
    
print(student.get("age"))
print(student.keys())
print(student.values())

//practice

# skills = ["Ml", "Python", "Numpy"]
languages = ["Java", "Python", "C++"]

# print(skills[2])
print(languages[2])

# skills[2] = "Pandas"
languages[2] = "JavaScript"
# print(skills[2])
print(languages[2])

# print(len(skills))
print(len(languages))

# print("maths" not in skills)
print("Ruby" not in languages)

# skills.append("Maths")
languages.append("Python")
# print(skills)
print(languages)

# skills.extend(["Calculus", "Stats", "Prob"])
languages.extend(["HTML", "CSS", "SQL"])
# print(skills)
print(languages)

# num = [10,30,20]
num = [50, 10, 30]
sorted_num = sorted(num)
print(sorted_num)

student = {
    "name": "Matee",
    "age": 24,
    "gpa": 3.45
}

# for key, value in student.items():
#     print(key, ":", value)
    
print(student.get("age"))
print(student.keys())
print(student.values())
