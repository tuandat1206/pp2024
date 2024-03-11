# 1.student.mark.py

# Global data storage
students = []
courses = []
marks = []

# Input functions
def input_number_of_students():
    return int(input("Enter the number of students: "))

def input_student_information():
    for _ in range(input_number_of_students()):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        DoB = input("Enter student date of birth (dd/mm/yyyy): ")
        students.append({"id": id, "name": name, "DoB": DoB})

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_information():
    for _ in range(input_number_of_courses()):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses.append({"id": id, "name": name})

def select_course_and_input_marks():
    list_courses()
    course_id = input("Select a course by ID to input marks: ")
    for student in students:
        marks.append({
            "student_id": student["id"],
            "course_id": course_id,
            "mark": input(f"Enter mark for student {student['id']} {student['name']}: ")
        })

# Listing functions
def list_courses():
    print("Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def list_students():
    print("Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['DoB']}")

def show_student_marks_for_a_given_course():
    course_id = input("Enter course ID to show marks: ")
    print(f"Marks for course ID {course_id}:")
    for mark in marks:
        if mark["course_id"] == course_id:
            student_name = next(student["name"] for student in students if student["id"] == mark["student_id"])
            print(f"Student ID: {mark['student_id']}, Name: {student_name}, Mark: {mark['mark']}")

# Main function to run the program
def main():
    input_student_information()
    input_course_information()
    select_course_and_input_marks()
    print("\n")
    list_students()
    print("\n")
    list_courses()
    print("\n")
    show_student_marks_for_a_given_course()

if __name__ == "__main__":
    main()
