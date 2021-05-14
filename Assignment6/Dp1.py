def LengthDP(b, n):
    a = b
    a.append(float('inf'))
    for j in range(0, n + 1):
        for i in range(0, j):
            if a[i] < a[j]:
                if l[i] > l[j]:
                    l[j] = l[i]
                    p[j] = i
        l[j] += 1
    return l[n] - 1


A = list(map(int, input("> ").split()))
l = [0 for i in range(0, len(A) + 1)]
p = [None for i in range(0, len(A) + 1)]
print("The max length of sequence is ", LengthDP(A, len(A)))

