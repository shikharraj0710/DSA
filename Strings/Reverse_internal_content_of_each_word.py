str = 'This is my book.'

# 1st method - List Comprehension
array_of_str = str.split()
print(' '.join([x[::-1] for x in array_of_str]))

# 2nd method - without list comphrension (using new variable)
newStr = ''
for word in str.split():
    newStr = newStr + word[::-1] + " "
print(newStr)

# 3rd method - without list comphrension (using end seperator)
for word in str.split():
    print(word[::-1], end=" ")