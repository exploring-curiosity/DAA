def read_array():
    a = input("> ").split()
    return a


def minimum(a, low, high):
    mini = int(a[low])
    pos = -1
    for i in range(low + 1, high):
        if int(a[i]) < mini:
            pos = i
            mini = int(a[i])
    return pos


a = read_array()
low = int(input("Enter lower limit : "))
high = int(input("Enter higher limit : "))
print("the minimum index is ", minimum(a[2:3], low, high))
