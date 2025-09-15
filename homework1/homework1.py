# File: homework1. py

# -- Variables and Data Types --

a = 10
print(a)
print(type(a)) 
# a is an interger

b = 1.5
print(b)
print(type(b)) 
# b is a float 

c = 3j
print(c)
print(type(c))
# c is complex  

d = "hello"
print(d)
print(type(d)) 
# d is a string 

e = [1, 2, 3]
print(e)
print(type(e)) 
# e is a list

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) 
# f is a dictionary

g = (1, 2)
print(g)
print(type(g)) 
# g is a tuple

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) 
# h is a list

i = True
print(i)
print(type(i)) 
# i is a boolean

j = None
print(j)
print(type(j)) 
# j is NoneType

k = [True, "blue", 12]
print(k)
print(type(k)) 
# k is a list

l = str(14)
print(l)
print(type(l)) 
# l is a string

m = 1e4
print(m)
print(type(m)) 
# m is a float

"""
1. I found 9 types of data
2. String, list, boolean, float, tuple, dictionary, complex, NoneType, integer 
3. (b and m), (l and d), (k, h, and e)
4. String - the function str () acted on the integer 14 and defined it as a string instead. 

"""

# ---Booleans ---

print(10 >9) 
# True, 10 is greater than 9

print(10 == 9)
# False, 10 does not equal 9 

print(10 <= 9)
# False, 10 is not less than or equal to 9

print(bool("abc"))
#True, strings are interpreted as true

print(bool(["apple", "cherry", "banana"]))
# True, lists are interpreted as true

print(bool(True))
# True

print(bool(False))
# False

print(bool(0))
# False, zero is interpreted to be false

print(bool(""))
# False, empty quotes are interpreted to be false

print(bool(" "))
# True, quotes containging a character are considered true

print(bool(()))
#False, empty brackets are considered to be false

print(bool([]))
#False, empty brackets are considered to be false

print(bool({}))
#False, empty brackets are considered to be false

print(bool(True and False))
# False, something cannot be true and false

print(bool(True and True ))
# True, if something is true it is true

print(bool(False and False))
# False, something cannot be false twice according to the computer's logic

print(bool(True or False))
# True, something is either true or true

print(bool(True or True))
# True, if something is true it is true

print(bool(False or False))
# False, something cannot be only false according to the computer's logic

print(not(False))
# True, the base assumption must be that something is true

print(not(True))
# False, the base assumption must be that something is true
 

"""
 1. Empty brackets or quotes are interpreted to be false, while any string inside these operators are interpreted to be true
 2. The difference in the way the computer treats True and True/True or True and False and False/False or False
 3. print(1 + 1 = 2) 1 + 1 is equal to 2
 4. print(1 + 1 = 3) 1 + 1 is not equal to 3
 """


# ---Operators ---

print(10 + 5)
# 15, + performs addition

print(10 - 5)
# 5, - performs subtraction

print(2 * 4)
# 8, * performs multiplication 

print(6/3)
# 2, / performs division

print(5 % 2)
# 1, % returns the remainder of division

print(3 ** 2)
# 9, ** raises the first number to the power of the second

print(15 // 2)
# 7, // divides and then rounds the result dowm

print(5 == 2)
# False, == checks equivalence 

print(10 != 10)
# False, != checks inequivalence 

print(2 < 5)
# True, < checks if the first number is smaller than the second

print(12 > 5)
# True, > checks if the first number is larger than the second

print(5 <= 6)
# True, <= checks if the first number is less than or equal to the second

print(1 >= 10)
# False, >= checks if the first number is greater than or equal to the second

x = 5

x += 5
# 10, += adds the number after the operator to the variable 

x -= 4
# 6, -= subtracts the number after the operator from the variable

x *= 3
# 18, *= multiplies the number after the operator by the variable 

"""
1. And returns true if both sides of the statement are true 
(1+1 = 2 and 3+3 = 6): True
(1+1 = 2 and 3+3 = 7): False
2. Or returns true if one side of the statement is true 
(1+1 = 2 or 3+2 = 6): True
(1+3 = 2 or 3+2 = 7): False
3. Not returns true if the statement after is not true
(1 not 6): True
(1 not 1): False

1. / divides the two numbers normally and returns a float, // divides and then rounds down to the nearest whole number
2. % Returns the whole number remainder of division, // returns the whole number quotient of division
3. % - (13 % 5 = 3)
4. Assignment operators correlate a value with a variable 
"""

# ---Strings ---

my_string = "hello"

print(my_string)
print(my_string[0])
print(my_string[1])
print(my_string[2])
print(my_string[3])
print(my_string[4])
print(my_string[-1])
print(my_string[1:3])
print(my_string[0:5:2])
print(len(my_string))
print(my_string + "goodbye")
print(my_string * 7)

name = "Oski"
print("Hello, my name is", name)

name = "Oski"
print(f"Hello, my name is {name}")

"""
1. Prints only a specific range of characters in a string. 1:3 sliced the string
2. The code printed the listed string and the defined variable directly after 
3. The code printed the listed string and the defined variable directly after 
4. In the second expression, you don't need to end the string to put in the variable - you can include variables in strings by using {}, which are called f-strings
"""


# ---Terminal Commands ---

"""
cd
Changes Directory - use to move from one directory to another
cd python_decal_fall25

ls
Lists - lists all files and folders within the current directory
ls

ls -a
List all - lists all files and folders within the current directory, including hidden files
ls -a


mkdir
Make directory - creates a directory 
mkdir Bananas

cat
Concanate - runs and prints files
cat Bananas

pwd
Print working directory - Prints the path of the directory you are currently in 


cd ..
Change directory parent - Brings you to the parent directory of the file you are in 
cd ..


cd .
Change directory none - Changes to the current directory - does not change anything 
cd . 


cd ∼
Change directory home - brings you to your home directory
cd ~


cp
Copy - Copies the file
cp ~/Bananas/


mv
Move - moves files from one directory to another
mv ~/Bananas/ ~/Oranges?


rm (be careful with this one)
remove - Removes information from a file or folder or directory
rm Bananas


clear
Clear - clears terminal
clear 


grep
Search - looks for matching info within a file
grep "Bananas" file.py

"""

"""
1. 
touch 
Creates a new file
touch Bananas

find
finds the location of a given file
find 

less
shows contents of a file
less Bananas

2. ls lists all visible files and folders while ls -a lists all visible and hidden files and folders
3. A file that performs a function on your computer but is not visible
4. 
-m 
Message: correlates text with a commmand 

-p
Creates nested directories if they do not exist already

-l
Long listing: lists more info when the ls commmand is used
"""

