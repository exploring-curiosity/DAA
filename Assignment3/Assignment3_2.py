import time
prefix_sum=[]
def max_subarray_sum_quadratic (a) :
	prefix_cal(a)	
	maxi=int(a[0])
	sub=a[0:1]
	for i in range(0,len(a)):
		for j in range(i+1,len(a)+1):
			x=sum(a,i,j)
			if(maxi < x):
				maxi=x
				sub=a[i:j]
	return sub,maxi

def prefix_cal(a):
	s=0
	for i in range(0,len(a)):
		prefix_sum.append(s)		
		s+=int(a[i])
	prefix_sum.append(s)	
	
def sum(A,i,j):
	return prefix_sum[j]-prefix_sum[i]

start=time.time()	
a=input("> ").split(" ")
b=[]
b,s=max_subarray_sum_quadratic(a)
end=time.time()
run_time= end - start
n=len(a)
asym_time = n*n*n
ratio=run_time/asym_time
print('Max Sub_array : ',b)
print('Max sum       : ',s)	
print('input size    : ',n)
print('running time  : ',run_time)
print('ratio         : ',ratio)
