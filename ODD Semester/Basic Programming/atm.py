# atm currency notes countes minimum
# input section
target = int(input("Enter the amount to be withdrawal "))

# logic section
amount = target - 100  # to fix the minimum a one hundred note
twok = amount // 2000  # count of two hundred currency 
amount -=  twok * 2000  # update amount 

fiveh = amount // 500
amount -= fiveh * 500  # update amount 

twoh = amount // 200
amount -= twoh * 200  # update amount 

oneh = amount // 100 + 1  # + 1 for hundred note fix count in starting
tmp = f'''
Currency Count of Two Thousand:={twok:4}
Currency Count of Five Hundred:={fiveh:>4}
Currency Count of Two Hundred :={twoh:>4}
Currency Count of One Hundred :={oneh:>4}
'''

# display section
print(f"For the amount {target} minimum currency count")
print(tmp)