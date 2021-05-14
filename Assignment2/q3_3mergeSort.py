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


def merge_sort(u):
    if len(u) == 0:
        return u
    elif len(u) == 1:
        return u
    else:
        m = len(u) // 2
        return merge(merge_sort(u[:m]), merge_sort(u[m:]))


a = input("> ").split(" ")
print("Sorted array : ", merge_sort(a))
