def preordering(a):
    n=len(a)
    for i in range(0,n-1):
        if a[i]<a[i+1]:
            break
        else :
            a[i],a[i+1]=a[i+1],a[i]


a=input("> ").split(" ")
preordering(a)
print("the ordered list is ",a)