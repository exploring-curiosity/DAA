def ordered_insert(e, a):
    if len(a)==0:
        a.append(e)
        return a
    elif int(e) < int(a[0]):
        a.insert(0,e)
        return a
    else:
        b=ordered_insert(e,a[1:])
        b.insert(0,a[0])
        return b


a = input("> ").split(" ")
a=ordered_insert(a[0],a[1:])
print(a)