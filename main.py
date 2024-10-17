# 1-misol
# import json
# data = {
#     "Ism": "John",
#     "Yosh": 15,
#     "Ism_1": "Alice",
#     "Yosh_1": 14
# }
#
# with open("data.json", "w") as file:
#     json.dump(data, file, indent=4)
#
# keys = ['Ism', 'Yosh', 'Ism_1', 'Yosh_1']
# for i in range(0, len(keys), 2):
#     print(f"Ism: {data[keys[i]]}, Yosh: {data[keys[i+1]]}")


# 2-misol chala
# import json
# yangi_talaba = {
#     "name": "Tom",
#     "age": 13
# }
#
# try:
#     with open("students.json", "r") as file:
#         students = json.load(file)
# except FileNotFoundError:
#     students = []
#
# students.append(yangi_talaba)
#
# with open("students.json", "w") as file:
#     json.dump(students, file, indent=4)
#
# for student in students:
#     print(f"Ism: {student['name']}, Yosh: {student['age']}")

# 3-misol
# with open("tasks.txt", "w") as file:
#     file.write("1. Finish homework\n")
#     file.write("2. Clean the room\n")
#     file.write("3. Read a book\n")
#
# with open("tasks.txt", "r") as file:
#     tasks = file.read()
#     print(tasks)

# 4-misol
# with open("books.txt", "w") as file:
#     file.write("Harry Potter, J.K. Rowling\n")
#     file.write("The Hobbit, J.R.R. Tolkien\n")
#     file.write("Pride and Prejudice, Jane Austen\n")
#
# with open("books.txt", "r") as file:
#     books = file.readlines()
#
# search_title = input("Qiqirmoqchi bo'lgan kitob nomini kiritng:")
#
# found = False
# for book in books:
#     title, author = book.strip().split(", ")
#     if title.lower() == search_title.lower():
#         print(f"Book: {title}, Author: {author}")
#         found = True
#         break
#
# if not found:
#     print("Bunday kitob topilmadi.")

# 5-misol
# import json
# malumotlar = [
#     {"name": "John", "grades": [80, 90, 85]},
#     {"name": "Alice", "grades": [95, 88, 87]}
# ]
#
# with open("grades.json", "w") as file:
#     json.dump(malumotlar, file, indent=4)
#
# with open("grades.json", "r") as file:
#     students = json.load(file)
#
# for student in students:
#     name = student['name']
#     grades = student['grades']
#     average_grade = sum(grades) / len(grades)
#     print(f"Name: {name}, Average Grade: {average_grade:.2f}")














