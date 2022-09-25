# 5 main types
# 
# 1) Numeric ( has 3 more: Integer, Float and Complex Numbers )
# 2) Sequence ( has 3 more: String, List and Tuples )
# 3) Dictionary (Stored in a key value object structure)
# 4) Boolean
# 5) Set

# Numeric
# Integer: Non fractional whole numbers
# Float: Fractional / Decimal numbers
# Complex: Real Numbers + Non real numbers (Eg: 10 + 10j);

# Sequence: 
# Strings: 
# Lists: 
# Tuples: Similar to lists / Ordered sequence of one or more types (Immutable)

# Set: Unordered list of data


a = 10.0;
print(type(a)); # Ans: float
b = 10;
print(type(b)); # Ans: int
c = 'srikar';
print(type(c)); # Ans: str
d = [1,2,3,4];
print(type(d)); # Ans: list

# ************************* STRINGS *************************
# Strings: characters enclosed in either single quotes or double quotes
# Strings are just a sequence of characters: Meaning they are an array. 
# Single Line Declarations
car = 'Lexus';

# Multi line Declarations: 
car_description = 'This Lexus RX 350 \
    is my car \
    which was bought in 2022';
print('Car Description: ', car_description)

# Reassigning values: 
name = 'Srikar';
print('Name before: ', name);
name = 'Phani Kumar';
print('Name after: ', name);

# Length: 
print('Length of name: ', len(name));

# Concatenation: 
print('Concatenation example: ', 'hello ' + 'there!');

# Accessing characters using 0-indexing: 
print('Element at 0th position in name is: ', name[0]);


# ******************** TYPE CASTING *******************
# Implicit: Python does that for you (Eg: 123.50 will be stored as float)
# Explicit: Use inbuilt functions such as int(), float(), str()

# int(): converts strings to numbers
print(int('55')); # Ans: 55
# float(): converts int numbers to float 
print(float(55)); # Ans: 55.0
# str(): converts numbers to strings
print(str(55)); # Ans: '55'

# ord(): returns int representing underlying unicode char
# hex(): int to hex
# oct(): int to octa and returns as string
# set(): 
# dict(): 
# list(): 


# ************************* INPUT() *************************
# Used to get user input

email = input('Please enter an email: ');
print('Email: ', email)

# PRINT FUNCTION CAN TAKE MULTIPLE ARGUMENTS TOO
# EG: print(obj1_name, obj2_name, sep=', ')
# sep() here is a seperator function which will seperate the object
# with ', '
print('Srikar', 'Phani Kumar', sep=', ');

num1 = input('Enter num1: ');
num2 = input('Ente num2: ');
print(num1, num2)