# python script to generate 4 digit number OTP

import random 
def otp():
    out=str(random.random())[-4:]
    return out 
out=otp()
print(out)
