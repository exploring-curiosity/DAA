def read_array():
    a = input("> ").split()
    return a


def minimum(a):
    mini = int(a[0])
    pos=-1
    for i in range(1, len(a)):
        if int(a[i]) < mini:
            pos = i
            mini = int(a[i])
    return pos


print("the minimum index is ", minimum(read_array()))
