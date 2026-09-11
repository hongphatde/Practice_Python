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
print(no_space("8 j 8   mBliB8g  imjB8B8  jl  B"))
print(no_space("8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" ))
print(no_space("8aaaaa dddd r     "))