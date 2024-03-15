class Student:
    def __init__(self, id, name, DoB):
        self.__id = id
        self.__name = name
        self.__DoB = DoB

    def input(self):
        self.__id = input("Enter student ID: ")
        self.__name = input("Enter student name: ")
        self.__DoB = input("Enter student date of birth (dd/mm/yyyy): ")

    def list(self):
        print(f"ID: {self.__id}, Name: {self.__name}, DoB: {self.__DoB}")

    # Accessor methods for private attributes
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def input(self):
        self.__id = input("Enter course ID: ")
        self.__name = input("Enter course name: ")

    def list(self):
        print(f"ID: {self.__id}, Name: {self.__name}")

    # Accessor methods for private attributes
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
class System:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_number_of_students(self):
        n = int(input("Enter the number of students: "))
        for _ in range(n):
            student = Student(None, None, None)
            student.input()
            self.students.append(student)

    def input_number_of_courses(self):
        n = int(input("Enter the number of courses: "))
        for _ in range(n):
            course = Course(None, None)
            course.input()
            self.courses.append(course)

    def select_course_and_input_marks(self):
        self.list_courses()
        course_id = input("Select a course by ID to input marks: ")
        for student in self.students:
            mark = input(f"Enter mark for student {student.id} {student.name}: ")
            self.marks.append({"student_id": student.id, "course_id": course_id, "mark": mark})

    def list_students(self):
        print("Students:")
        for student in self.students:
            student.list()
 
    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            course.list()

    def show_student_marks_for_a_given_course(self):
        course_id = input("Enter course ID to show marks: ")
        print(f"Marks for course ID {course_id}:")
        for mark in self.marks:
            if mark["course_id"] == course_id:
                student_name = next(student.name for student in self.students if student.id == mark["student_id"])
                print(f"Student ID: {mark['student_id']}, Name: {student_name}, Mark: {mark['mark']}")

def main():
    system = System()
    system.input_number_of_students()
    system.input_number_of_courses()
    system.select_course_and_input_marks()
    print("\n")
    system.list_students()
    print("\n")
    system.list_courses()
    print("\n")
    system.show_student_marks_for_a_given_course()

if __name__ == "__main__":
    main()
