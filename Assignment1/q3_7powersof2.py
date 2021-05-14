def preordering(a):
    n=len(a)
    for i in range(0,n-1):
        if a[2**i]<a[2**(i+1)]:
            break
        else :
            a[2**i],a[2**(i+1)]=a[2**(i+1)],a[2**i]

a={}
n=int(input("enter the number of terms : "))
for i in range(0,n):
    a[2**i]=int(input("Enter number : "))
preordering(a)
print(a.values())