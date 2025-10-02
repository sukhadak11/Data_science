'''
Write a Python program that checks whether a given number is prime or not. 
A prime number is a natural number greater than 1 that has no positive divisors 
other than 1 and itself.'''

def is_prime_number(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input())
print(is_prime_number(n))    