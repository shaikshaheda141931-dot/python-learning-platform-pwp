import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime

# =========================================================
# LOGIN DETAILS
# =========================================================
USERNAME = "shannu"
PASSWORD = "123456"

# =========================================================
# COLORS
# =========================================================
BG = "#071A33"
CARD = "#102A4A"
BLUE = "#1E5AA8"
LIGHT_BLUE = "#2E75C9"
WHITE = "#FFFFFF"
TEXT = "#DCEBFA"
GREEN = "#2EBD85"
GOLD = "#D4AF37"
GRAY = "#8FA6BF"
RED = "#E05252"

# =========================================================
# MODULES WITH DETAILED THEORY
# =========================================================
MODULES = [

    # =====================================================
    # MODULE 1
    # =====================================================
    {
        "name": "Module 1 - Python Fundamentals",
        "topics": [

            (
                "Introduction to Python",
                """Python is a high-level, general-purpose programming language.
It was created by Guido van Rossum and was first released in 1991.

Python is popular because its syntax is simple, readable and easy to understand.
It is an interpreted language, which means Python code can be executed by an
interpreter without requiring a separate compilation step in the traditional way.

Python is used in many areas such as web development, data science, artificial
intelligence, machine learning, automation, scientific computing and software
development.

Important advantages of Python include:
1. Easy and readable syntax.
2. Large standard library.
3. Supports object-oriented programming.
4. Supports procedural and functional programming.
5. Large developer community.
6. Useful libraries for AI, ML and data analysis.

Example:

print("Hello World")

The above program displays Hello World on the screen.

Python is especially useful for beginners because programs can be written using
fewer lines of code compared with many other programming languages."""
            ),

            (
                "Python Syntax",
                """Python syntax refers to the rules used to write Python programs.

Python uses indentation to identify blocks of code. Unlike languages that use
curly brackets, Python normally uses spaces or tabs to represent a block.

Example:

if age >= 18:
    print("Adult")

The print statement is indented because it belongs to the if block.

Python is case-sensitive. This means Name, name and NAME are treated as different
identifiers.

A Python statement can normally be written on a separate line.

Example:

x = 10
y = 20
print(x + y)

Python syntax is designed to be simple and readable. Correct indentation is very
important because incorrect indentation can produce an IndentationError.

Python also allows comments to be added to make programs easier to understand."""
            ),

            (
                "Variables",
                """A variable is a name used to store a value in a program.

Python does not require the programmer to explicitly declare the data type before
creating a variable. The type is determined automatically from the value assigned.

Examples:

name = "Shaheda"
age = 18
height = 5.4

Here, name stores a string, age stores an integer and height stores a floating
point value.

Variables can be changed during program execution.

Example:

age = 18
age = 19

After the second statement, age contains 19.

Variable names should be meaningful. For example, student_name is easier to
understand than simply x.

Rules for variable names:
1. A variable name can contain letters, numbers and underscore.
2. It cannot start with a number.
3. It cannot contain spaces.
4. Python keywords cannot be used as variable names.
5. Variable names are case-sensitive.

Good variable naming makes programs easier to read and maintain."""
            ),

            (
                "Data Types",
                """A data type defines the kind of value stored in a variable.

Python provides several built-in data types.

1. int
Used for whole numbers.
Example:
age = 18

2. float
Used for decimal numbers.
Example:
price = 99.50

3. str
Used for text.
Example:
name = "Shaheda"

4. bool
Stores True or False.
Example:
is_student = True

5. list
Stores multiple values in an ordered and changeable collection.
Example:
numbers = [10, 20, 30]

6. tuple
Stores multiple values in an ordered collection that is normally immutable.
Example:
data = (10, 20, 30)

7. set
Stores unique elements.
Example:
values = {1, 2, 3}

8. dict
Stores key-value pairs.
Example:
student = {"name": "Shaheda", "age": 18}

The type() function can be used to check the type of a value."""
            ),

            (
                "Operators",
                """Operators are symbols or keywords used to perform operations on values.

Arithmetic operators:
+ addition
- subtraction
* multiplication
/ division
% modulus
// floor division
** exponentiation

Example:

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)

Comparison operators are used to compare values:
== equal
!= not equal
> greater than
< less than
>= greater than or equal
<= less than or equal

Logical operators include:
and
or
not

Assignment operators include:
=
+=
-=
*=
/=

Python also supports membership operators such as in and not in.

Operators allow programmers to perform calculations, comparisons and logical
operations inside programs."""
            ),

            (
                "Input and Output",
                """Input and output are basic parts of every programming language.

The input() function is used to receive information from the user.

Example:

name = input("Enter your name: ")
print(name)

By default, input() returns data as a string.

If numerical input is required, conversion can be performed.

Example:

age = int(input("Enter your age: "))

The print() function is used to display information.

Example:

print("Welcome to Python")

Multiple values can also be printed.

Example:

name = "Shaheda"
age = 18

print(name, age)

Input allows a program to interact with the user, while output allows the
program to communicate results back to the user."""
            ),

            (
                "Comments",
                """Comments are statements written to explain the code.

Python ignores comments during program execution.

A single-line comment begins with the # symbol.

Example:

# This is a comment
x = 10

Comments are useful because they help programmers understand the purpose of
different sections of code.

Good comments should explain why something is done when the reason is not
obvious from the code itself.

Comments are especially useful in large projects where multiple programmers
work together.

Python does not execute comments, so they do not affect the output of the program."""
            ),

            (
                "Practice",
                """Practice is important for learning Python programming.

Try creating small programs using the concepts learned in this module.

Practice 1:
Create a program that accepts a student's name and age and displays them.

Practice 2:
Create a calculator that accepts two numbers and performs addition,
subtraction, multiplication and division.

Practice 3:
Create variables for student name, enrollment number, semester and CGPA.
Display all values using print().

Practice 4:
Create a program that checks the type of different variables using type().

Regular practice helps improve programming logic and makes Python syntax easier
to remember."""
            )
        ]
    },

    # =====================================================
    # MODULE 2
    # =====================================================
    {
        "name": "Module 2 - Control Flow and Functions",
        "topics": [

            (
                "if Statement",
                """The if statement is used to execute code only when a condition
is true.

Example:

age = 20

if age >= 18:
    print("Adult")

The condition age >= 18 is evaluated first. If it is true, the indented code
will execute.

Conditions normally use comparison operators such as ==, !=, >, <, >= and <=.

The if statement is important because programs often need to make decisions
based on user input or data.

Example:

marks = 75

if marks >= 40:
    print("Pass")

If the condition is false, the code inside the if block is skipped."""
            ),

            (
                "if-else",
                """The if-else statement provides two different execution paths.

If the condition is true, the if block executes. If it is false, the else
block executes.

Example:

marks = 35

if marks >= 40:
    print("Pass")
else:
    print("Fail")

The if-else structure is useful when there are exactly two main possibilities.

Another example:

age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

The decision is based on the condition provided in the if statement."""
            ),

            (
                "elif",
                """The elif keyword is used when a program needs to check multiple
conditions.

Example:

marks = 85

if marks >= 90:
    print("A+")
elif marks >= 75:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("C")

Python checks the conditions from top to bottom. Once a true condition is found,
its block is executed and the remaining conditions are skipped.

elif makes programs easier to read than writing many separate if statements.

It is commonly used in grading systems, menu-based programs and decision-making
applications."""
            ),

            (
                "for Loop",
                """A for loop is used to repeat a block of code for each item in a
sequence.

Example:

for i in range(5):
    print(i)

The range(5) produces values from 0 to 4.

A for loop can also be used with lists.

Example:

names = ["A", "B", "C"]

for name in names:
    print(name)

For loops are useful when the number of repetitions is known or when a
collection of items needs to be processed one by one.

Loops reduce repeated code and make programs shorter and easier to maintain."""
            ),

            (
                "while Loop",
                """A while loop repeats a block of code as long as its condition
remains true.

Example:

count = 1

while count <= 5:
    print(count)
    count += 1

The condition is checked before every iteration.

It is important to update the condition inside the loop. Otherwise, the program
may create an infinite loop.

While loops are useful when the number of repetitions is not known in advance
and execution depends on a condition.

Example applications include menus, input validation and repeated user actions."""
            ),

            (
                "break and continue",
                """The break and continue statements control loop execution.

The break statement immediately stops the loop.

Example:

for i in range(10):
    if i == 5:
        break
    print(i)

The loop stops when i becomes 5.

The continue statement skips the current iteration and moves to the next one.

Example:

for i in range(5):
    if i == 2:
        continue
    print(i)

In this example, 2 is skipped.

break is useful when a required result has been found. continue is useful when
some values should be ignored while the loop continues."""
            ),

            (
                "Functions",
                """A function is a reusable block of code that performs a specific
task.

Functions are defined using the def keyword.

Example:

def greet():
    print("Hello")

The function can be called using:

greet()

Functions provide several advantages:
1. Code reuse.
2. Better organization.
3. Easier testing.
4. Reduced duplication.
5. Improved readability.

A function can perform calculations, process data or return results.

Large programs are normally divided into multiple functions so that each
function performs a specific responsibility."""
            ),

            (
                "Function Parameters",
                """Parameters allow functions to receive input values.

Example:

def greet(name):
    print("Hello", name)

The function can be called as:

greet("Shaheda")

Here, name is a parameter and Shaheda is an argument.

Functions can have multiple parameters.

Example:

def add(a, b):
    print(a + b)

add(10, 20)

Parameters make functions flexible because the same function can work with
different values.

Python also supports default parameters.

Example:

def greet(name="Student"):
    print("Hello", name)"""
            ),

            (
                "Return Values",
                """The return statement is used to send a result from a function
back to the calling code.

Example:

def add(a, b):
    return a + b

result = add(10, 20)
print(result)

The returned value can be stored in a variable or used in another expression.

Returning values is useful because functions can perform calculations and give
their results to other parts of the program.

A function can return numbers, strings, lists, dictionaries or other objects."""
            ),

            (
                "Lambda",
                """A lambda function is a small anonymous function.

A normal function can be written as:

def square(x):
    return x * x

The same operation can be written using lambda:

square = lambda x: x * x

Lambda functions are generally used for short operations.

They can be useful with functions such as map(), filter() and sorted().

Because lambda functions are designed for simple expressions, regular def
functions are usually preferred when the logic becomes complex."""
            )
        ]
    },

    # =====================================================
    # MODULE 3
    # =====================================================
    {
        "name": "Module 3 - Data Structures",
        "topics": [

            (
                "List",
                """A list is an ordered and changeable collection in Python.

Example:

numbers = [10, 20, 30, 40]

Lists can contain different data types.

Example:

data = [10, "Python", 5.5, True]

Lists support indexing and slicing.

Elements can be modified:

numbers[0] = 100

Common list methods include:
append()
insert()
remove()
pop()
sort()
reverse()

Lists are useful when a program needs to store multiple values and modify them
during execution."""
            ),

            (
                "Tuple",
                """A tuple is an ordered collection that is generally immutable.

Example:

data = (10, 20, 30)

Tuples support indexing and slicing like lists, but their elements cannot
normally be changed after creation.

Tuples are useful for representing fixed collections of values.

Example:

student = ("Shaheda", 18, "AI")

Tuples can also be unpacked:

name, age, course = student

Because tuples are immutable, they can be useful when data should remain fixed."""
            ),

            (
                "Set",
                """A set is an unordered collection of unique elements.

Example:

numbers = {1, 2, 3, 4}

If duplicate values are added, the set keeps only unique values.

Example:

numbers = {1, 2, 2, 3}

The resulting set contains 1, 2 and 3.

Sets support operations such as union, intersection and difference.

They are useful when uniqueness is important or when mathematical set
operations are required.

Sets do not use normal numeric indexing like lists."""
            ),

            (
                "Dictionary",
                """A dictionary stores data using key-value pairs.

Example:

student = {
    "name": "Shaheda",
    "age": 18,
    "course": "AI"
}

Values can be accessed using their keys.

Example:

print(student["name"])

Dictionaries are mutable, so values can be changed.

Example:

student["age"] = 19

New key-value pairs can also be added.

Dictionaries are very useful for representing structured information such as
student records, employee details and configuration data."""
            ),

            (
                "Strings",
                """A string is a sequence of characters.

Example:

name = "Python"

Strings can be created using single, double or triple quotes.

Python provides many string methods such as:
upper()
lower()
strip()
replace()
split()
find()

Example:

text = "python"
print(text.upper())

Strings support indexing and slicing.

Example:

word = "Python"
print(word[0])
print(word[0:3])

Strings are immutable, meaning individual characters cannot normally be changed
directly after the string is created."""
            ),

            (
                "Indexing",
                """Indexing is used to access individual elements of a sequence.

Python uses zero-based indexing.

Example:

numbers = [10, 20, 30]

numbers[0] gives 10.
numbers[1] gives 20.
numbers[2] gives 30.

Python also supports negative indexing.

numbers[-1] gives the last element.

Indexing can be used with strings, lists and tuples.

Correct indexing is important because accessing an invalid index can produce
an IndexError."""
            ),

            (
                "Slicing",
                """Slicing is used to extract part of a sequence.

The general form is:

sequence[start:stop:step]

Example:

numbers = [0, 1, 2, 3, 4, 5]

numbers[1:4]

This returns elements from index 1 up to, but not including, index 4.

Slicing can also use a step.

Example:

numbers[::2]

This accesses every second element.

Slicing is useful for extracting parts of strings, lists and tuples."""
            ),

            (
                "Nested Data Structures",
                """A nested data structure contains another data structure inside it.

Example:

students = [
    {"name": "A", "age": 18},
    {"name": "B", "age": 19}
]

Here, a list contains dictionaries.

Another example is a dictionary containing a list:

student = {
    "name": "Shaheda",
    "subjects": ["Python", "DBMS", "Math"]
}

Nested structures are useful when representing complex real-world information.

They are commonly used in applications, APIs and data-processing programs."""
            ),

            (
                "Iteration",
                """Iteration means processing elements one by one.

The for loop is commonly used for iteration.

Example:

numbers = [10, 20, 30]

for number in numbers:
    print(number)

Dictionaries can also be iterated.

Example:

student = {"name": "A", "age": 18}

for key, value in student.items():
    print(key, value)

Iteration is one of the most important concepts when working with collections
because it allows a program to process every element systematically."""
            ),

            (
                "Practice",
                """Practice the following data structure operations.

1. Create a list containing five student names.
2. Add another name using append().
3. Remove one name.
4. Create a tuple containing course information.
5. Create a set with duplicate values and observe the result.
6. Create a dictionary containing name, age and course.
7. Use indexing to access values.
8. Use slicing to extract elements.
9. Use a loop to display all elements.

Practice with different data structures helps you understand when each
structure should be used."""
            )
        ]
    },

    # =====================================================
    # MODULE 4
    # =====================================================
    {
        "name": "Module 4 - File and Exception Handling",
        "topics": [

            (
                "File Handling",
                """File handling allows a Python program to work with files stored
on a computer.

Python provides the open() function for opening files.

Example:

file = open("data.txt", "r")

After working with a file, it should be closed.

Example:

file.close()

A better approach is to use the with statement because it automatically handles
closing the file.

Example:

with open("data.txt", "r") as file:
    data = file.read()

File handling is useful for storing information permanently instead of keeping
everything only in memory."""
            ),

            (
                "File Modes",
                """File modes define how a file should be opened.

Common modes include:

r - read
w - write
a - append
x - create

Read mode is used to access existing content.

Write mode creates or overwrites file content.

Append mode adds new content at the end of an existing file.

Example:

with open("data.txt", "w") as file:
    file.write("Hello")

Choosing the correct file mode is important because write mode can replace
existing content."""
            ),

            (
                "Reading Files",
                """Python provides several methods for reading file contents.

read() reads the complete content.

readline() reads one line.

readlines() reads multiple lines and returns them as a list.

Example:

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

Files can contain large amounts of information, so reading line by line may
sometimes be more suitable.

The with statement automatically closes the file after the operation is complete."""
            ),

            (
                "Writing Files",
                """Writing files allows programs to store information permanently.

Example:

with open("data.txt", "w") as file:
    file.write("Python Learning")

The write() method writes a string to the file.

Multiple lines can be written using newline characters.

Example:

file.write("Python\\nDBMS\\nAI")

Append mode can be used when existing content should be preserved.

Example:

with open("data.txt", "a") as file:
    file.write("\\nNew Topic")

File writing is useful for logs, reports, user information and application data."""
            ),

            (
                "CSV Files",
                """CSV stands for Comma-Separated Values.

CSV files are commonly used for storing tabular data.

Python provides the csv module to work with CSV files.

Example:

import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Shaheda", 18])

CSV files are useful for exchanging data between spreadsheets, databases and
Python programs.

They are commonly used in data analysis and simple data storage applications."""
            ),

            (
                "Exception Handling",
                """An exception is an error that occurs during program execution.

Python provides try and except blocks for handling exceptions.

Example:

try:
    number = int(input("Enter number: "))
    print(number)
except ValueError:
    print("Please enter a valid number")

Exception handling prevents unexpected errors from stopping the entire program.

Common exceptions include ValueError, TypeError, IndexError, KeyError and
FileNotFoundError.

Good exception handling makes applications more reliable and user-friendly."""
            ),

            (
                "finally",
                """The finally block contains code that should execute whether an
exception occurs or not.

Example:

try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("Operation completed")

The finally block is useful for cleanup operations such as closing resources.

It is often used together with try and except.

The finally block is executed after the try and except processing is complete."""
            ),

            (
                "raise",
                """The raise statement allows a programmer to manually generate
an exception.

Example:

age = -1

if age < 0:
    raise ValueError("Age cannot be negative")

The raise statement is useful when a program needs to validate data and stop
execution when an invalid condition is detected.

It allows programmers to create meaningful error messages.

Custom validation using raise improves the reliability of applications."""
            ),

            (
                "Logging",
                """Logging records information about the execution of a program.

Python provides the logging module.

Logging can record messages such as:
debug information
normal application information
warnings
errors
critical problems

Example:

import logging

logging.basicConfig(level=logging.INFO)
logging.info("Application started")

Logging is useful for debugging applications and understanding what happened
during execution.

Large applications commonly use logs to monitor errors and important events."""
            ),

            (
                "Practice",
                """Practice file and exception handling by creating a small student
record program.

The program can:
1. Accept student information.
2. Store information in a file.
3. Read the information.
4. Handle invalid input.
5. Display suitable error messages.
6. Store records in a CSV file.
7. Use logging for important operations.

This practice combines multiple concepts from the module and provides a good
foundation for real applications."""
            )
        ]
    },

    # =====================================================
    # MODULE 5
    # =====================================================
    {
        "name": "Module 5 - Object-Oriented Programming",
        "topics": [

            (
                "Class",
                """A class is a blueprint used to create objects.

A class can contain attributes and methods.

Example:

class Student:
    pass

The class defines the structure and behavior that objects created from it can
use.

Classes are one of the most important concepts in object-oriented programming.

They help organize large programs by combining related data and functionality
into a single unit."""
            ),

            (
                "Object",
                """An object is an instance of a class.

Example:

class Student:
    pass

student1 = Student()

Here, student1 is an object of the Student class.

Objects can have attributes that represent their data and methods that represent
their behavior.

Object-oriented programming allows real-world entities such as students,
employees, bank accounts and vehicles to be represented in software."""
            ),

            (
                "Constructor",
                """A constructor is used to initialize an object.

In Python, the __init__() method is commonly used for this purpose.

Example:

class Student:
    def __init__(self, name):
        self.name = name

student = Student("Shaheda")

When the object is created, the __init__() method executes automatically.

Constructors are useful for setting initial values for object attributes."""
            ),

            (
                "Methods",
                """Methods are functions defined inside a class.

Example:

class Student:

    def display(self):
        print("Student information")

Methods define actions that objects can perform.

The self parameter refers to the current object.

Methods can access attributes of the object and can also return values.

Using methods keeps the logic related to an object organized within its class."""
            ),

            (
                "Inheritance",
                """Inheritance allows one class to acquire properties and methods
from another class.

The existing class is often called the parent or base class, while the new
class is called the child or derived class.

Example:

class Animal:
    def sound(self):
        print("Sound")

class Dog(Animal):
    pass

Dog inherits the sound() method from Animal.

Inheritance promotes code reuse and helps create relationships between classes."""
            ),

            (
                "Encapsulation",
                """Encapsulation means combining data and methods within a class
and controlling access to internal information.

It helps protect object data from unwanted modification.

Python uses naming conventions such as a leading underscore or double
underscore for attributes that should have restricted access.

Encapsulation improves organization and makes classes easier to maintain.

It is an important principle of object-oriented programming."""
            ),

            (
                "Polymorphism",
                """Polymorphism means that the same interface or method can behave
differently for different objects.

For example, different classes may define a method named sound() but provide
different implementations.

A Dog may produce one sound while a Cat produces another.

Polymorphism allows programs to work with different object types through a
common interface.

It improves flexibility and makes code easier to extend."""
            ),

            (
                "Abstraction",
                """Abstraction means hiding unnecessary implementation details and
showing only the important features.

For example, when using a car, a driver uses the steering wheel, accelerator
and brakes without needing to know the internal engine implementation.

In programming, abstraction allows developers to focus on what an object does
rather than exactly how every internal operation works.

Abstraction reduces complexity and improves program design."""
            ),

            (
                "OOP Practice",
                """Create a Student class as practice.

The class can contain:
name
enrollment number
course
marks

Create methods such as:
display()
calculate_percentage()
show_result()

Then create multiple Student objects and test the methods.

This exercise helps understand classes, objects, attributes, constructors and
methods in a practical way."""
            ),

            (
                "OOP Mini Project",
                """A simple OOP mini project can be a Student Management System.

Possible features:
1. Add student.
2. Display student.
3. Update student.
4. Calculate marks.
5. Display percentage.
6. Search student.
7. Delete student.

The project can use classes such as Student and StudentManager.

Using OOP makes the project organized and easier to extend with new features."""
            )
        ]
    },

    # =====================================================
    # MODULE 6
    # =====================================================
    {
        "name": "Module 6 - Database and Web",
        "topics": [

            (
                "Database Concepts",
                """A database is an organized collection of information.

Databases are used to store, retrieve, update and manage data efficiently.

A relational database stores information in tables consisting of rows and
columns.

A row generally represents one record while a column represents an attribute.

For example, a Student table may contain:
Student ID
Name
Age
Course

Database systems are used in websites, banking systems, educational systems,
hospitals and business applications."""
            ),

            (
                "SQL Basics",
                """SQL stands for Structured Query Language.

SQL is used to communicate with relational databases.

Important SQL commands include:

CREATE - creates database objects.
INSERT - adds records.
SELECT - retrieves records.
UPDATE - modifies records.
DELETE - removes records.

Example:

SELECT * FROM students;

This retrieves all records from the students table.

SQL is one of the most important technologies used for database management."""
            ),

            (
                "CRUD",
                """CRUD represents four basic database operations.

C - Create
R - Read
U - Update
D - Delete

Create means adding new information.

Read means retrieving existing information.

Update means changing existing information.

Delete means removing information.

Almost every database application uses these four operations.

For example, a student management system may allow an administrator to add,
view, modify and delete student records."""
            ),

            (
                "SQLite",
                """SQLite is a lightweight relational database system.

Python includes the sqlite3 module, which allows programs to work with SQLite
databases without installing a separate database server.

Example:

import sqlite3

connection = sqlite3.connect("college.db")

A database connection is used to create tables and execute SQL statements.

SQLite is useful for small applications, learning projects, desktop programs
and prototypes.

The database is normally stored in a file on the computer."""
            ),

            (
                "INSERT",
                """The INSERT statement is used to add new records to a database.

Example:

INSERT INTO students
(name, age)
VALUES
('Shaheda', 18);

INSERT is a basic CRUD operation.

When using Python with SQLite, SQL statements can be executed through a
database cursor.

After inserting data, the transaction may need to be committed.

INSERT is commonly used in registration forms, student management systems and
other data-entry applications."""
            ),

            (
                "SELECT",
                """The SELECT statement is used to retrieve information from a
database.

Example:

SELECT * FROM students;

The * symbol means that all columns are requested.

Specific columns can also be selected.

Example:

SELECT name, age FROM students;

A WHERE clause can be used to filter records.

Example:

SELECT * FROM students WHERE age >= 18;

SELECT is one of the most frequently used SQL commands."""
            ),

            (
                "UPDATE",
                """The UPDATE statement modifies existing records.

Example:

UPDATE students
SET age = 19
WHERE name = 'Shaheda';

The WHERE condition is important because it identifies which records should be
changed.

Without an appropriate condition, multiple records may be modified.

UPDATE is commonly used when users edit their profile information or when
administrators correct stored data."""
            ),

            (
                "DELETE",
                """The DELETE statement removes records from a database.

Example:

DELETE FROM students
WHERE name = 'Shaheda';

The WHERE clause is important because it determines which records are removed.

Deleting data should be performed carefully because the removed information may
not be easily recoverable.

DELETE is used in applications when users or administrators need to remove
unwanted records."""
            ),

            (
                "REST API",
                """REST stands for Representational State Transfer.

A REST API allows different applications to communicate through HTTP.

Common HTTP methods include:

GET - retrieve data
POST - create data
PUT - update data
DELETE - remove data

For example, a mobile application may request student information from a
server using a REST API.

REST APIs are commonly used in web applications, mobile applications and
software systems that need communication between different services."""
            ),

            (
                "JSON",
                """JSON stands for JavaScript Object Notation.

JSON is a lightweight format used for storing and exchanging structured data.

Example:

{
    "name": "Shaheda",
    "age": 18,
    "course": "AI"
}

JSON data is easy for both humans and programs to read.

Python provides the json module for converting Python objects to JSON and
converting JSON back into Python objects.

JSON is commonly used when sending and receiving data through REST APIs."""
            )
        ]
    },

    # =====================================================
    # MODULE 7
    # =====================================================
    {
        "name": "Module 7 - Automation and Projects",
        "topics": [

            (
                "Automation",
                """Automation means using software to perform repetitive tasks
automatically.

Python is widely used for automation because it provides many libraries for
working with files, folders, websites and data.

Examples of automation include:
1. Renaming files.
2. Organizing folders.
3. Generating reports.
4. Processing spreadsheets.
5. Sending automated messages.
6. Performing repeated calculations.

Automation saves time and reduces repetitive manual work.

Before automating a task, the steps should be clearly understood and tested."""
            ),

            (
                "File Automation",
                """Python can automate many file-related tasks.

The os and pathlib modules can be used to work with files and folders.

Possible tasks include:
creating folders
renaming files
moving files
copying files
checking file extensions
organizing files by type

For example, a program can automatically move all PDF files into a PDF folder.

File automation is useful for managing large collections of documents and
reducing repetitive manual operations."""
            ),

            (
                "GUI Programming",
                """GUI stands for Graphical User Interface.

A GUI allows users to interact with a program through visual elements such as:

Buttons
Labels
Text boxes
Menus
Frames
Radio buttons
Check boxes

Python provides Tkinter for creating desktop GUI applications.

A GUI application normally responds to user actions instead of running only
from the command line.

Tkinter is useful for educational projects, calculators, management systems
and small desktop applications."""
            ),

            (
                "Event Handling",
                """Event handling means responding to actions performed by the
user.

Examples of events include:
button clicks
keyboard input
mouse movement
mouse clicks
window events

In Tkinter, a button can be connected to a function using the command option.

Example:

button = tk.Button(root, text="Click", command=my_function)

When the user clicks the button, my_function is executed.

Event handling makes GUI applications interactive."""
            ),

            (
                "Project Design",
                """Project design is the process of planning how an application
will work before writing the complete code.

A project design normally includes:
1. Problem definition.
2. Requirements.
3. User interface design.
4. Data design.
5. Program structure.
6. Technologies.
7. Testing strategy.

Good design makes development easier and reduces confusion.

A project should be divided into smaller components so that each part can be
developed and tested separately."""
            ),

            (
                "Planning",
                """Planning is an important stage of software development.

A project can be divided into tasks such as:
requirement collection
UI design
database design
coding
testing
debugging
documentation
presentation

A clear plan helps developers track progress.

Large projects should be divided into smaller milestones so that problems can
be identified early.

Planning also helps estimate the time and resources required for development."""
            ),

            (
                "Testing",
                """Testing is the process of checking whether a program works
correctly.

Testing should use different types of input, including valid and invalid data.

Examples of testing:
1. Normal input.
2. Boundary values.
3. Empty input.
4. Incorrect input.
5. Large values.
6. Repeated operations.

Testing helps identify errors before the software is delivered to users.

A good testing process improves reliability and user experience."""
            ),

            (
                "Debugging",
                """Debugging is the process of finding and fixing errors in a
program.

Common types of programming errors include:
Syntax errors
Runtime errors
Logical errors

Syntax errors occur when code violates language rules.

Runtime errors occur while the program is running.

Logical errors occur when the program runs but produces an incorrect result.

Debugging can involve reading error messages, checking variables, testing
individual functions and using debugging tools."""
            ),

            (
                "Mini Project",
                """A mini project combines multiple programming concepts into a
working application.

Example mini projects include:
Student Management System
Calculator
To-Do List
Library Management System
Quiz Application
Expense Tracker
Contact Manager

A good mini project should have a clear purpose and should solve a small
real-world problem.

The project should include a user interface, proper logic and testing."""
            ),

            (
                "Final Project Preparation",
                """Final project preparation includes all activities required to
complete and present a project.

Important steps include:

1. Define the problem.
2. Identify users and requirements.
3. Design the application.
4. Implement the features.
5. Test the application.
6. Fix errors.
7. Prepare documentation.
8. Prepare screenshots or demonstrations.
9. Prepare the presentation.
10. Practice explaining the project.

A final project should clearly demonstrate what problem it solves, how it was
developed and what technologies were used.

Good preparation makes the final demonstration more organized and effective."""
            )
        ]
    }
]

# =========================================================
# QUIZZES - 5 QUESTIONS EACH
# =========================================================
MODULE_QUIZZES = [

    [
        ("Which language is this platform teaching?",
         ["Java", "Python", "C++", "HTML"], 1),
        ("Which function displays output?",
         ["input()", "show()", "print()", "display()"], 2),
        ("Which symbol is used for a comment?",
         ["//", "#", "/*", "--"], 1),
        ("Which data type stores True or False?",
         ["int", "float", "bool", "str"], 2),
        ("Which function accepts user input?",
         ["input()", "get()", "scan()", "read()"], 0)
    ],

    [
        ("Which statement is used for decision making?",
         ["if", "loop", "def", "print"], 0),
        ("Which keyword stops a loop?",
         ["stop", "break", "exitloop", "end"], 1),
        ("Which keyword defines a function?",
         ["function", "fun", "def", "define"], 2),
        ("Which loop works with range()?",
         ["for", "if", "try", "class"], 0),
        ("Which keyword returns a value?",
         ["send", "return", "value", "back"], 1)
    ],

    [
        ("Which collection is ordered and changeable?",
         ["List", "Tuple", "Set", "None"], 0),
        ("Which collection stores unique values?",
         ["List", "Set", "String", "Tuple"], 1),
        ("Which structure uses key-value pairs?",
         ["List", "Tuple", "Dictionary", "Set"], 2),
        ("Python indexing normally starts from?",
         ["1", "0", "-1", "2"], 1),
        ("Which symbol is used for slicing?",
         [";", ":", "#", "@"], 1)
    ],

    [
        ("Which mode opens a file for reading?",
         ["w", "a", "r", "x"], 2),
        ("Which block handles exceptions?",
         ["try-except", "if-else", "for", "class"], 0),
        ("Which block always executes?",
         ["try", "except", "finally", "raise"], 2),
        ("CSV stands for?",
         ["Common System Values",
          "Comma-Separated Values",
          "Computer Saved Values",
          "Code Storage Variable"], 1),
        ("Which keyword raises an exception?",
         ["throw", "raise", "error", "exception"], 1)
    ],

    [
        ("A class is a?",
         ["Variable", "Blueprint", "Loop", "File"], 1),
        ("An object is an instance of?",
         ["Function", "Class", "Loop", "Module"], 1),
        ("Which is commonly a constructor?",
         ["start()", "main()", "__init__()", "create()"], 2),
        ("Which concept supports parent-child classes?",
         ["Inheritance", "Looping", "Input", "Logging"], 0),
        ("Which concept hides implementation details?",
         ["Abstraction", "Iteration", "Input", "Compilation"], 0)
    ],

    [
        ("What does SQL stand for?",
         ["Simple Query Language",
          "Structured Query Language",
          "System Query List",
          "Structured Question Language"], 1),
        ("Which command retrieves data?",
         ["INSERT", "SELECT", "UPDATE", "DELETE"], 1),
        ("Which command adds records?",
         ["INSERT", "SELECT", "DELETE", "READ"], 0),
        ("Which command modifies records?",
         ["CHANGE", "MODIFY", "UPDATE", "EDIT"], 2),
        ("Which format is common for data exchange?",
         ["JSON", "TXT", "EXE", "BAT"], 0)
    ],

    [
        ("What does automation mean?",
         ["Manual work", "Automatic task execution",
          "Deleting data", "Creating hardware"], 1),
        ("Which library is used for Python GUI?",
         ["tkinter", "numpy", "random", "math"], 0),
        ("What is debugging?",
         ["Writing comments", "Finding and fixing errors",
          "Creating folders", "Installing Python"], 1),
        ("What is testing used for?",
         ["Checking application behavior", "Deleting code",
          "Changing passwords", "Creating databases"], 0),
        ("What should a final project include?",
         ["Only code", "Only theory",
          "Implementation and testing", "Only screenshots"], 2)
    ]
]

# =========================================================
# FINAL QUIZ
# =========================================================
FINAL_QUIZ = [
    ("Which keyword defines a Python function?",
     ["def", "fun", "function", "define"], 0),

    ("Which structure stores key-value pairs?",
     ["List", "Tuple", "Dictionary", "Set"], 2),

    ("Which block handles exceptions?",
     ["try-except", "for", "class", "if"], 0),

    ("Which OOP concept supports parent-child classes?",
     ["Inheritance", "Slicing", "Iteration", "Input"], 0),

    ("Which SQL command retrieves data?",
     ["INSERT", "UPDATE", "SELECT", "DELETE"], 2)
]

# =========================================================
# FINAL ASSESSMENT
# =========================================================
ASSESSMENT = [
    ("Which function displays output?",
     ["print()", "input()", "scan()", "show()"], 0),

    ("Which collection contains unique elements?",
     ["List", "Set", "String", "Dictionary"], 1),

    ("Which keyword creates a class?",
     ["class", "object", "def", "new"], 0),

    ("Which SQL command removes records?",
     ["DELETE", "SELECT", "INSERT", "UPDATE"], 0),

    ("Which process finds and fixes errors?",
     ["Testing", "Debugging", "Planning", "Design"], 1)
]


# =========================================================
# MAIN APPLICATION
# =========================================================
class LearningPlatform:

    def __init__(self, root):

        self.root = root
        self.root.title("Python Learning Platform")

        # FULL SCREEN / MAXIMIZED
        self.root.state("zoomed")
        self.root.configure(bg=BG)
        self.root.resizable(True, True)

        # VARIABLES
        self.current_module = 0
        self.current_topic = 0

        self.quiz_index = 0
        self.quiz_score = 0
        self.quiz_questions = []

        self.module_scores = [0] * 7
        self.final_quiz_score = 0
        self.assessment_score = 0

        self.content_frame = None

        self.show_login()

    # =====================================================
    # CLEAR
    # =====================================================
    def clear(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    # =====================================================
    # LOGIN
    # =====================================================
    def show_login(self):

        self.clear()

        main = tk.Frame(
            self.root,
            bg=BG
        )

        main.pack(
            fill="both",
            expand=True
        )

        card = tk.Frame(
            main,
            bg=CARD,
            width=500,
            height=580
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text="PYTHON LEARNING",
            font=("Segoe UI", 30, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(pady=(60, 5))

        tk.Label(
            card,
            text="PLATFORM",
            font=("Segoe UI", 17, "bold"),
            bg=CARD,
            fg=LIGHT_BLUE
        ).pack()

        tk.Label(
            card,
            text="Login to continue",
            font=("Segoe UI", 12),
            bg=CARD,
            fg=GRAY
        ).pack(pady=(10, 35))

        tk.Label(
            card,
            text="Username",
            font=("Segoe UI", 11, "bold"),
            bg=CARD,
            fg=TEXT
        ).pack(anchor="w", padx=60)

        self.username_entry = tk.Entry(
            card,
            font=("Segoe UI", 12),
            bg=WHITE,
            fg="black",
            relief="flat"
        )

        self.username_entry.pack(
            fill="x",
            padx=60,
            pady=(5, 20),
            ipady=9
        )

        tk.Label(
            card,
            text="Password",
            font=("Segoe UI", 11, "bold"),
            bg=CARD,
            fg=TEXT
        ).pack(anchor="w", padx=60)

        self.password_entry = tk.Entry(
            card,
            font=("Segoe UI", 12),
            bg=WHITE,
            fg="black",
            show="*",
            relief="flat"
        )

        self.password_entry.pack(
            fill="x",
            padx=60,
            pady=(5, 25),
            ipady=9
        )

        tk.Button(
            card,
            text="LOGIN",
            font=("Segoe UI", 12, "bold"),
            bg=BLUE,
            fg=WHITE,
            activebackground=LIGHT_BLUE,
            relief="flat",
            cursor="hand2",
            command=self.login
        ).pack(
            fill="x",
            padx=60,
            ipady=11
        )

        tk.Label(
            card,
            text="Forgot Password?",
            font=("Segoe UI", 10, "underline"),
            bg=CARD,
            fg=LIGHT_BLUE
        ).pack(pady=18)

        self.root.bind(
            "<Return>",
            lambda event: self.login()
        )

    # =====================================================
    # LOGIN CHECK
    # =====================================================
    def login(self):

        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username == USERNAME and password == PASSWORD:

            self.root.unbind("<Return>")
            self.show_get_started()

        else:

            messagebox.showerror(
                "Login Failed",
                "Incorrect username or password.\n\n"
                "Username: shannu\n"
                "Password: 123456"
            )

    # =====================================================
    # GET STARTED
    # =====================================================
    def show_get_started(self):

        self.clear()

        main = tk.Frame(
            self.root,
            bg=BG
        )

        main.pack(
            fill="both",
            expand=True
        )

        card = tk.Frame(
            main,
            bg=CARD,
            width=850,
            height=560
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text="WELCOME TO",
            font=("Segoe UI", 22, "bold"),
            bg=CARD,
            fg=LIGHT_BLUE
        ).pack(pady=(90, 5))

        tk.Label(
            card,
            text="PYTHON LEARNING PLATFORM",
            font=("Segoe UI", 32, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack()

        tk.Label(
            card,
            text="Learn Python step-by-step",
            font=("Segoe UI", 16),
            bg=CARD,
            fg=TEXT
        ).pack(pady=20)

        tk.Label(
            card,
            text="Detailed Theory  |  7 Modules  |  Module Quizzes  |  Final Assessment",
            font=("Segoe UI", 12),
            bg=CARD,
            fg=GRAY
        ).pack()

        tk.Button(
            card,
            text="GET STARTED",
            font=("Segoe UI", 15, "bold"),
            bg=GREEN,
            fg=WHITE,
            activebackground="#259B6D",
            relief="flat",
            cursor="hand2",
            command=self.show_dashboard
        ).pack(
            pady=45,
            ipadx=40,
            ipady=13
        )

    # =====================================================
    # DASHBOARD
    # =====================================================
    def show_dashboard(self):

        self.clear()

        header = tk.Frame(
            self.root,
            bg=BG,
            height=75
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="PYTHON LEARNING PLATFORM",
            font=("Segoe UI", 23, "bold"),
            bg=BG,
            fg=WHITE
        ).pack(
            side="left",
            padx=30,
            pady=18
        )

        tk.Button(
            header,
            text="LOGOUT",
            font=("Segoe UI", 10, "bold"),
            bg=RED,
            fg=WHITE,
            relief="flat",
            cursor="hand2",
            command=self.show_login
        ).pack(
            side="right",
            padx=30,
            pady=20
        )

        body = tk.Frame(
            self.root,
            bg=BG
        )

        body.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        # LEFT MODULE PANEL
        left = tk.Frame(
            body,
            bg=CARD,
            width=310
        )

        left.pack(
            side="left",
            fill="y",
            padx=(0, 15)
        )

        left.pack_propagate(False)

        tk.Label(
            left,
            text="MODULES",
            font=("Segoe UI", 16, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(pady=18)

        for i, module in enumerate(MODULES):

            if i == self.current_module:
                color = LIGHT_BLUE

            elif i < self.current_module:
                color = "#236B54"

            else:
                color = "#173654"

            text = module["name"]

            if i < self.current_module:
                text = "[OK] " + text

            tk.Button(
                left,
                text=text,
                font=("Segoe UI", 9, "bold"),
                bg=color,
                fg=WHITE,
                relief="flat",
                anchor="w",
                cursor="hand2",
                command=lambda index=i: self.open_module(index)
            ).pack(
                fill="x",
                padx=12,
                pady=4,
                ipady=7
            )

        # PROGRESS
        progress = tk.Frame(
            left,
            bg=CARD
        )

        progress.pack(
            fill="x",
            padx=18,
            pady=20
        )

        completed = self.current_module

        tk.Label(
            progress,
            text=f"Progress: {completed}/7 Modules",
            font=("Segoe UI", 10, "bold"),
            bg=CARD,
            fg=TEXT
        ).pack(anchor="w")

        bar = tk.Frame(
            progress,
            bg="#173654",
            height=14
        )

        bar.pack(
            fill="x",
            pady=8
        )

        width = int((completed / 7) * 270)

        if width > 0:

            tk.Frame(
                bar,
                bg=GREEN,
                height=14,
                width=width
            ).place(x=0, y=0)

        tk.Button(
            left,
            text="VIEW CERTIFICATE",
            font=("Segoe UI", 9, "bold"),
            bg=GOLD,
            fg="#111111",
            relief="flat",
            cursor="hand2",
            command=self.show_certificate
        ).pack(
            side="bottom",
            fill="x",
            padx=15,
            pady=20
        )

        # RIGHT CONTENT
        right = tk.Frame(
            body,
            bg=BG
        )

        right.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.content_frame = right

        self.show_module_content()

    # =====================================================
    # OPEN MODULE
    # =====================================================
    def open_module(self, index):

        if index > self.current_module:

            messagebox.showinfo(
                "Module Locked",
                "Complete the previous module and quiz first."
            )

            return

        self.current_module = index
        self.current_topic = 0

        self.show_dashboard()

    # =====================================================
    # MODULE CONTENT
    # =====================================================
    def show_module_content(self):

        for widget in self.content_frame.winfo_children():
            widget.destroy()

        module = MODULES[self.current_module]

        top = tk.Frame(
            self.content_frame,
            bg=BG
        )

        top.pack(fill="x")

        tk.Label(
            top,
            text=module["name"],
            font=("Segoe UI", 22, "bold"),
            bg=BG,
            fg=WHITE
        ).pack(side="left")

        tk.Label(
            top,
            text=f"Topic {self.current_topic + 1}/{len(module['topics'])}",
            font=("Segoe UI", 11, "bold"),
            bg=BG,
            fg=GRAY
        ).pack(side="right")

        columns = tk.Frame(
            self.content_frame,
            bg=BG
        )

        columns.pack(
            fill="both",
            expand=True,
            pady=15
        )

        # TOPIC LIST
        topics_card = tk.Frame(
            columns,
            bg=CARD,
            width=250
        )

        topics_card.pack(
            side="left",
            fill="y",
            padx=(0, 12)
        )

        topics_card.pack_propagate(False)

        tk.Label(
            topics_card,
            text="TOPICS",
            font=("Segoe UI", 14, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(pady=12)

        for i, (topic_name, theory) in enumerate(module["topics"]):

            if i == self.current_topic:
                color = LIGHT_BLUE
            elif i < self.current_topic:
                color = "#236B54"
            else:
                color = "#173654"

            text = topic_name

            if i < self.current_topic:
                text = "[OK] " + text

            tk.Button(
                topics_card,
                text=text,
                font=("Segoe UI", 8, "bold"),
                bg=color,
                fg=WHITE,
                relief="flat",
                anchor="w",
                cursor="hand2",
                command=lambda index=i: self.select_topic(index)
            ).pack(
                fill="x",
                padx=8,
                pady=2,
                ipady=5
            )

        # THEORY
        theory_card = tk.Frame(
            columns,
            bg=CARD
        )

        theory_card.pack(
            side="left",
            fill="both",
            expand=True
        )

        topic_name, theory = module["topics"][self.current_topic]

        tk.Label(
            theory_card,
            text=topic_name,
            font=("Segoe UI", 21, "bold"),
            bg=CARD,
            fg=LIGHT_BLUE
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        text_box = scrolledtext.ScrolledText(
            theory_card,
            wrap="word",
            font=("Segoe UI", 12),
            bg="#0B203A",
            fg=TEXT,
            insertbackground=WHITE,
            relief="flat",
            padx=18,
            pady=18
        )

        text_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 15)
        )

        text_box.insert(
            "1.0",
            theory
        )

        text_box.config(
            state="disabled"
        )

        bottom = tk.Frame(
            self.content_frame,
            bg=BG
        )

        bottom.pack(
            fill="x"
        )

        tk.Button(
            bottom,
            text="NEXT STEP  ->",
            font=("Segoe UI", 12, "bold"),
            bg=GREEN,
            fg=WHITE,
            relief="flat",
            cursor="hand2",
            command=self.next_step
        ).pack(
            side="right",
            padx=5,
            pady=5,
            ipadx=25,
            ipady=9
        )

    # =====================================================
    # SELECT TOPIC
    # =====================================================
    def select_topic(self, index):

        self.current_topic = index

        self.show_module_content()

    # =====================================================
    # NEXT STEP
    # =====================================================
    def next_step(self):

        module = MODULES[self.current_module]

        if self.current_topic < len(module["topics"]) - 1:

            self.current_topic += 1

            self.show_module_content()

        else:

            self.start_module_quiz()

    # =====================================================
    # START MODULE QUIZ
    # =====================================================
    def start_module_quiz(self):

        self.quiz_questions = MODULE_QUIZZES[self.current_module]
        self.quiz_index = 0
        self.quiz_score = 0

        self.show_quiz(
            f"Module {self.current_module + 1} Quiz",
            "module"
        )

    # =====================================================
    # START FINAL QUIZ
    # =====================================================
    def start_final_quiz(self):

        self.quiz_questions = FINAL_QUIZ
        self.quiz_index = 0
        self.quiz_score = 0

        self.show_quiz(
            "Final Quiz",
            "final"
        )

    # =====================================================
    # START ASSESSMENT
    # =====================================================
    def start_assessment(self):

        self.quiz_questions = ASSESSMENT
        self.quiz_index = 0
        self.quiz_score = 0

        self.show_quiz(
            "Final Assessment",
            "assessment"
        )

    # =====================================================
    # QUIZ SCREEN
    # =====================================================
    def show_quiz(self, title, quiz_type):

        self.clear()

        main = tk.Frame(
            self.root,
            bg=BG
        )

        main.pack(
            fill="both",
            expand=True
        )

        card = tk.Frame(
            main,
            bg=CARD,
            width=900,
            height=650
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 27, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(pady=(40, 5))

        tk.Label(
            card,
            text=f"Question {self.quiz_index + 1} of {len(self.quiz_questions)}",
            font=("Segoe UI", 12, "bold"),
            bg=CARD,
            fg=GRAY
        ).pack(pady=(0, 30))

        question, options, correct = self.quiz_questions[self.quiz_index]

        tk.Label(
            card,
            text=question,
            font=("Segoe UI", 18, "bold"),
            bg=CARD,
            fg=TEXT,
            wraplength=750
        ).pack(pady=20)

        self.answer_var = tk.IntVar(value=-1)

        for i, option in enumerate(options):

            tk.Radiobutton(
                card,
                text=option,
                variable=self.answer_var,
                value=i,
                font=("Segoe UI", 13),
                bg=CARD,
                fg=WHITE,
                activebackground=CARD,
                activeforeground=WHITE,
                selectcolor=BLUE,
                anchor="w"
            ).pack(
                fill="x",
                padx=100,
                pady=7
            )

        button_text = "NEXT"

        if self.quiz_index == len(self.quiz_questions) - 1:
            button_text = "SUBMIT"

        tk.Button(
            card,
            text=button_text,
            font=("Segoe UI", 13, "bold"),
            bg=GREEN,
            fg=WHITE,
            relief="flat",
            cursor="hand2",
            command=lambda: self.finish_quiz(quiz_type)
        ).pack(
            pady=35,
            ipadx=35,
            ipady=10
        )

    # =====================================================
    # FINISH QUIZ
    # =====================================================
    def finish_quiz(self, quiz_type):

        selected = self.answer_var.get()

        if selected == -1:

            messagebox.showwarning(
                "Select Answer",
                "Please select an answer."
            )

            return

        correct_answer = self.quiz_questions[self.quiz_index][2]

        if selected == correct_answer:
            self.quiz_score += 1

        if self.quiz_index < len(self.quiz_questions) - 1:

            self.quiz_index += 1

            if quiz_type == "module":
                title = f"Module {self.current_module + 1} Quiz"
            elif quiz_type == "final":
                title = "Final Quiz"
            else:
                title = "Final Assessment"

            self.show_quiz(
                title,
                quiz_type
            )

        else:

            if quiz_type == "module":

                self.module_scores[self.current_module] = self.quiz_score
                self.show_module_result()

            elif quiz_type == "final":

                self.final_quiz_score = self.quiz_score
                self.show_final_quiz_result()

            else:

                self.assessment_score = self.quiz_score
                self.show_assessment_result()

    # =====================================================
    # MODULE RESULT
    # =====================================================
    def show_module_result(self):

        self.clear()

        percentage = self.quiz_score / 5 * 100

        card = tk.Frame(
            self.root,
            bg=CARD,
            width=650,
            height=470
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text="MODULE QUIZ COMPLETED",
            font=("Segoe UI", 26, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(pady=(55, 15))

        tk.Label(
            card,
            text=f"Score: {self.quiz_score}/5",
            font=("Segoe UI", 22, "bold"),
            bg=CARD,
            fg=GREEN
        ).pack(pady=10)

        tk.Label(
            card,
            text=f"Percentage: {percentage:.0f}%",
            font=("Segoe UI", 16),
            bg=CARD,
            fg=TEXT
        ).pack()

        if self.current_module < 6:
            text = "GO TO NEXT MODULE"
        else:
            text = "START FINAL QUIZ"

        tk.Button(
            card,
            text=text,
            font=("Segoe UI", 12, "bold"),
            bg=BLUE,
            fg=WHITE,
            relief="flat",
            cursor="hand2",
            command=self.after_module_quiz
        ).pack(
            pady=45,
            ipadx=30,
            ipady=11
        )

    # =====================================================
    # AFTER MODULE
    # =====================================================
    def after_module_quiz(self):

        if self.current_module < 6:

            self.current_module += 1
            self.current_topic = 0

            self.show_dashboard()

        else:

            self.start_final_quiz()

    # =====================================================
    # FINAL QUIZ RESULT
    # =====================================================
    def show_final_quiz_result(self):

        self.clear()

        percentage = self.final_quiz_score / 5 * 100

        card = tk.Frame(
            self.root,
            bg=CARD,
            width=650,
            height=470
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text="FINAL QUIZ COMPLETED",
            font=("Segoe UI", 26, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(pady=(55, 15))

        tk.Label(
            card,
            text=f"Score: {self.final_quiz_score}/5",
            font=("Segoe UI", 22, "bold"),
            bg=CARD,
            fg=GREEN
        ).pack(pady=10)

        tk.Label(
            card,
            text=f"Percentage: {percentage:.0f}%",
            font=("Segoe UI", 16),
            bg=CARD,
            fg=TEXT
        ).pack()

        tk.Button(
            card,
            text="START FINAL ASSESSMENT",
            font=("Segoe UI", 12, "bold"),
            bg=BLUE,
            fg=WHITE,
            relief="flat",
            cursor="hand2",
            command=self.start_assessment
        ).pack(
            pady=45,
            ipadx=30,
            ipady=11
        )

    # =====================================================
    # ASSESSMENT RESULT
    # =====================================================
    def show_assessment_result(self):

        self.clear()

        percentage = self.assessment_score / 5 * 100

        card = tk.Frame(
            self.root,
            bg=CARD,
            width=650,
            height=470
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text="FINAL ASSESSMENT COMPLETED",
            font=("Segoe UI", 24, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(pady=(55, 15))

        tk.Label(
            card,
            text=f"Score: {self.assessment_score}/5",
            font=("Segoe UI", 22, "bold"),
            bg=CARD,
            fg=GREEN
        ).pack(pady=10)

        tk.Label(
            card,
            text=f"Percentage: {percentage:.0f}%",
            font=("Segoe UI", 16),
            bg=CARD,
            fg=TEXT
        ).pack()

        tk.Button(
            card,
            text="GENERATE CERTIFICATE",
            font=("Segoe UI", 12, "bold"),
            bg=GOLD,
            fg="#111111",
            relief="flat",
            cursor="hand2",
            command=self.show_certificate
        ).pack(
            pady=45,
            ipadx=30,
            ipady=11
        )

    # =====================================================
    # CERTIFICATE
    # =====================================================
    def show_certificate(self):

        self.clear()

        outer = tk.Frame(
            self.root,
            bg=GOLD,
            width=1100,
            height=650
        )

        outer.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        outer.pack_propagate(False)

        inner = tk.Frame(
            outer,
            bg=WHITE,
            highlightbackground="#173654",
            highlightthickness=5
        )

        inner.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=12
        )

        tk.Label(
            inner,
            text="CERTIFICATE OF COMPLETION",
            font=("Segoe UI", 30, "bold"),
            bg=WHITE,
            fg="#102F55"
        ).pack(
            pady=(55, 20)
        )

        tk.Label(
            inner,
            text="This certificate is proudly presented to",
            font=("Segoe UI", 13),
            bg=WHITE,
            fg="#555555"
        ).pack()

        tk.Label(
            inner,
            text="SHAIK SHAHEDA",
            font=("Segoe UI", 34, "bold"),
            bg=WHITE,
            fg="#102F55"
        ).pack(pady=18)

        tk.Frame(
            inner,
            bg=GOLD,
            height=2,
            width=550
        ).pack()

        tk.Label(
            inner,
            text="for successfully completing the Python Learning Platform",
            font=("Segoe UI", 13),
            bg=WHITE,
            fg="#444444"
        ).pack(pady=(25, 8))

        total_score = (
            sum(self.module_scores)
            + self.final_quiz_score
            + self.assessment_score
        )

        total_marks = 45

        percentage = (
            total_score / total_marks
        ) * 100

        tk.Label(
            inner,
            text=f"Total Score: {total_score}/{total_marks}    |    "
                 f"Percentage: {percentage:.1f}%",
            font=("Segoe UI", 13, "bold"),
            bg=WHITE,
            fg="#102F55"
        ).pack(pady=8)

        tk.Label(
            inner,
            text=f"Date: {datetime.now().strftime('%d-%m-%Y')}",
            font=("Segoe UI", 11),
            bg=WHITE,
            fg="#777777"
        ).pack()

        # BOTTOM
        bottom = tk.Frame(
            inner,
            bg=WHITE
        )

        bottom.pack(
            side="bottom",
            fill="x",
            padx=55,
            pady=30
        )

        tk.Label(
            bottom,
            text="PYTHON LEARNING PLATFORM",
            font=("Segoe UI", 9, "bold"),
            bg=WHITE,
            fg="#777777"
        ).pack(
            side="left",
            pady=20
        )

        # SIGNATURE
        signature = tk.Frame(
            bottom,
            bg=WHITE
        )

        signature.pack(
            side="right",
            padx=25
        )

        tk.Label(
            signature,
            text="Nilesh Jadav",
            font=("Segoe Script", 19, "italic"),
            bg=WHITE,
            fg="#102F55"
        ).pack()

        tk.Frame(
            signature,
            bg="#555555",
            height=1,
            width=180
        ).pack()

        tk.Label(
            signature,
            text="AUTHORIZED SIGNATURE",
            font=("Segoe UI", 7, "bold"),
            bg=WHITE,
            fg="#777777"
        ).pack(pady=(3, 0))

        tk.Button(
            self.root,
            text="BACK TO DASHBOARD",
            font=("Segoe UI", 10, "bold"),
            bg=BLUE,
            fg=WHITE,
            relief="flat",
            cursor="hand2",
            command=self.show_dashboard
        ).place(
            relx=0.5,
            rely=0.97,
            anchor="center"
        )


# =========================================================
# RUN APPLICATION
# =========================================================
if __name__ == "__main__":

    root = tk.Tk()

    app = LearningPlatform(root)

    # MAXIMIZED WINDOW
    root.state("zoomed")

    root.mainloop()