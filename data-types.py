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