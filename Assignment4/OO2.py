import time
def NotBrute(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if(i<j and a[i]>a[j]):
                print("(",a[i],",",a[j],")")
a=list(map(int,input("> ").split()))
start=time.time()
NotBrute(a)
end=time.time()
run_time= end - start
n=len(a)
asym_time = n*n
ratio=run_time/asym_time
print('input size    : ',n)
print('running time  : ',run_time)
print('ratio         : ',ratio)