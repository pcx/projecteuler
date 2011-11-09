"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

http://projecteuler.net/problem=1
"""
sum = 0
for x in range(1,1000):
    if x%3 == 0 or x%5==0:
        sum += x
print sum
