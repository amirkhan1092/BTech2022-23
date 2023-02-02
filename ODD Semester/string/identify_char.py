# ch = input('Enter the single length string (character) ')
st = input('Enter the string: ').lower()
vowels = consonants = space = special = digits = 0
for ch in st:
    if ch in 'aeiou':
        vowels += 1
    elif ch.isalpha():  # 'a' <= ch <= 'z'
        consonants += 1
    elif ch.isdigit():  # '0' <= ch <= '9'
        digits += 1
    elif ch.isspace():
        space += 1
    else:
        special += 1

print(f'Number of Vowels: {vowels}')
print(f'Number of Consonants: {consonants}')   
print(f'Number of Digits: {digits}')
print(f'Number of Space: {space}')
print(f'Number of special char: {special}')            


