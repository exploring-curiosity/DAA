def read_array():
    a=input("> ").split()
    return a,len(a)
a,n=read_array()
print("The length is "+str(n))
print(a)