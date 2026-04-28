'''
FUNCTIONS AND STRINGS

FUNCTIONS:- function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function.
A function can return data as a result.
Need - 1] all logically related code is grouped together in a function. 
       2] code reusability.
       3] it makes the code more readable and easier to maintain, easy to debug.
       4] repetation is avoided.
syntax - def var(parameters):
            body
first line of the function is called function header and rest of the lines are called function body.
function can be called by using the function name followed by parentheses.


Variable Scope:- the region of the program where a variable is defined and can be accessed is called variable scope.
1] local variable - a variable that is defined inside a function and can only be accessed within that function.
2] global variable - a variable that is defined outside a function and can be accessed from anywhere in the program.

return statement - a return statement is used to exit a function and return a value to the caller.

Additional features 
1] Required arguments - arguments that are required to be passed to a function.
       eg. def add(a, b):
        return a + b
2] Default arguments - arguments that have a default value and are optional to be passed to a function.
       eg. def greet(name="Guest"):
        print("Hello", name)
3] Keyword arguments - arguments that are passed to a function by specifying the parameter name.
       eg. def greet(name, age):
        print("Hello", name, "you are", age, "years old")
        greet(age=25, name="Alice")
4] Variable-length arguments - arguments that can take a variable number of values.
       eg. def sum(*args):
        total = 0
        for n in args:
            total += n
        return total
(similaar to rest parrameter in js)

Lambda or anonymous function - a small, unnamed function that can be defined in a single line of code.
syntax - lambda arguments: expression
eg. add = lambda a, b: a + b
    print(add(5, 3))
    instead of doing 
    eg. def add(a, b):
              return a + b

Documentation string(docstring)
is similar to comments but for functions. 
they arre multiline stringsused to explain function
syntax - def function_name(parameters):
               """docstring"""
            body
we can access docstring using __doc__ attribute of the function.
it should start with a capital letter and end with a period.



Good programming practices for functions:
1] Use meaningful names for functions and parameters.                      
2] instead of using 8 spaces for indentation, use 4 spaces.
3] make use of proper comments 
4] use od documentation strings
5] use spaces around operators 
6] function should be in lowercase and words should be separated by underscores.

--------------------------------------------------------------------------------------------
Introduction to Modules
A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py added.
Modules are used to organize code into manageable sections and to promote code reusability.
from ... import ... - used to import specific functions or variables from a module.
import ... - used to import the entire module.
eg. from math import math

creating a module 
1] create a file with .py extension and write the code in it.
2] save the file with a name that is a valid Python identifier.
3] import the module in another Python file using the import statement.
eg.
# my_module.py
def greet(name):
    print("Hello", name)

# main.py
from my_module import greet
    greet("Alice")

The dir() function




'''




