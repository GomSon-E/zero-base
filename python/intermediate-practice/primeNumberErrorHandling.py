class NotPrimeException(Exception):
    def __init__(self, num):
        super().__init__(f'{num} is not prime number')

class PrimeException(Exception):
    def __init__(self, num):
        super().__init__(f'{num} is prime number')

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            raise NotPrimeException(num)

    raise PrimeException(num)