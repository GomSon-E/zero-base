import random

import primeNumberErrorHandling as p

primeNumbers = []

n = 0
while n < 10:

    num = random.randint(1, 1000)

    if num not in primeNumbers:

        try:
            p.isPrime(num)
        except p.NotPrimeException as e:
            print(e)
        except p.PrimeException as e:
            print(e)
            primeNumbers.append(num)

    else:
        print(f'{num} is overlapped number')

    n += 1

print(f'Prime Numbers: {primeNumbers}')