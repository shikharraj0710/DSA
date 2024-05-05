str = 'a0b3c2d6'

# 1st method
output = ''
for index in range(0, len(str)):
    if index % 2 == 0 and str[index].isalpha():
        output += str[index] * int(str[index + 1])

print(output)

# 2nd method
dict = {}
index = 0
output1 = ''
while index <= len(str) - 1:
    dict[str[index]] = int(str[index + 1])
    index += 2

for [key, value] in dict.items():
    output1 += key * value

print(output1)
        