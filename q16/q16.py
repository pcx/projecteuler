"""
 2^100 = (1 + 1)^1000
"""

from math import factorial

factorial_1000 = factorial(1000)

answer = 0
for r in range(0, 500):
    answer += factorial_1000 / (factorial(r) * factorial(1000-r))
answer = 2 * answer
answer += factorial_1000/factorial(500)**2

answer = str(answer)
sum_of_digits = 0
for digit in answer:
    sum_of_digits += int(digit)
print sum_of_digits
