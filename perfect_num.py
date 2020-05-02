def sumPdivisors(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum

def is_perfect():
    for i in range(1, 500):
        if i == sumPdivisors(i):
            print(f'{i} is a perfect number.')

print(is_perfect())