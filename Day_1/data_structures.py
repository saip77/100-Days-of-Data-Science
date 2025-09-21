### Data Structures

# Lists
my_list = [1, 2, 3, 4, 5]
print(my_list)
list_new = [[1, 2, 3], [4, 5, 6]]
print(list_new[0][1])

# List Methods
my_list.append(6)
print(my_list)
my_list.insert(1, 7)
print(my_list)
del my_list[1]
print(my_list)

# Tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Tuple Methods
print(my_tuple.count(2))
print(my_tuple.index(3))

# Sets
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Set Methods
my_set.add(6)
print(my_set)
my_set.remove(2)
print(my_set)


# Dictionaries
my_dict = {"name": "Sai Prasad", "age": 24, "city": "Bangalore"}
print(my_dict)

# Dictionary Methods
print(my_dict["name"])
print(my_dict.get("name"))
print(my_dict.get("state", "Not Available"))
my_dict["state"] = "Karnataka"
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())