# In Python we have a concept of slicing 
string = "Kabir Karim"
print(string[0:5])  # Output: Kabir 
print(string[6:11])  # Output: Karim
# string slicing can also be done using negative indexing
print(string[-11:-6])  # Output: Kabir
print(string[-5:])  # Output: Karim

# String Data type is immutable, which means we cannot change the value of a string once it is created. However, we can create a new string based on the existing string.

#String Functions
# 1. len() function returns the length of the string.
print(len(string))  # Output: 11

# 2. lower() function returns the string in lowercase.
print(string.lower())  # Output: kabir karim

# 3. upper() function returns the string in uppercase.
print(string.upper())  # Output: KABIR KARIM

# 4. strip() function returns the string with leading and trailing whitespace removed.
string_with_whitespace = "   Kabir Karim   "
print(string_with_whitespace.strip())  # Output: Kabir Karim

# 5. replace() function returns a new string with all occurrences of a substring replaced with another substring.
print(string.replace("Kabir", "Alice"))  # Output: Alice Karim

# 6. find() function returns the index of the first occurrence of a substring.
print(string.find("Kabir"))  # Output: 0
print(string.find("Karim"))  # Output: 6

# 7. count() function returns the number of occurrences of a substring.
print(string.count("a"))  # Output: 2

# 8. capitalize() function returns the string with the first character capitalized and the rest of the characters in lowercase.
print(string.capitalize())  # Output: Kabir karim

# 9. title() function returns the string with the first character of each word capitalized.
print(string.title())  # Output: Kabir Karim

# 10. endswith() function returns True if the string ends with the specified suffix, otherwise False.
print(string.endswith("Karim"))  # Output: True
print(string.endswith("Kabir"))  # Output: False

# 11. startswith() function returns True if the string starts with the specified prefix, otherwise False.
print(string.startswith("Kabir"))  # Output: True
print(string.startswith("Karim"))  # Output: False

