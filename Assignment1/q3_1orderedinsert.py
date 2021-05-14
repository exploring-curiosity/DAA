def ordered_insert(a):
    n = len(a)
    for i in range(0, n - 1):
        if i == 0:
            if a[n - 1] < a[n - 2]:
                a[n - 1], a[n - 2] = a[n - 2], a[n - 1]
            elif a[n - 1] >= a[n - 2]:
                break
        elif a[n - 2 - i] < a[n - 1 - i] < a[n - i]:
            break
        else:
            a[n - 1 - i], a[n - 2 - i] = a[n - 2 - i], a[n - 1 - i]


a = input("> ").split()
ordered_insert(a)
print("ordered list is ", a)
