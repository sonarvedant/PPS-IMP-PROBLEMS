"""
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










"""