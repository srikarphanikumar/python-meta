# 2 main functions in handling files
# 1) Open - Used for reading, writing and creating a file 
#       Default mode is 'r'
# 2) Close

########################### Open ##########################
# accepts 2 arguments: file_name/file_path, mode
# mode can be read write or create
# open(file_name_or_path, mode)
# you can also mention output format of the file : text / binary

# mode: 
# r: open / read a text file
# rb: open / read a binary file
# r+ : reading and writing
# w: writing -- note that it will overwrite the existing file. 
    # wb: write a binary file
# a: opens a file to edit or append data

# with open('sample.txt', r); ==> better way to use because it automatically 
# closes the file


########################### Close ##########################
# close(): does not take any arguments. Used to close a file. 


# File handling: 
file = open('test.txt', mode='r');
print('File data: ', file)

# print('First line of the file: ', file.read());
print('All lines of the file: ', file.readlines())

# file.read() : read first line
# file.readlines(): returns an array of files

with open('test.txt', mode='r') as fileName:
    data = fileName.readline();
    print('Data variable: ', data)

with open('sample.txt', 'w') as newFile:
    # add a single line
    # \n: new line escape character. 
    newFile.write('Writing new content into new file. \n')

    # add multiple lines
    newFile.writelines(['Adding second line \n', 'Adding third line']);

# if you want to append data to the new file now. 
try: 
    with open('sample/sample2.txt', 'w') as newFile: 
        newFile.write('\nAdding last line to the file using append')
except FileNotFoundError as e:
    print('File not found error: ', e)

# read(): whole content of file
# readline(): first line of the file
# readline(integer): integer passing will read integer number of characters
# readlines(): returns an ordered listof all lines as an array;