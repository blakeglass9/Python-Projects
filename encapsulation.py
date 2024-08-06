class Student:
    def __init__(self, first_name, last_name, phone_number, email, course):
        # Public attributes
        self.first_name = first_name
        self.last_name = last_name

        # Protected attributes (prefix with a single underscore)
        self._phone_number = phone_number
        self._email = email

        # Private attributes (prefix with double underscores)
        self.__course = course

    # Protected method (prefix with a single underscore)
    def _display_protected_info(self):
        return f"Phone Number: {self._phone_number}, Email: {self._email}"

    # Private method (prefix with double underscores)
    def __get_course(self):
        return self.__course

    # Public method to access private information in a controlled manner
    def get_student_info(self):
        protected_info = self._display_protected_info()
        course_info = self.__get_course()
        return f"Name: {self.first_name} {self.last_name}\n{protected_info}\nCourse: {course_info}"

# Create an instance of Student
student = Student("John", "Doe", "123-456-7890", "john.doe@example.com", "Mathematics")

# Accessing public attributes
print(f"First Name: {student.first_name}")
print(f"Last Name: {student.last_name}")

# Accessing protected attribute directly (not recommended)
print(f"Phone Number (Direct Access): {student._phone_number}")
print(f"Email (Direct Access): {student._email}")

# Accessing private attribute directly (will raise an error)
try:
    print(f"Course (Direct Access): {student.__course}")
except AttributeError as e:
    print(e)

# Accessing private attribute through a public method
print(student.get_student_info())

# Accessing protected method (not recommended)
print(student._display_protected_info())
