course = "Python for Beginners"
         #012345              // Index
#Methods
print(course.upper()) #Converts string to uppercase
print(course.lower()) #Converts string to lowercase
print(course.find("y")) #Returns index of the first occurance of the character in the string
print(course.find("Y")) #Sensitive to character cases
print(course.find("for")) #Can also return index for words/combined characters
print(course.replace("for", "4")) #Replaces string with another string // Returns a new string, does not modify it
print(course.replace("x", "4")) #Nothing happens if the characters are not present in the original string
print("Python" in course) #Returns a boolean
