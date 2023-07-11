# Section 2: Concept Questions [19 marks]

# 2.1 Write a function that takes in an input and checks to see if it’s an isogram. The function should return True or False.
# An isogram is a word where no letter is repeated. Examples include:
# ● "isogram"
# ● "uncopyrightable" ● “ambidextrously”
def is_isogram(word):
    if not isinstance(word, str):
        raise ValueError('Your input need to be a string.')
    word = word.lower()  
    return len(word) == len(set(word)) 



# Section 3: Python Challenge [25 marks]
def calculate_classes(num_students):
    if not isinstance(num_students, int) or num_students <= 0:
        raise ValueError('Number of students should be a positive integer')

    # Number of classes can't be less than 2
    num_classes = max(2, (num_students + 29) // 30) 

    # Allocate students to classes as evenly as possible
    class_allocation = {f'Class {i+1}': num_students // num_classes for i in range(num_classes)}

    # Distribute the remaining students
    remainder = num_students % num_classes
    for i in range(remainder):
        class_allocation[f'Class {i+1}'] += 1

    print(f'Proposed Allocation: {num_classes} classes {class_allocation}')

# Testing the function with given examples
calculate_classes(31) 
calculate_classes(59)  
calculate_classes(87)  
calculate_classes(123)  
calculate_classes(21)  
