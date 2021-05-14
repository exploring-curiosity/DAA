def power(a,n):
    if n==1:
        return a
    else:
        return a*power(a,n-1)


a=int(input("Enter the value of x : "))
n=int(input("Enter the value of power : "))
print("The result is ",power(a,n))