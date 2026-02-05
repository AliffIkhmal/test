# tupples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
# Accessing elements
print(my_tuple[0])      # first element output: 1
print(my_tuple[-1])     # last element output: 5
print(my_tuple[1:3])    # slicing output: (2, 3)
print(my_tuple[:2])     # slicing from start output: (1, 2)
print(my_tuple[2:])     # slicing to end output: (3, 4, 5)
print(my_tuple[-3:-1])  # negative indexing slicing output: (3, 4)

# Tuples are immutable, so we cannot modify elements
my_tuple[1] = 10  # This will raise a TypeError
print(my_tuple)

# However, we can concatenate tuples to create a new one
new_tuple = my_tuple + (6, 7)
print(new_tuple)  # output: (1, 2, 3, 4, 5, 6, 7)
# Tuple methods

print(my_tuple.index(3))    # find index output: 2 
print(my_tuple.count(1))     # count occurrences output: 1
print(len(my_tuple))         # length of tuple output: 5

# Iterating through a tuple
for item in my_tuple:
    print(item)

# excercise
