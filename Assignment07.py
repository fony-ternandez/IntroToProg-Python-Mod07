# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data

#Create a Person Class
#Add first_name and last_name properties to the constructor
class Person:
    """Represents a person with a first and last name."""

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha():
            self._first_name = value
        else:
            raise ValueError("First name must contain only letters.")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha():
            self._last_name = value
        else:
            raise ValueError("Last name must contain only letters.")

    # Override the __str__() method to return Person data
    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nCourse: {self.course_name}"

# Create a Student class the inherits from the Person class
class Student(Person):
    """Represents a student enrolled in a course."""


    # TODO call to the Person constructor and pass it the first_name and last_name data (Done)
    def __init__(self, first_name: str = "", last_name: str = "", course_name: str = ""):
        super().__init__(first_name, last_name)
        self.course_name = course_name  # add an assignment to the course_name property using the course_name parameter (Done)

    @property
    def course_name(self):
        return self._course_name  # add the getter for course_name (Done)

    @course_name.setter
    def course_name(self, value: str):
        if value.strip():
            self._course_name = value  # add the setter for course_name (Done)
        else:
            raise ValueError("Course name cannot be empty.")

    # Override the __str__() method to return the Student data (Done)
    def __str__(self):
        return f"{super().__str__()}, Course: {self.course_name}"



# Processing --------------------------------------- #
class FileProcessor:
    """A collection of processing layer functions that work with JSON files."""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads data from a JSON file into a list of Student objects."""
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                for item in data:
                    student = Student(item["first_name"], item["last_name"], item["course_name"])
                    student_data.append(student)
        except FileNotFoundError:
            print(f"File {file_name} not found. Starting with an empty list.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes a custom message for each student's registration to a JSON file."""
        try:
            with open(file_name, "w") as file:
                # Create a list of registration messages
                messages = [f"{student.first_name} {student.last_name} is now registered for {student.course_name}!"
                            for student in student_data]
                json.dump(messages, file, indent=4)  # Save messages with indentation

            print(f"Data successfully saved to {file_name}")
        except Exception as e:
            print(f"Error writing to file: {e}")

# Presentation --------------------------------------- #
class IO:
    """Handles input and output tasks."""

    @staticmethod
    def output_menu(menu: str):
        """Displays the menu of choices."""
        print(menu)

    @staticmethod
    def input_menu_choice():
        """Gets the menu choice from the user."""
        return input("Enter your menu choice number: ").strip()

    @staticmethod
    def input_student_data(student_data: list):
        """Prompts the user to enter student data and outputs a custom registration message."""
        try:
            first_name = input("Enter the student's first name: ").strip()
            last_name = input("Enter the student's last name: ").strip()
            course_name = input("Enter the course name: ").strip()
            student = Student(first_name, last_name, course_name)
            student_data.append(student)
            print("-" * 50)
            print(f"{student.first_name} {student.last_name} is now registered for {student.course_name}!")
            print("-" * 50)
        except ValueError as e:
            print(f"Error: {e}")
        return student_data

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """Displays all students and their courses."""
        print("-" * 50)
        if student_data:
            for student in student_data:
                print(f"{student.first_name} {student.last_name} is registered for {student.course_name}.")
            print("-" * 50)
        else:
            print("No students are currently registered.")
            print("-" * 50)

# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file


FileProcessor.write_data_to_file(FILE_NAME, students)
students = FileProcessor.read_data_from_file(FILE_NAME, students)

while True:
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        students = IO.input_student_data(students)
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
    elif menu_choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
