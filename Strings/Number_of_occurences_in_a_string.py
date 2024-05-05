input = 'aaabbccddefgg'

dict = {}

for ch in input:
    dict[ch] = dict.get(ch, 0) + 1


for key, value in dict.items():
    print(key, value, sep="-")
