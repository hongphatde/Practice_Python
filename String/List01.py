#Exercise 1: Count the MonKeys!
def make_count(numbers):
# Solution 1
# Create a empty list 
    number_list = []
# Add to the array of counted monkeys.
    for index in range(1,numbers + 1):
         number_list.append(index)
    return number_list
"""
# Solution 2: List Comprehension
    return [index for index in range(1,numbers + 1)]
# Test case
print(make_count(5))
print(make_count(1))
print(make_count(10))
"""
# Exercise 2
def sorter(textbook):
# Solution 1
    # Replace directly in the current list
    textbook.sort(key = str.lower)
    return textbook

# Solution 2: Use sorted()
"""
# Create a empty list
    after_sort = []
# Sorted list and then get each element
    for index in sorted(textbook, reverse=False, key = str.lower):
        after_sort.append(index)
    return after_sort
"""
# Test case
"""
print(sorter(['Algebra', 'history', 'Geometry', 'english']))
print(sorter(['Algebra', 'History', 'Geometry', 'English']))
print(sorter(['Alg#bra', '$istory', 'Geom^try', '**english']))
"""

# Exercise 3
def add_length(str_):
    list_words = str_.split()
    new_list = []
    for word in list_words:
        new_list.append(word + str(len(word)))
    return new_list

# print(add_length('you will win'))

# Exercise 4: Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    # Create a count variable and a sum of variable
    positive = 0
    negative = 0
    if not arr:
        return []
    # Loop each element
    for number in arr:
        # Check if the element is greater than zero.
        if number > 0:
            positive += 1
        # Check if the element is less than zero.
        elif number < 0:
            negative += number
        else:
            continue
    return [positive, negative]    

# Test case
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]))
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
print(count_positives_sum_negatives([]))