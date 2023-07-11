# Section 2: Concept Questions [19 marks]

# 2.1 Write a function that takes in an input and checks to see if it’s an isogram. The function should return True or False.
# An isogram is a word where no letter is repeated. Examples include:
# ● "isogram"
# ● "uncopyrightable" ● “ambidextrously”
def is_isogram(word):
    word = word.lower()  
    return len(word) == len(set(word))  

print(is_isogram("uncopyrightable"))  
print(is_isogram("ambidextrously"))  
print(is_isogram("aabbcc"))  

