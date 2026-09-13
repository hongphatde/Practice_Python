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
# Exercise 5: Sum Mixed Array
def sum_mix(arr):
    result = 0
    for number in arr:
        result += int(number)
    return result
        
print(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']))