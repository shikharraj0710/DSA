str1 = 'aaabbcccc'

# 1st method
# OUTPUT: a3b2c4
output = ''

dict = {}
index = 0
while index <= len(str1) - 1:
    if dict.get(str1[index]):
        dict[str1[index]] += 1
    else:
        dict[str1[index]] = 1
    index += 1

for [key, value] in dict.items():
    output += key + str(value)

print(output)

# 2nd method
# INPUT: aaabbcccc
# OUTPUT: 3a2b4c

output1 = ''
ch = str1[0]
index1 = 1
count = 1

while index1 <= len(str1) - 1:
    if ch == str1[index1]:
        count += 1
    else:
        output1 += str(count) + ch
        ch = str1[index1]
        count = 1
    index1 += 1

output1 += str(count) + ch

print(output1)