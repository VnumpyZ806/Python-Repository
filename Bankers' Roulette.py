Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']
>>> names = names_string.split(", ")
... 
... import random
... 
... # Get the total number of items in list.
... num_items = len(names)
... # Generate random numbers between 0 and the last index. 
... random_choice = random.randint(0, num_items - 1)
... # Choose and print a random name.
... print(names[random_choice])
SyntaxError: multiple statements found while compiling a single statement
