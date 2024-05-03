my_list = [1, 2, 3, 4, 5]


my_list.append(6)
print("List after adding element:", my_list)

my_list.remove(3)
print("List after removing element:", my_list)

my_list[0] = 0
print("List after modifying element:", my_list)

my_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict['d'] = 4
print("Dictionary after adding key-value pair:", my_dict)

del my_dict['b']
print("Dictionary after removing key:", my_dict)

my_dict['a'] = 0
print("Dictionary after modifying value:", my_dict)

my_set = {1, 2, 3, 4, 5}

my_set.add(6)
print("Set after adding element:", my_set)

my_set.remove(3)
print("Set after removing element:", my_set)


my_set.remove(1)
my_set.add(0)
print("Set after modifying element:", my_set)