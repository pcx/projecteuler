largest = 0
for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        z = x * y
        if z > largest:
            s = str(z)
            rs = s[::-1]
            if s == rs:
                largest = z
print largest
        
