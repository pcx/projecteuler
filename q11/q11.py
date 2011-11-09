import sys

if len(sys.argv) != 2:
    print "error: wrong usage, try $<script-name> <input-file>"
    sys.exit(2)

try:
    fin = open(sys.argv[1], "r")
except IOError:
    print "error: could not find file", sys.argv[1]
    sys.exit(2)
else:
    print "status: Successfully opened data file"


rows = [line.strip() for line in fin.readlines()]
data = []
for row in rows:
    row1= []
    for element in row.split(" "):
        row1.append(int(element))
    data.append(row1)
print data[0][1]

largest = 0
product = 0
for rno in range(0, 20):
    for cno in range(0, 20):
        #row level sequence
        if(cno + 3 < 20):
            product = (data[rno][cno] * data[rno][cno + 1] *
                       data[rno][cno + 2] * data[rno][cno + 3])           
            if largest < product:
                largest = product
        #coloumn level sequence
        if(rno + 3 < 20):
            product = (data[rno][cno] * data[rno + 1][cno] *
                       data[rno + 2][cno] * data[rno + 3][cno])           
            if largest < product:
                largest = product
        #leftwards diagonal sequence
        if(rno - 3 >= 0 and cno + 3 < 20):
            product = (data[rno][cno] * data[rno - 1][cno + 1] *
                       data[rno - 2][cno + 2] * data[rno - 3][cno + 3])           
            if largest < product:
                largest = product
        #rightwards diagonal sequence
        if(rno + 3 < 20 and cno + 3 < 20):
            product = (data[rno][cno] * data[rno + 1][cno + 1] *
                       data[rno + 2][cno + 2] * data[rno + 3][cno + 3])           
            if largest < product:
                largest = product

print "Largest product is:", largest
