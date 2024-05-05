str = 'Shikhar Raj'

# 1st Method - Slice Operator
# print(str[::-1])

# 2nd Method - reversed method - returns < reversed object >
reversed_str = reversed(str)
# for x in reversed_str:
#     print(x)

# print(''.join(reversed_str))

# 3rd Method
newStr = ''
index = len(str) - 1
while index >= 0:
    newStr += str[index]
    index -= 1

print(newStr)
