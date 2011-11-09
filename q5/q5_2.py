prime_factors = (2, 3, 5, 7, 11, 13, 17, 19)
value = 1
for prime_factor in prime_factors:
    for x in range(1, 6):
        if prime_factor**x > 20:
            break
    value = value * (prime_factor**(x-1))

print value
