str = 'This is my good book.'
array_of_str = str.split()

# 1st method
index = 0
while index <= len(array_of_str) - 1:
    if index % 2 == 0:
        print(array_of_str[index][::-1], end=" ")
    else:
        print(array_of_str[index], end=" ")
    index += 1

# 2nd method:
outputArray = []
for i in range(0, len(array_of_str)):
    if not (i % 2 == 0):
        outputArray.append(array_of_str[i])
    else:
        outputArray.append(array_of_str[i][::-1])

print(' '.join(outputArray))


