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

answer = ""

carrier = 0
for n in range(0, 52):
    sum_of_digits = 0
    for number in numbers:
        sum_of_digits += int(number[n])
    sum_of_digits += carrier
    answer += str(sum_of_digits % 10)
    carrier = int(sum_of_digits /10)

print answer[51:41:-1]
