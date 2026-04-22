# count the no of students

nums = int(input("Enter total students:"))

# data storage

studentsData = []

# inserting data

for i in range(nums):
    print(f"denter data of students {i+1}:")
    name = input("name")
    roll_no = int(input("roll no"))
    marks = int(input("marks"))

    if marks > 95:
        grade = "A"
    elif marks > 80:
        grade = "B"
    elif marks > 70:
        grade = "C"
    elif marks >= 33:
        grade = "D"
    else:
        grade = "F"

    students = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "grade": grade
    }

    studentsData.append(students)

# printing data
print("all students' data: \n")

for s in studentsData:
    print(f"{s['name']}  - roll no: {s['roll_no']} -marks: {s['marks']}  - grade:{s['grade']}")


# passed students
print("\n student who passed :")

print("\n students who passed :")

for s in studentsData:
    if s["marks"] >= 33:
        print(f"{s['name']} - marks: {s['marks']} - grade: {s['grade']}")