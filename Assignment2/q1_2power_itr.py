def power(a,n):
    x=1
    for i in range(0,n):
        x*=a
    return x


a=int(input("Enter the value of x : "))
n=int(input("Enter the value of power : "))
print("The result is ",power(a,n))