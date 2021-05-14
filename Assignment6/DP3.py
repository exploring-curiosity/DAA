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


def TraceLISitr():
    le = LengthDP(A, len(A))
    k = 0
    n = len(A) - 1
    m = l.index(le)
    while True:
        lis.append(A[m])
        if (p[m] is None):
            break
        m = p[m]
    lis.reverse()

lis = []
A = list(map(int, input("> ").split()))
l = [0 for i in range(0, len(A) + 1)]
p = [None for i in range(0, len(A) + 1)]
TraceLISitr()
print(lis)
