# input section
amount = int(input('Enter the amount ')) 
amount -= 100  # secure a hundred note

# logic section 
twok = amount // 2000
amount %= 2000
fiveh = amount // 500
amount %= 500
twoh = amount // 200
amount %= 200
oneh = amount // 100  + 1

# display section 
print(f'No. of 100 Notes {oneh}')
print(f'No. of 200 Notes {twoh}')
print(f'No. of 500 Notes {fiveh}')
print(f'No. of 2000 Notes {twok}')
