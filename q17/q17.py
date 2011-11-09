words = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
    100 : 'hundred',
    1000 : 'thousand',
}

def spell_number(n, words):
    word = ""
    while True:
        if n == 1000:
            return words[1] + "" + words[1000]
        elif n >= 100:
            if n%100 == 0:
                return words[n/100] + words[100]
            else:
                return words[int(n/100)]+ words[100] + "and" + spell_number(n%100, words)
        elif not words.has_key(n):
            return words[int(n/10)*10] + spell_number(n%10, words)
        else:
            return words[n]

sum = 0
for n in [len(spell_number(n, words)) for n in range(1, 1001)]:
    sum += n
print sum
