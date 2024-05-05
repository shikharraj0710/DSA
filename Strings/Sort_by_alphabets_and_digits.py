str = '1AB2C3'
alphabets = []
digits = []
output = ''

for ch in str:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)

print(''.join(sorted(alphabets) + sorted(digits)))