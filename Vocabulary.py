"""     OOP - OBJECT ORIENTED PROGRAMMING

APIE - 4 pillars of OOP: abstraction, polymorphism, inheritance, encapsulation
Abstraction - dealing with things at our level, not sweating always how it works underneath. stay at the highest level, solve the problem, move on. be lazy. hiding lower level operations for user friendliness. dealing with the idea rather than the process.
Polymorphism - functions that operate differently depending on the data given
Inheritance - bringing data and functionality in from a parent class/object
            - To go up the chain, in our example...
              Object
              Person
              Student
Encapsulation - bundling together of data and functions which manipulate that data. e.g. a function needs data? pull that in with params/args, and return what the output should be. i.e. if we want to make any changes to a class, those methods should all be encapsulated within the class itself.

attribute - data within a class

heirarchial inheritance - when a class is inherited by multiple classes

method - a function inside of a Class

multi level inheritance - class inherits what its parent has inherited from its own parent. chaining inheritance. layered inheritance. e.g. Grandparents to grandkid.

multiple inheritance - class inherits from multiple other classes

single inheritance - class inherits from a single other class
"""
#############
#############
"""     PYTHON FUNDAMENTALS

API - 

argument - what you pass into a function, per its definition [line]
            def myfunc(param1, param2, param3):
                pass

            myfunc(pos_arg1, pos_arg2, pos_arg3)

keyword argument - example below... 'year=' etc
            mini_me = Human("Carson", 2, datetime(year=2019, month=6, day=27))

arithmetic operator - perform mathematical computations on data ( + - * / // %)

assignment operator - perform mathematical operations and reassign the result to the variable

boolean - data type, true or false

branching - (if, then, else) allows for distinct outcomes based upon true/false evaluations

callback - a function that calls on another function within its parameters

closure - (see callback)

code block - region of code that is indented. note: non-indented code is NOT a code block. per Adam. (\t)

code injection - (bad) e.g. SQL injection, when someone maliciously puts code into an input knowing that your program will actually run it as code.

concatenation - appends multiple strings together with a + operator

conditional - statement that resolves to TRUE or FALSE

custom data type - can be constructed using classes

dictionary - mutable, unordered set of key/value pairs denoted by {( : ), ( : )}

drop through - when multiple if statements are ordered incorrectly, causing multiple outputs to fire. E.g. When checking for ages <18, 18 < 21, and 21+.

elif - if all preceding if/elif conditions resolve to FALSE, and this elif resolves to TRUE, execute

else - if all preceding if/elif conditions resolve to FALSE, these default conditions are executed

float - data type, rational number positive or negative, can contain decimals

for loop - block of code that is executed over the number of items specified in a sequence

function - a named, reusable block of code that can (1) take in information, and (2) return information. a playbook.
         - the only case where an internal variable does not have scope to the rest of the program. if/for/while do give scope to vars.
         - correctly said, "That if statement did in fact give scope to the rest of the program."

if - when a condition is met, execute the following code

integer - data type, whole number positive or negative

interpreter - python's way of executing python code

.json - javascript object notation, aka looks just like a python dictionary

linked list - 

list - mutable and ordered data type denoted by []

list comprehension - #HW define

modular programming - e.g. data v repo v UI. antonym: spaghetti coding. insulating chunks of code so that one change in a program doesn't break everything else going on.

modulus - arithmetic operator, returns remainder of a division problem

mutable/immutable - able to be changed

name mangling - 

node - the items inside of a linked list

ordered sequence - includes string, list, tuple. excludes set (which is unordered)

parameters - what a function asks for as input, in the definition [line]

PII - personally identifiable information. keep this data out of the hands of those who don't need it.

procedure - sequential steps you take while performing actions. functions allow for procedure reusability.

proxy/ing - #hw

refactoring - 

repository pattern (middleware / middleman) - separation of concern. in our class example: data v repo v UI

reserved word - a word that has special meaning in python and cannot be used to name a variable

return - what is passed back from a function. if no other return specified, defaults to 'NONE'

sanitize - ensuring that outside data is vetted by the program to prevent malicious activity

scope - the idea that a child block of text contains local information, and can access information from its parent. However, the parent cannot access information from this child. (Bad practice.)

set - mutable and unordered data type {}

silently - does not throw an error, if one might exist

slicing - 

string - data type denoted by ' or "

string templating - e.g. f-string, plugging valud python code directly into a string

TDD - test driven development, programming toward an already written test to stay on track. write the test file before the procedure/actual file.

terminal flag - appending a '-r' (replace with any letter) after a terminal command
              - Example: py -m venv my_super_cool_env
              - (py = python) (-m is mod) (venv = virt env) (name the venv as our_name)

tuple - immutable and ordered data type denoted by () and a ,    (a more perforant type)

unpacking - can be done on a tuple. declare multiple vars in 1 line.
            name, age = "Drew", 31     this technically creates a tuple

variable - a name that stores and refers to some data

VEnv - virtual environment. purpose is for sharing a project, and easily including any dependencies that go along with the project.

while loop - block of code that is repeated while a condition is met

"""
#               COLLECTIONS
#                      Indexed
# Type       Mutable   Ordered     Denotation
# ------------------------------------------------------------------------------
# List       Yes       Yes         [,]              .append  .pop  .insert
# Set        Yes       N (unique)  {,}              .add     .pop  .update
# Tuple      N         Yes         (,)
# Dictionary Yes       N (unique)  { KEY : VALUE }   dict["key"] = value  .pop  .update  .get
#                                                   .update can take 2 dictionaries into 1 new dict
#
# Advantage of a tuple over a list, you can unpack a tuple
# In python, any data type can go inside any collection type
"""
Keyboard finger map
LP  LR  LM  LI      RI      RM  RR  RP
1   2   3   45      67      8   9   0-=     []
!   @   #   $%      ^&      *(  )   _+      {}

"""
#                   LOOPS
# ------------------------------------------
# For loop - Operates for the length of the iterable given to it
# While loop - 
# 
# Variables used within the loop ARE available outside of the loop
"""
        SCOPE
Location        Share scope?
-----------------------------
If              Yes
For loop        Yes
While loop      Yes
Function        N
(to be continued...)

"""

if True:
    myvar = "i'm here"

print(myvar)