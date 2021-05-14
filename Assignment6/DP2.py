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


def TraceLISrec(n, ind):
    for i in range(0, ind):
        if n == l[ind - 1 - i]:
            if l[ind - 1 - i] == 1:
                lis.append(A[ind - 1 - i])
                return None
            else:
                TraceLISrec(l[p[ind - 1 - i]], p[ind - 1 - i] + 1)
                lis.append(A[ind - 1 - i])
                return None


lis = []
A = list(map(int, input("> ").split()))
l = [0 for i in range(0, len(A) + 1)]
p = [None for i in range(0, len(A) + 1)]
TraceLISrec(LengthDP(A, len(A)), len(A) - 1)
print(lis)
