def merge(u,v):
    if len(u)==0:
        return v
    elif len(v)==0:
        return u
    else :
        if u[0]<v[0]:
            m=u.pop(0)
        else :
            m=v.pop(0)
        x=merge(u,v)
        x.insert(0,m)
        return x


a = input("Input a> ").split(" ")
b = input("Input b> ").split(" ")
b=merge(a,b)
print("Merged sequence : ",b)