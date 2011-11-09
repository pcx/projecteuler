for a in range(1, 1000):
    for b in range(a, 1000):
        c = 1000 - a - b
        if c > 0:
            if c**2 == a**2 + b**2:
                print a*b*c
                break

"""
A far elegant way to get this done is:

Any Pythogorean triplet can be  represented as:
c = m^2+n^2
a = m^2-n^2
b = 2mn
where a^2 + b^2 = c^2

Sum of the triplet then is: 2m(m + n) = 1000 (according to the question)

Since n > 0
=> m+n > m
=> m^2 < 500
=> m < sqrt(500)
=> m < 24       -----> (1)

since a = m^2 - n^2 > 0
=> m > n       -----> (2)

since m(m+n) = 500
factorsing gives that only possible combinations for m and m+n are:
1 x 500
2 x 250
4 x 125
20 x 25

using equations (1) and (2), we have
m = 20
n = 5

=> c = 425, a = 375, b = 200
=> abc = 31875000

"""
