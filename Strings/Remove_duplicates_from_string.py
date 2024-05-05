string = 'aaaabbbbcccdefff'

print(set(string))

output = ''
for ch in string:
    if ch not in output:
        output += ch

print(output)