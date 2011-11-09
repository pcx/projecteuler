"""
 To reach the other end one has to cross exactly 40 edges,
 of which 20 are vertical and 20 are horizontal,
 so no. of routes is the number of combinations of picking 20 edges out of 40
"""
from math import factorial

print factorial(40) / factorial(20)**2
