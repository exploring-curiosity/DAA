def fast_power(a,n):
    if(n==1):
        return a
    elif n%2==1:
        return a*power(a,n-1)
    else:
        x=power(a,n/2)
        return x*x


a=int(input("Enter the value of x : "))
n=int(input("Enter the value of power : "))
print("The result is ",fast_power(a,n))