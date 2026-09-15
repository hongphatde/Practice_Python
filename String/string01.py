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
print(reverse_words("The greatest victory is that which requires no battle"))

# Exercise 8: Beginner Series #4 Cockroach
   # Exercise: exchange km/h to cm/s of Cockroach's speed
def cockroach_speech(speed):
    return speed // 0.036

# Test case
print(cockroach_speech(1.08))
print(cockroach_speech(2.7781687862099695))
print(cockroach_speech(0.9353327640357478))

# Exercise 9: Remove the minimum
def remove_minimum(numbers):
    # Return null list, if list don't have value
    if not numbers:
        return []
   
    minimun_value = numbers[0]
    minimun_index = 0
    # Loop numbers list with iterable, number 
    for iterable, number in enumerate(numbers):
        if number < minimun_value:
            minimun_value = number
            minimun_index = iterable
    return numbers[:minimun_index] + numbers[minimun_index + 1:]

print(remove_minimum([128, 374, 67, 398, 146, 60]))
print(remove_minimum([304,153, 262, 28]))
print(remove_minimum([192, 312]))