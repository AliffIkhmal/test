# Lists

# fruits = ["apple", "banana", "cherry", "grapes"]
# print(fruits)

# # Accessing elements
# print(fruits[0])      # first element output: apple
# print(fruits[-1])     # last element output: grapes
# print(fruits[1:3])    # slicing output: ['banana', 'cherry']
# print(fruits[:2])     # slicing from start output: ['apple', 'banana']
# print(fruits[2:])     # slicing to end output: ['cherry', 'grapes']
# print(fruits[-3:-1])  # negative indexing slicing output: ['banana', 'cherry']

# # Modifying elements
# fruits[1] = "blueberry"
# print(fruits)  # output: ['apple', 'blueberry', 'cherry', 'grapes']

# # Adding elements
# fruits.append("orange")             # add to the end output: ['apple', 'blueberry', 'cherry', 'grapes', 'orange']
# fruits.insert(1, "kiwi")            # insert at index 1 output: ['apple', 'kiwi', 'blueberry', 'cherry', 'grapes', 'orange']
# fruits.extend(["mango", "papaya"])  # extend list output: ['apple', 'kiwi', 'blueberry', 'cherry', 'grapes', 'orange', 'mango', 'papaya']
# fruits += ["peach", "plum"]         # concatenate lists output: ['apple', 'kiwi', 'blueberry', 'cherry', 'grapes', 'orange', 'mango', 'papaya', 'peach', 'plum']
# fruits *= 1                         # repeat list output: ['apple', 'kiwi', 'blueberry', 'cherry', 'grapes', 'orange', 'mango', 'papaya', 'peach', 'plum']
# fruits.pop()                        # remove last element output: ['apple', 'kiwi', 'blueberry', 'cherry', 'grapes', 'orange', 'mango', 'papaya', 'peach']
# fruits.remove("kiwi")               # remove specific element output: ['apple', 'blueberry', 'cherry', 'grapes', 'orange', 'mango', 'papaya', 'peach']
# print(fruits)


# # List methods
# print(fruits.index("cherry"))    # find index output: 2
# print(fruits.count("apple"))     # count occurrences output: 1
# fruits.sort()                    # sort list output: ['apple', 'blueberry', 'cherry', 'grapes', 'mango', 'orange', 'papaya', 'peach']
# fruits.reverse()                 # reverse list output: ['peach', 'papaya', 'orange', 'mango', 'grapes', 'cherry', 'blueberry', 'apple']
# print(len(fruits))               # length of list output: 8
# print(fruits)                    # final list output: ['peach', 'papaya', 'orange', 'mango', 'grapes', 'cherry', 'blueberry', 'apple']

# # Iterating through a list
# for fruit in fruits:
#     print(fruit)

# excercise

grocery_list = ["milk", "butter", "bread", "biscuits"]
grocery_list.append("eggs")          #adding eggs to the list
grocery_list.remove("butter")        #removing butter from the list 
print(len(grocery_list))             #printing the length of the list
print(grocery_list)

#finding largest and smallest number in a list
numbers = [34, 1, 0, -23, 12, 99, 4]    
print("Largest number:", max(numbers))  
print("Smallest number:", min(numbers))

