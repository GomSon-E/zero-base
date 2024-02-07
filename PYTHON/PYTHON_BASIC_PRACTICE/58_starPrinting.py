for i in range(1, 6) :
    print('*' * i)

print('=' * 20)

for i in range(1, 6) :
    print(' ' * (5 - i), end='')
    print('*' * i)

print('=' * 20)

for i in range(5, 0, -1) :
    print('*' * i)

print('=' * 20)

for i in range(5, 0, -1) :
    print(' ' * (5 - i), end='')
    print('*' * i)

print('=' * 20)

for i in range(1, 10):
    if i <= 5 :
        print('*' * i)
    else :
        print('*' * (10 - i))

print('=' * 20)

for i in range(0, 5) :
    for j in range(0, 5) :
        if i == j :
            print('*', end='')
        else :
            print(' ', end='')
    print()

print('=' * 20)

for i in range(0, 5) :
    for j in range(0, 5) :
        if i + j == 4 :
            print('*', end='')
        else :
            print(' ', end='')
    print()

print('=' * 20)

for i in range(1, 11):
    if i <= 5 :
        print(' ' * (5 - i), end='')
        print('*' * (2 * i - 1), end='')
        print(' ' * (5 - i), end='')
    else :
        print(' ' * (i - 6), end='')
        print('*' * ((-2 * i) + 21), end='')
        print(' ' * (i - 6), end='')
    print()