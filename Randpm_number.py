'''
Develop a Python program that generates two random numbers and asks the user to 
enter the product of these numbers. The program should then check if the user's 
answer is correct and display an appropriate message.'''

import random

n1 = random.randint(1,20)
n2 = random.randint(1,20)

user_answer = int(input(f"What is the product of {n1} and {n2}? "))

actual_answer = n1 * n2

if user_answer == actual_answer:
    print("Correct")
else:
    print(f"Wrong!, The correct answer is {actual_answer}")