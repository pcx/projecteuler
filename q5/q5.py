prime_factors = (2, 3, 5, 7, 11, 13, 17, 19)

def factorise(n, divisor, factors):
        if n % divisor == 0:
            if(factors.has_key(divisor)):
                factors[divisor] += 1
            else:
                factors[divisor] = 1
            factorise(n/divisor, divisor, factors)



factors_all = []
for n in range(20, 0, -1):
    factors = dict()
    for divisor in prime_factors:
        factorise(n, divisor, factors)
    factors_all.append(factors)


lcm_factors = dict()
for prime_factor in prime_factors:
    if not lcm_factors.has_key(prime_factor):
        lcm_factors[prime_factor] = 0
    for factors in factors_all:
        if factors.has_key(prime_factor):
            if factors[prime_factor] > lcm_factors[prime_factor]:
                lcm_factors[prime_factor] = factors[prime_factor]

value = 1
for prime_factor in prime_factors:
    if(lcm_factors.has_key(prime_factor)):
        value = value * (prime_factor**lcm_factors[prime_factor])

print value
