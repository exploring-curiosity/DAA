def power(a,n):
    x=a
    i=1
    while i<n:
        if i%2==1:
            x*=a
            i+=1
        elif i*2<=n:
            x*=x
            i*=2
        else:
            x*=a
            i+=1
    return x


a=int(input("Enter the value of x : "))
n=int(input("Enter the value of power : "))
print("The result is ",power(a,n))