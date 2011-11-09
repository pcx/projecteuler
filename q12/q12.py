i = 1
while 1:
    count = 1
    n = i * (i + 1) / 2
    for x in range(1, int(n**0.5)+1):
        if n % x == 0:
            count += 2
    if count > 500:
        break
    i += 1
print "The smallest such number is:", n
