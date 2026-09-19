# Exercise 1: Remove String Spaces
def no_space(sentence):
    # Create a string 
    new_str = ""
    # Loop iterable of sentence
    for word in sentence:
    # Condition check space between words
        if word == " ":
            continue
        else:
            new_str += word
    return new_str
        
# Test case
#print(no_space("8 j 8   mBliB8g  imjB8B8  jl  B"))
#print(no_space("8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" ))
#print(no_space("8aaaaa dddd r     "))

# Exercise 2: Total amount of points
def points(games):
    point = 0
    # Get each element in games
    for game in games:
    # Convert to a list to separate the values.
        x,y = game.split(":")
    # Convert string to integer
        x = int(x)
        y = int(y)
        if x > y:
            point += 3
        elif x == y:
            point += 1
    return  point

#print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))
#print(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']))        

# Exercise 3: Expression Matter
# Note: without reordering the operands
def expression_matter(a,b,c):
# Create a list containing mathematical operations
    Result = [a+b+c, (a+b)*c, a*b*c, a+b*c, a*b+c, a* (b+c)]
# Use method max() to find the maximum value
    return max(Result)

# Test case
#print(expression_matter(2, 1, 2))
#print(expression_matter(2, 1, 1))
#print(expression_matter(3, 3, 3))
#print(expression_matter(5, 1, 3))

# Exercise 4: Count Sheep...
def count_sheep(sheepes):
# Solution 1
    # Sheep counter variable
    count = 0
    # Check each element 
    for sheep in sheepes:
    # If the sheep is in position (True), the count variable increases by 1
        if sheep == True:
            count += 1
    # If the sheep is not in position (False, null, underfined), the count variable equals 0
        else:
            count += 0
    return count 

# Solution 2
    #return sheepes.count(True)
# Test case
"""
print(count_sheep([True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]))
"""
# Exercise 5: Sum Mixed integer Array
def sum_mix(arr):
# Solution 1
    result = 0
    for number in arr:
        result += int(number)
    return result
# Solution 2
    #return sum([int(i) for i in arr])
# Test case        
#print(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']))

#Exercise 6: List Filtering 
def filter_list(exercise):
# Solution 1

    list_new = []
    
    for element in exercise:
        # Check if element is an integer. 
        if isinstance(element, int):
        # Add element list new
            list_new.append(element)
    return list_new

# Solution 2: Shorty
    #return [element for element in exercise if isinstance(element, int)]
# Test case
"""
print(filter_list([1,2,'aasf','1','123',123]))
print(filter_list([1,'a','b',0,15]))
print(filter_list([1,'a','b',0,15]))

"""
# Exercise 7: Reversed Words
def reverse_words(sentence):
# Solution 1
    # Reverse the characters in sentence
    sentence = sentence[::-1]
    # Receive the processed words
    result =""
    # Receive the characters that have passed
    word = ""
    
    for char in sentence:
        if char == " ":
        # Enter each word if a space is encountered.
            result += word[::-1] + " "
        # Reset word
            word = ""
        else:
            word += char
    # Enter the last word when there are no spaces.
    result += word[::-1]
    return result

# Solution 2
"""
    sentence_list = sentence.split()
    return " ".join(sentence_list[::-1])
"""

# Test case
#print(reverse_words("The greatest victory is that which requires no battle"))

# Exercise 8: Beginner Series #4 Cockroach
   # Exercise: exchange km/h to cm/s of Cockroach's speed
def cockroach_speech(speed):
    return speed // 0.036

# Test case
#print(cockroach_speech(1.08))
#print(cockroach_speech(2.7781687862099695))
#print(cockroach_speech(0.9353327640357478))

# Exercise 9: Remove the minimum
def remove_minimum(numbers):
# Solution 1

    # Return null list, if list don't have value
    if not numbers:
        return []
    # Find minimum value in numbers's variable
    minimum = min(numbers)
    # Set the index for the smallest number.
    index = numbers.index(minimum)
    # Return list new, don't mutable original list
    return numbers[:index] + numbers[index + 1:]

# Solution 2: Use enumerate() method
"""
    # Return null list, if list don't have value
    if not numbers:
        return []
    # Receive value of numbers's iterable 
    minimun_value = numbers[0]
    # Receive index of iterable
    minimun_index = 0
    # Loop numbers list with index, number 
    for index , number in enumerate(numbers):
        if number < minimun_value:
            minimun_value = number
            minimun_index = index 
    return numbers[:minimun_index] + numbers[minimun_index + 1:]
"""
# Test case
#print(remove_minimum([128, 374, 67, 398, 146, 60]))
#print(remove_minimum([304,153, 262, 28]))
#print(remove_minimum([192, 312]))

# Exercise 10: Subtract the sum
def subtract_sum(numbers):
    
    fruits = {1: 'kiwi', 2: 'pear', 3: 'kiwi', 4: 'banana', 5: 'melon', 6: 'banana', 7: 'melon',
        8: 'pineapple', 9: 'apple', 10: 'pineapple', 11: 'cucumber', 12: 'pineapple',
        13: 'cucumber', 14: 'orange', 15: 'grape', 16: 'orange', 17: 'grape', 18: 'apple',
        19: 'grape', 20: 'cherry', 21: 'pear', 22: 'cherry', 23: 'pear', 24: 'kiwi',
        25: 'banana', 26: 'kiwi', 27: 'apple', 28: 'melon', 29: 'banana', 30: 'melon',
        31: 'pineapple', 32: 'melon', 33: 'pineapple', 34: 'cucumber', 35: 'orange',
        36: 'apple', 37: 'orange', 38: 'grape', 39: 'orange', 40: 'grape', 41: 'cherry',
        42: 'pear', 43: 'cherry', 44: 'pear', 45: 'apple', 46: 'pear', 47: 'kiwi',
        48: 'banana', 49: 'kiwi', 50: 'banana', 51: 'melon', 52: 'pineapple', 53: 'melon',
        54: 'apple', 55: 'cucumber', 56: 'pineapple', 57: 'cucumber', 58: 'orange',
        59: 'cucumber', 60: 'orange', 61: 'grape', 62: 'cherry', 63: 'apple', 64: 'cherry',
        65: 'pear', 66: 'cherry', 67: 'pear', 68: 'kiwi', 69: 'pear', 70: 'kiwi', 71: 'banana',
        72: 'apple', 73: 'banana', 74: 'melon', 75: 'pineapple', 76: 'melon', 77: 'pineapple',
        78: 'cucumber', 79: 'pineapple', 80: 'cucumber', 81: 'apple', 82: 'grape', 83: 'orange',
        84: 'grape', 85: 'cherry', 86: 'grape', 87: 'cherry', 88: 'pear', 89: 'cherry',
        90: 'apple', 91: 'kiwi', 92: 'banana', 93: 'kiwi', 94: 'banana', 95: 'melon',
        96: 'banana', 97: 'melon', 98: 'pineapple', 99: 'apple', 100: 'pineapple'}

    
   
    # Convert the number to a string to iterate over its digits
    a_string = str(numbers)

    # Calculate the sum of digits
    total = 0
    for number in a_string:
        total += int(number)
    
    # Subtract the sum from the number
    result = numbers - total

    # If the result is in the fruits dictionary, print the associated fruit
    if result in fruits:
        return fruits[result]
    else:
        # If not, recursively call the function with the new number
        return subtract_sum(result)
    
    
#print(subtract_sum(325))
#print(subtract_sum(149))

# Exercise 11: Square Every Digit
def square_digits(numbers):
    
# Solution 1
    
    # Convert the number type INTEGER -> string
    num_str = str(numbers)
    # CREATE AN EMPTY STRING
    new_str = ""
    
    # Loops each element of string
    for number in num_str:
    # Convert the number to an interger to calculate the square of its element.
        new_str += str(int(number) ** 2)
    
    # Merge elements in a string and return a integer
    return int("".join(new_str))
    
  
# Solution 2: Use data type List
    """
    num_list = list(str(numbers))
    # Use list comprehension to square each element in num_list that save a string
    result = [str(int(number) ** 2) for number in num_list]
    
    return int("".join(result))
  
    """
# Test case
#print(square_digits(9119))
#print(square_digits(765))

# Exercise 12: Remove element
def remove_every_other(my_list):
    # Create a new empty list 
    list_new = []
    # Iterable element 
    for element in my_list[::2]:
        list_new.append(element)
    return list_new
    
# Solution 2: List comprehension
    #return [element for element in my_list[::2]]

# Test case
#print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
#print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Exercise 13: Invert values
def invert(value_list):
# Solution 1
    # Create a new empty list
    new_list = []
    # Iterable number interger in list
    for number in value_list:
    # Change the sign of the number
        new_list.append(-number)
    return new_list
    
    
# Solution 2: List comprehension
    #return [-number for number in value_list]
# Test case
#print(invert([1, -2, 3, -4, 5]))
#print(invert([1, 2, 3, 4, 5]))


# Exercise 14: Do I get bonus?
def bonus_time(salary, bonus):
    if bonus:
        return f"${salary * 10}"
    else:
        return f"${salary}"
    
print(bonus_time(10000, True))
print(bonus_time(25000, True))
print(bonus_time(300000, False))

# Exercise 15: The Feast of Many Beasts
def feast(beast, dish):
    # Check the first and last characters of the two strings
    return beast[0] == dish[0] and beast[-1] == dish[-1]

# Test case
print(feast("great blue heron", "garlic naan"))
print(feast("chickadee", "chocolate cake"))
print(feast("brown bear", "bear claw"))

