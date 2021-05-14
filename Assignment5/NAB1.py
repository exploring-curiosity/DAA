import time


def Brute(s):
    new={}
    b = list(s.keys())
    n = list(s.values())
    for i in range(len(b)):
        for j in range(len(n)):
            if n[j] == b[i]:
                print("(b", i + 1, ",n", j + 1, ")")
                new[b[i]]=n[j]
    return new

b = list(map(int, input("bolt dimensions > ").split()))
n = list(map(int, input("nut  dimensions > ").split()))
s = dict(zip(b, n))
start = time.time()
s=Brute(s)
end = time.time()
run_time = start - end
a = max(len(b), len(n))
asym_time = a * a
ratio = run_time / asym_time
print(s)
print("Length of input: ", a)
print("Run time : ", run_time)
print("ratio : ", ratio)
