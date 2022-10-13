"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(number): # determines if number is prime

    for x in range(2, number):
        if number % x == 0:
            return 0
    else:
        return 1
    
def primes(number_of_primes):
    list = []
    i=2 # 2 is the first prime number
    while len(list)<number_of_primes: 
        if is_prime(i) == 1:
            list.append(i)
        i+=1

    return list
