"""
 This solution doesnt yet work correctly.
"""

import sys

if len(sys.argv) != 2:
    print "error: invalid usage, try $<program-name> <data-file>"
    sys.exit(2)

try:
    fin = open(sys.argv[1], "r")
except IOError:
    print "error: could not open file", sys.argv[1]
    sys.exit(2)

#saving each number as a string, but in reverse for easier indexing
#adding two more places making the index range to [0-51]
numbers = [("00"+line.strip())[::-1] for line in fin.readlines()]

#creating a list with sum of digits at an index n of all the numbers
sum_of_digits = []
for n in range(0, 52):
    sum_at_n = 0
    for number in numbers:
        sum_at_n += int(number[n])
    sum_of_digits.append(sum_at_n)

#instantiating an empty answer string
answer = ""
#instantiating an empty carriers dictionary
carriers = dict()
#function to calculate carrier at a position n

def carrier_at(n, sum_of_digits, carriers):
    if carriers.has_key(n):
        return carriers[n]
    else:
        carrier = 0
        if n > 0:
            carrier += int((sum_of_digits[n-1] + carrier_at(n-1, sum_of_digits, carriers)) / 10) % 10
        if n > 1:
            carrier += int((sum_of_digits[n-2] + carrier_at(n-2, sum_of_digits, carriers)) / 100) % 10
        carrier = carrier % 10
        if not carriers.has_key(n):
            carriers[n] = carrier
        return carrier

if __name__ == "__main__":
    for n in range(51, 41, -1):
        print "Calculating digit at", n
        digit_at_n = (sum_of_digits[n] + carrier_at(n, sum_of_digits, carriers)) % 10
        print "Digit at ", n, "is", digit_at_n
        print "Carrier at ", n, "is", carriers[n]
        answer += str(digit_at_n)
    print answer
