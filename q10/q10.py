def is_prime(num):
    for x in range(2, int(num**0.5)+1):
        if num % x == 0:
            return False
    return True
sum = 0
for n in range(2, 2000001):
    if is_prime(n):
        sum += n
print sum
