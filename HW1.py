# HW1.py
# Author: Angel Bien

# Question 1:
print("Question 1")
# Print Hello World like we did in class
print("Hello World")
# Question 2:
print("Question 2")
# Print the following:
# Your name
print("Angel Bien")
# Your age
print("18")
# Your favorite color
print("Black")
# Your favorite animal
print("Tiger")
# Question 3:
print("Question 3")
# Create a variable called "myName" and set it equal to your name
myName = "Angel Bien"
# Create a variable called "myAge" and set it equal to your age
myAge = "18"
# Create a variable called "myColor" and set it equal to your favorite color
myColor = "Black"
# Create a variable called "myAnimal" and set it equal to your favorite animal
myAnimal = "Tiger"
# Print the following:
# Hello, my name is <myName>
print("Hello, my name is " + myName)
# I am <myAge> years old
print("I am " + myAge + " years old")
# My favorite color is <myColor>
print("My favorite color is " + myColor)
# My favorite animal is <myAnimal>
print("My favorite animal is " + myAnimal)

# Question 4:
print("Question 4")
# Calculate the following and print the result:
# 2 + 2
print("4")
# 3 * 4
print("12")
# 5 - 6
print("-1")
# 8 / 2
print("4")
# Question 5:
print("Question 5")
# Create a variable called "num1" and set it equal to 2
num1 = "2"
# Create a variable called "num2" and set it equal to 3
num2 = "3"
# Create a variable called "num3" and set it equal to 4
num3 = "4"
# Create a variable called "num4" and set it equal to 5
num4 = "5"
# Calculate the following and print the result:
# num1 + num2
print("5")
# num3 * num4
print("20")
# num4 - num1
print("3")
# num2 / num1
print("1.5")
# Question 6: Write a program that asks the user for their name and then prints the following:
print("Question 6")
name1 = input ("What is your name?")
# Hello, <name>. Please enter three numbers.
print("Hello, " + name1 + ". Please enter three numbers.")
# The program should then ask the user for three numbers (floats) and print the following:
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
num3 = float(input("Enter a number: "))
# 1. The sum of the three numbers is <sum>
print ("The sum of the three numbers is " + str(float(num1) + float(num2) + float(num3)))
# 2. The product of the three numbers is <product>
print ("The product of the three numbers is " + str(float(num1) * float(num2) * float(num3)))
# 3. round the three numbers to the nearest integer and print the sum of the three rounded numbers divided by 3 
print ("The sum of the three rounded numbers divided by 3 is " + str(round(num1) + round(num2) + round(num3) / 3))
# 4. The average of the three numbers is <average>
print ("The average of the three numbers is " + str((float(num1) + float(num2) + float(num3)) / 3))
# Question 7: Ask the user for an input of a symbol (in the example its *)     
print("Question 7")
# Print a diamond of the symbol that looks like the following. Include the spaces and the | character. 
# Hint: the print("symbol", end="") with \t and \n characters will be useful here.
symbol = input("Enter a symbol: ")
print("    " + symbol + "    |")
print("   " + symbol + symbol + symbol + "   |")
print("  " + symbol + symbol + symbol + symbol + symbol + "  |")
print(" " + symbol + symbol + symbol + symbol + symbol + symbol + symbol + " |")
print("  " + symbol + symbol + symbol + symbol + symbol + "  |")
print("   " + symbol + symbol + symbol + "   |")
print("    " + symbol + "    |")
#    *     |
#   ***    |
#  *****   |
# *******  |
#  *****   |
#   ***    |
#    *     |
