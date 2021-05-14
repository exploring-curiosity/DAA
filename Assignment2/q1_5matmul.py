class MyError(Exception):
    def __str__(self):
        return (repr("Exception : if matrix 1 is m*n then matrix 2 should be n*o"))


def mat_mul(a, b):
    c = []
    for i in range(0, len(a)):
        x=[]
        for j in range(0, len(b[0])):
            q=0
            for k in range(0, len(b)):
                q += a[i][k] * b[k][j]
            x.append(q)
        c.append(x)
    return c


try:
    m = int(input("enter the no of rows for matrix 1: "))
    n = int(input("enter the no of columns for matrix 1: "))
    a = []
    for i in range(0, m):
        x = []
        for j in range(0, n):
            x.append(int(input("> ")))
        a.append(x)

    m = int(input("enter the no of rows for matrix 2: "))
    o = int(input("enter the no of columns for matrix 2: "))
    b = []
    if (n != m):
        raise (MyError())
    for i in range(0, m):
        x = []
        for j in range(0, o):
            x.append(int(input("> ")))
        b.append(x)

    c = mat_mul(a, b)
    for r in c:
        print(r)

except MyError as error:
    print(error)