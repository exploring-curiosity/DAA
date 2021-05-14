class MyError(Exception):
    def __str__(self):
        return repr("Exception : if matrix 1 is m*n then matrix 2 should be n*o")


def mat_power(a, n):
    if (n == 1):
        return a
    elif n % 2 == 1:
        return mat_mul(a,mat_power(a, n - 1))
    else:
        x = mat_power(a, n / 2)
        return mat_mul(x,x)


def mat_mul(a, b):
    c = []
    for i in range(0, len(a)):
        x = []
        for j in range(0, len(b[0])):
            q = 0
            for k in range(0, len(b)):
                q += a[i][k] * b[k][j]
            x.append(q)
        c.append(x)
    return c


try:
    n=int(input("Enter the n value : "))
    a=[[0,1],[1,1]]
    c = mat_power(a, n)
    b=[[0],[1]]
    z=mat_mul(c,b)
    print("> ",z[0])

except MyError as error:
    print(error)
