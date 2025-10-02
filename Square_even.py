'''
Create a Python script that prints the squares of all even or odd numbers within the range of 100 to 200. 
Choose either even or odd numbers and document your choice in the code.'''
for num in range(100,201):
    if num % 2 == 0:
        print(f"{num}^2 = {num ** 2}")