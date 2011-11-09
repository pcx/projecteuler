def is_prime(num):
    for x in range(2, int((num**0.5)) + 1):
        if num % x == 0:
            return False
    return True

def get_next_prime(num):
    while 1:
        num += 1
        if is_prime(num):
            break
    return num

prime = 1
for n in range(1, 10002):
    prime = get_next_prime(prime)
print prime
