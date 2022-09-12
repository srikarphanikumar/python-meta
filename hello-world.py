print('hello world');

name = 'John';

if (name == 'John'): 
    print('Name: ', name);

# Commenting options
# Basic function
def sayHello(): 
    print('Hello from sayHello Fn');

sayHello();

# Variables and how to use them
# Naming Variables: Camel case (myName), snake case (my_name)

x = 5;
print('x: ', x);

# Assigning same value to different variables
a = b = c = 10; 
print('a: ', a)
print('b: ', b)
print('c: ', c)

# Assigning different value to different variables
d,e,f = 1,2,3; 
print('d: ', d)
print('e: ', e)
print('f: ', f)


# Delete a variable
del a;
# print('A: ', a) # will throw an error since A is not defined