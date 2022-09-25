# Method to divide 2 numbers
def divideby(a,b):
    return a/b;

# Common Errors: 
# IndexError (while accessing list[6] when you have just 3 items)
# ZeroDivisionError
# FileNotFoundError

# Exception handling:

# ZeroDIvisionError
try:
    ans = divideby(40, 0);
except ZeroDivisionError:
    print('cant divide by zero bro!')
except Exception as e:
    print('Something went wrong', e);
    print('e.__class__: ', e.__class__)


# Index Error
list1 = [1,2,3,4];

try:
    item = list1[4];
    print(item);
except IndexError:
    print('Index Error bro');
except: 
    print('Some other error')

# File not found error:
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("Unable to locate file")  