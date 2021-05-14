def PNF(a, low, high):
    count = 0
    i = low
    while i < high:
        if int(a[i]) < 0:
            count += 1
        i += 1
    i = low
    j = 0
    print(count)
    while j < count:
        if int(a[i]) < 0:
            i += 1
            j += 1
            continue
        else:
            a.insert(high - 1, a.pop(i))

    return count


a = input("> ").split(" ")
low = int(input("Low : "))
high = int(input("High : "))
n = PNF(a, low, high)
print(n)
print(a[low:low + n])
print(a[low + n:high])
