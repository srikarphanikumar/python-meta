
################################## Lists: Array ##############################

from textwrap import indent


list1 = [1,2,3,4];
list1.sort(reverse=True);
print('Sorted list1: ', list1)
list2 = [1, 'Two', {'a': 4}, True, 2.3];

# Print an array
# Way-1: using *
print('Everything in list1: ', *list1);
# Way-2: using simple print and sep
print('Everything in list1: ', list1, sep=" ");
print('Everything in list2: ', list2, sep=" ");
# Way-3: using for loop
for x in list1:
    print('Value: ', x);

# Insert into array:
# at specified index: list.insert(index, value)
# after last index: list.append();
# add a new list to existing list: list.extend();

list1.insert(len(list1), 'new item using insert');
list1.append('Adding new item using append');
list1.extend(['Using extend: ', 5, 6, 7]);
print('List1 after adding: ', list1, sep=",")

# Deleting from array:
# Way-1: at specified index: list.pop(index);
# Way-2: using del keyword and specifying index

list2.pop(4);
print('List2 after deleting value at index 4: ', list2, sep=",")
del list1[3];
print('List1 after deleting value at index 3: ', list1, sep=",")


# ################## TUPLES ##################
# Same as lists but once declared cant change value
tuple1 = (1, 'Two', 'Two', True, 4.5);
# count occurrence of a value: 
print('Number of times `Two` is in tuple1: ', tuple1.count('Two'));
# Access an index and value: 
print('Index of 1: ', tuple1.index(1))
print(' Type of tuple1: ', type(tuple1));
print(' Value at index 1: ', tuple1[1]);


# ########################## Sets ##################

set1 = {1,2,3,4,5}; 
print('Everything in set1: ', set1);

set1.add(2); # does not print repeated values
set1.discard(4);
set1.remove(3);
print('Everything in set1 after: ', set1);

set2 = {6, 7, 8, 5};
print('*******************');
print('Everything in set1: ', set1);
print('Everything in set2: ', set2);
print('*******************');
print('set1 union set2: ', set1.union(set2));
print('set1 union set2 using pipe: ', set1 | set2);
print('*******************');
print('set1 intersetion set2: ', set1.intersection(set2));
print('set1 intersetion set2 using &: ', set1 & set2);
print('*******************');
# difference: gives values of first set not in second set
print('set1 difference set2: ', set1.difference(set2));
print('set1 difference set2 using -: ', set1 - set2);
print('*******************');
# symmetrical difference: elements in set a or set b but not in both
print('set1 symmetric_difference set2: ', set1.symmetric_difference(set2));
print('set1 symmetric_difference set2 using ^: ', set1 ^ set2);
print('*******************');

# ########################## Dictionaries ##################
dict1 = {1: 'coffee', 2: 'tea', 3: 'lemonade'};
# add to dict
dict1['Name'] = 'Srikar'
print('dict1: ', dict1)

print('&&&&&&&&&&&&&&&&&&&');
for key, value in dict1.items():
    print('Key: ', key);
    print('value: ', value);
