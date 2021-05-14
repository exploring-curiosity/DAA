import time
def Partition(a):
    b=list(a.keys())
    n=list(a.values())
    n1=[]
    n2=[]
    for i in range(len(n)):
        if n[i]<b[-1]:
            n1.append(n[i])
        elif n[i]>b[-1]:
            n2.append(n[i])
    n1+=n2
    n1.append(b[-1])
    return dict(zip(b,n1))


def NotBrute(a):
    if(len(a)==1):
        return a
    a=Partition(a)
    b=list(a.keys())
    x=a.pop(b[-1])
    a=NotBrute(a)
    a[b[-1]]=x
    return a


b = list(map(int, input("bolt dimensions > ").split()))
n = list(map(int, input("nut  dimensions > ").split()))
s = dict(zip(b, n))
start = time.time()
s=NotBrute(s)
end = time.time()
run_time = start - end
a = max(len(b), len(n))
asym_time = a * a
ratio = run_time / asym_time
print(s)
print("Length of input: ", a)
print("Run time : ", run_time)
print("ratio : ", ratio)