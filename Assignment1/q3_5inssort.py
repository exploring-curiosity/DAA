def ins_sort(a,n):
    if n == 0:
        return
    else:
        ins_sort(a,n-1)
        ordered_insert(a,n)


def ordered_insert(a, n):
    if n == 0:
        return
    elif a[n - 1] < a[n]:
        return
    else:
        a[n - 1], a[n] = a[n], a[n - 1]
        ordered_insert(a, n - 1)


a = input("> ").split()
ins_sort(a,len(a)-1)
print("ordered list is ", a)
