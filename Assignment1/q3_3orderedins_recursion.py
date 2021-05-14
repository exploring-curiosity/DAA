def ordered_insert(a, n):
    if n == 0:
        return
    elif a[n - 1] < a[n]:
        return
    else:
        a[n - 1], a[n] = a[n], a[n - 1]
        ordered_insert(a, n - 1)


a = input("> ").split()
n = int(input("Enter n value : "))
ordered_insert(a, n)
print("ordered list is ", a)
