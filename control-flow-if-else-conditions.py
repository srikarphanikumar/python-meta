# # Control Flow: control the flow of the operations in the code
# # Tell what to execute first and what next

# # Conditional (if, else, elif)
# bill_total = 24;
# discount1 = 10;
# discount2 = 20;

# if bill_total > 200:
#     print('Bill greater than 100!');
#     bill_total = bill_total - (discount1 * 2);
# elif bill_total > 100 and bill_total < 200: 
#     print('Bill total greater than 100 and less than 200');
# else: 
#     print('Bill Less than 100');

# print('Total Bill: ', str(bill_total));

# # Match-case statement : Similar to switch 
# httpStatus = 500;

# match httpStatus:
#     case 200 | 201: 
#         print('case 200');
#     case 202 | 301:
#         print('case 202 or 301');
#     case 400 | 403: 
#         print('case 400 server error');
#     case _: 
#         print('similar to default case in switch');

# # Loops (for, while)
# str = 'looping';

# for char in str:
#     print('Char: ', char);

# favorites = ['Cake 1', 'Cake 2', 'Cake 3'];

# for dessert in favorites:
#     print('Each Dessert: ', dessert);

# for i in range(10): 
#     print('I: ', i);

# for index, item in enumerate(favorites):
#     print('Index: ', index);
#     print('Item: ', item);
# #Starter Code

# favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

# for dessert in favorites:
#     if dessert == 'Churros':
#         pass #used to ignore the if-condition
#     print('Other desserts I like are', dessert) 


# # while

# counter = 0;
# while counter < len(favorites):
#     print('Favorite item number: ', favorites[counter]);
#     counter += 1;

# # Nested loops: 

# list1 = [1,2,3,4,5,6,7,8,9];
# list2 = [1,2,3,4,5,6,7,8,9];

# for item1 in list1: 
#     print(item1);
#     for item2 in list2: 
#         print(item2);

import time;

start_time = time.time();

for i in range(10):
    for j in range(10):
        print(0, end = ' ');
    print();

print(round((time.time() - start_time), 2))