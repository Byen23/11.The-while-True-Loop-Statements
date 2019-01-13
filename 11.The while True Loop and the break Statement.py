# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 2019

@author: Byen23
"""
# This will be the 11th program to be uploaded to Github.

"""Count Control with a While Loop"""

# Summation with a for loop

theSum = 0

for count in range(1, 100001):
	theSum += count
print(theSum)

# Summation with a while loop
theSum = 0
count = 1

while count <= 100000:
	theSum += count
	count += 1
print(theSum)

"""The next example shows two versions of a script that counts down, from an upper bound of 10 to a lower bound of 1."""

# Counting down with a for loop

for count in range(10, 0, -1):
	print(count,"\n", end = " ")
	
# Counting down with a while loop

count = 10

while count >= 1:
	print(count, end = "")
	count -= 1
	
# The while True Loop and the break statement

theSum = 0.0

while True:
	data = input("Enter a number or just enter to quit: ")
	if data == "":
		break
	number = float(data)
	theSum += number
print("The sum 1s", theSum)

"""Our next example modifies the input section of the grade-conversion program to continue taking input numbers from the user until she enters an acceptable value. The logic of this loop is similar to that of the previous example"""

while True:
	number = int(input("Enter the numeric grade: "))
	if number >= 0 and number <= 100:
		break
	else:
		print("Error: grade must be between 100 and 0")
print(number) # Just echo the valid input


""" Here is a version of the numeric input loop that uses a Boolean variable:"""

done = False

while not done:
	number = int(input("Enter the numeric grade: "))
	if number >= 0 and number <= 100:
		done = True
	else:
		print("Error: grade must be between 100 and 0")
print(number) 


	