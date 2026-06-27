# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions with
# structured error handling
# New concepts: the use of functions, classes, and using
# the separation of concerns pattern (+docstrings)
# Change Log: (Who, When, What)
# thcov,6/17/2026,Created script from starter (version 3)
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

# Define the variables
students: list = []  # a table of student data
menu_choice: str = "" # Holds the choice made by the user.

# Beginning of functions definitions
# Processing ----------------------------------------#
class FileProcessor:
    """A collection of processing layer functions that work
    with processing JSON files

    ChangeLog: (Who, When, What)
    thcov,6/17/2026,Created class
    thcov,6/17/2026,Added function: write_data_to_file
    thcov,6/17/2026,Added function: read_data_from_file"""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """This function reads the data from JSON file and loads it to
        student_data two-dimensional list of dictionary rows using the
        json.load() function.

        ChangeLog: (Who, When, What)
        thcov,6/17/2026,Created function

        :param file_name: JSON file to read from
        :type file_name: string
        :param student_data: to be loaded with the file data
        :type student_data: list of dict rows
        :return: a new list containing the loaded JSON data
        :rtype: list of dict rows"""
        file = None

        # Provides error handling when file is read into list of dict rows.
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
        except Exception as e:
            message = "Error: There was a problem loading the file data into the program.\n"
            message += "Please check to make sure the file exists and is a json file."
            IO.output_error_messages(message=message,error=e)
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """This function writes the contents of 'student_data' to a file
        using the json.dump() function.

        ChangeLog: (Who, When, What)
        thcov,6/17/2026,Created function

        :param file_name: JSON file to write the data to
        :type file_name: string
        :param student_data: contains the data to save to the file
        :type student_data: list of dict. rows
        :return: None"""
        file = None

        # Provides error handling when dict. rows are written to file
        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent=2)
            print("Successfully saved data to file.")
            print("The file contains the following data:")
            IO.output_student_courses(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            IO.output_error_messages(message=message,error=e)
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()

# Presentation ----------------------------------------#
class IO:
    """A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    thcov,6/17/2026,Created class
    thcov,6/17/2026,Added output_error_messages
    thcov,6/17/2026,Added output_menu
    thcov,6/17/2026,Added input_menu_choice
    thcov,6/17/2026,Added output_student_courses
    thcov,6/17/2026,Added input_student_data"""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """This function outputs custom error messages to the user

        ChangeLog: (Who, When, What)
        thcov,6/17/2026,Created function

        :param message: custom error message to display (string)
        :param error: Exception with technical information to display to user
        :return: None"""
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """This function displays the Course Registration Program
        menu to the user

        ChangeLog: (Who, When, What)
        thcov,6/17/2026,Created function

        :param menu: the string of the Course Registration Program menu
        :type menu: string
        :return: None"""
        print(menu)

    @staticmethod
    def input_menu_choice():
        """This function gets a menu selection from the user
        Valid return options include: '1', '2', '3', or '4'

        ChangeLog: (Who, When, What)
        thcov,6/17/2026,Created function

        :return: user's menu selection
        :rtype: string"""
        choice = "0"
        while True:
            try:
                choice = input("Please make a menu selection: ")
                if choice not in ("1", "2", "3", "4"):
                    raise Exception("Invalid menu selection. Please enter 1, 2, 3, or 4.")
                return choice
            except Exception as e:
                IO.output_error_messages(message=str(e), error=e)

    @staticmethod
    def output_student_courses(student_data: list):
        """This function displays to the user a string of comma-separated values
        for each row in student_data.

        ChangeLog: (Who, When, What)
        thcov,6/17/2026,Created function

        :param student_data: the student data to display to user
        :type student_data: list of dict. rows
        :return: None"""
        print("-" * 50)
        for student in student_data:
            print(f'{student["FirstName"]},'
                  f'{student["LastName"]},{student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """This function captures the student's first name, last name,
        and course from the user

        ChangeLog: (Who, When, What)
        thcov,6/17/2026,Created function

        :param student_data: to be filled with user's input data
        :type student_data: list of dict. rows
        :return: current data + user's input data
        :rtype: list of dict. rows"""
        # Provides error handling when user enters first name.
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            # Provides error handling when user enters last name.
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="Error: There was a problem processing your data. Please try again.", error=e)
        except Exception as e:
            IO.output_error_messages(message="There was a problem with the data you entered.", error=e)
        return student_data

# End of function definitions

# Beginning of main body of the script
# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
