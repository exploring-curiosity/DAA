def ordered_insert(a,n):
    temp=a[n]
    for i in range(1, n+1):
        if i==n:
            if a[0]>temp :
                a[1]=a[0]
                a[0]=temp
            else:
                a[1]=temp
        else:
            if(a[n-i]<temp):
                a[n-i+1]=temp
                break
            else:
                a[n-i+1]=a[n-i]


a = input("> ").split()
n = int(input("Enter n value : "))
ordered_insert(a,n)
print("ordered list is ", a)
