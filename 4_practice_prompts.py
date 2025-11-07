
# ----------------------------------------
# Print Practice Exercises
# ----------------------------------------

# Print Practice #1
# Write Python code that prints the sentence: I love learning Python
print("I love learning Python")


# Print Practice #2
# Write Python code that prints the sentence: Learning with 'TOTAL Python' is super fun!
print("Learning with 'TOTAL Python' is super fun!")


# Print Practice #3
# Write Python code that prints the number 555 to the screen as a result of a mathematical expression
print(500 + 55)

##############################################################################################################
# Find 3 objects around the room and create variables from it,
# Insert those variables into an f-string sentence(look at slide 22)in repl.it
laptop = "laptop"
owala ="owala"
pencil= "pencil"
print(f"On my desk, I have a {laptop}, a {owala}, and a {pencil}.")
# Familiarize yourself with the syntax of the print() function.
# Print your name.
# Print today's date.
# Print the name of your favorite movie.

print("Jackie")
print("11/07/2025")
print("trainspotting")

# Print your name and age on separate lines using a single print() function.
# Use f-strings to print a message like: "In 10 years, [Your Name] will be [Your Age + 10] years old."
name = "Jackie"
age = 16

print(f"{name}\n{age}")

print(f"In 10 years, {name} will be {age + 10} years old.")

##############################################################################################################

###########################String Practice##################################
#syntax is the way we write code
# print("Hello World")
# name = "John"
#in other languages, this is different
# in javascript for example, you define
#variables with let or const or var
#in python, you just give your variables a
#name and then define it with a value


#challenge
# find a summary of the movie blue beetle online and create a 
# variable called blue_beetle_summary and print it it out to the screen

# print the length of the summary
# upper case the entire summary
# print the summary
# print the summary in lowercase
# replace the word blue with red
# print the summary
# string index the word beetle and print it out
# print the last word of the summary
# print the summary in reverse
blue_beetle_summary = "Blue Beetle is a movie about Jaime Reyes, a teenager who discovers an ancient alien scarab that gives him superpowers. He becomes the Blue Beetle and must protect his family while learning how to control his new abilities."

print(len(blue_beetle_summary))

print(blue_beetle_summary.upper())

print(blue_beetle_summary.lower())

print(blue_beetle_summary.replace("Blue", "Red"))

print(blue_beetle_summary[blue_beetle_summary.index("Beetle"):blue_beetle_summary.index("Beetle") + len("Beetle")])

print(blue_beetle_summary.split()[-1])

print(blue_beetle_summary[::-1])


##########################input practice#############################################
#input is when we ask the user for input/data
# Ask the user to enter their name.

# Input Practice #1
# Write Python code that allows the user to enter their answer, by making them the following question:
# What are you learning today?
answer = input("What are you learning today? ")
print(answer)
# Your code must be able to print to the screen whatever is entered by the user (use the print function).

# Input Practice #2
# Write Python code that allows the user to enter their answer, by making them the following question:
# Where are you from?
location = input("Where are you from? ")
print(location)
# Your code must be able to print to the screen whatever is entered by the user (use the print function).

# Input Practice #3
# Write Python code that displays the user's full name on the screen, by allowing them to enter their first and last name with the following instructions:
# What is your name?

# What is your surname?
# The code must be able to print the user's first and last name on the screen, separated by a space.
first = input("What is your name? ")
last = input("What is your surname? ")
print(first + " " + last)
# Exercise:
# Write a program that asks the user for their name and favorite color, then prints a message using both pieces of information.

name = input("What is your name? ")
color = input("What is your favorite color? ")
print(f"{name} loves the color {color}.")







