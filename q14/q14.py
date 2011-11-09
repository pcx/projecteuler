cachedict = dict()
largest_chain_len = 0
starting_value = 0


for n in xrange(1, 1000001):
 #   print "calculating for n =", n
    num = n
    chain_len = 1
    while num != 1:
        if cachedict.has_key(num):
            next = cachedict[num]
        else:
            if num % 2 == 0:
                next = num/2
            else:
                next = (3*num) + 1
            cachedict[num] = next
        num = next
        chain_len += 1
    if chain_len > largest_chain_len:
        largest_chain_len = chain_len
        starting_value = n
print starting_value, chain_len
