import time
def max_subarray_sum_cubic (a) :
	maxi=int(a[0])
	sub=a[0:1]
	for i in range(0,len(a)):
		for j in range(i+1,len(a)+1):
			x=sum(a,i,j)
			if(maxi < x):
				maxi=x
				sub=a[i:j]
	return sub,maxi
	
def sum(a,i,j):
	s=0
	for z in range(i,j):
		s+=int(a[z])	
	return s	
start=time.time()			
a=input("> ").split(" ")
b=[]
b,s=max_subarray_sum_cubic(a)
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
