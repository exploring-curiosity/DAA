def read_array():
    a = input("> ").split()
    return a


def minimum(a, low, high):
    mini = int(a[low])
    pos = low
    for i in range(low + 1, high):
        if int(a[i]) < mini:
            pos = i
            mini = int(a[i])
    return pos


def sel_sort(a):
    for i in range(0, len(a) - 1):
        mind = minimum(a, i, len(a))
        a[i], a[mind] = a[mind], a[i]


ar = read_array()
sel_sort(ar)
print("Sorted array is ", ar)
