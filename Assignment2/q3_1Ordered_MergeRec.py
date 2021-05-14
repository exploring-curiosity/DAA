def ordered_insert(e, a):
    if len(a) == 0:
        a.append(e)
        return a
    elif int(e) < int(a[0]):
        a.insert(0, e)
        return a
    else:
        b = ordered_insert(e, a[1:])
        b.insert(0, a[0])
        return b


def ordered_merge(u, v):
    if len(u) == 1:
        return ordered_insert(u[0], v)
    else:
        v = ordered_insert(u[len(u)-1], v)
        return ordered_merge(u[:len(u)-1],v)


a = input("Input a> ").split(" ")
b = input("Input b> ").split(" ")

b=ordered_merge(a,b)
print("Merged sequence : ",b)
