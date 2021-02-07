# Exercise 5: Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence: 0.8475 '

# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

# Exercise 6: Read the documentation of the string methods at https://docs.python.org/library/stdtypes.html#string-methods You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.

# Answer
colon_pos = str.find(':')
extracted_str = str[colon_pos+1 : ].strip()
parsed_float = float(extracted_str)

print(parsed_float, 'is a', type(parsed_float))