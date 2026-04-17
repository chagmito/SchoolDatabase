class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

    @classmethod
    def find_student(cls, student_id):
        for student in cls.student_list:
            if student.get_student_id() == student_id:
                return student
        return None

    @classmethod
    def view_all_students(cls):
        if not cls.student_list:
            print("No students found.")
        else:
            for student in cls.student_list:
                student.view_student_info()


class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

        StudentDatabase.add_student(self)

    def get_student_id(self):
        return self.__student_id

    def enroll_student(self):
        if self.__is_enrolled:
            print(f"Student {self.__student_id} is already enrolled.")
        else:
            self.__is_enrolled = True
            print(f"Student {self.__student_id} has been enrolled.")

    def drop_student(self):
        if not self.__is_enrolled:
            print(f"Student {self.__student_id} is not enrolled.")
        else:
            self.__is_enrolled = False
            print(f"Student {self.__student_id} has been dropped.")

    def view_student_info(self):
        print(f"ID: {self.__student_id}, Name: {self.__name}, "
              f"Department: {self.__department}, Enrolled: {self.__is_enrolled}")



s1 = Student("S101", "Alice Smith", "Computer Science", True)
s2 = Student("S102", "Bob Johnson", "Mathematics", False)
s3 = Student("S103", "Charlie Lee", "Physics", True)



while True:
    print("\n--- Student Management Menu ---")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        StudentDatabase.view_all_students()

    elif choice == "2":
        sid = input("Enter Student ID to enroll: ")
        student = StudentDatabase.find_student(sid)

        if student:
            student.enroll_student()
        else:
            print("Invalid Student ID.")

    elif choice == "3":
        sid = input("Enter Student ID to drop: ")
        student = StudentDatabase.find_student(sid)

        if student:
            student.drop_student()
        else:
            print("Invalid Student ID.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")