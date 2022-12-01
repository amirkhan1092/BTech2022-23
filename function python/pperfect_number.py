def perfect(n) :
    sum=0
    for i in range(1,n) :
        if(n%i==0) :
            sum =sum+i
    if(sum==n) :
        return "Perfect"
    else :
        return "Not perfect"

# main code
num = int(input('Enter the number ')) 
out = perfect(num)
print(out)       