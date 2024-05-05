input = 'a4k3b2'

# 1st method
output = ''
dict = {}
index = 0

while index <= len(input) - 1:
    if dict.get(input[index]):
        dict[input[index]] += 1
    else:
        dict[input[index]] = int(input[index + 1])
    index += 2

for [key, value] in dict.items():
    output += key + chr(ord(key) + int(value))

print(output)

# 2nd method
output1 = ''
index1 = 0
ch = ''
alphabet = ''

while index1 <= len(input) - 1:
    ch = input[index1]
    if ch.isalpha():
        alphabet = ch
    elif ch.isdigit():
        output1 += alphabet + chr(ord(alphabet) + int(ch))
    index1 += 1

print(output1)
    
