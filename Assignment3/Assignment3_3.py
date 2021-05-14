import time

def prefix_cal(a):
	s=0
	prefix_sum=[]	
	pos=0
	m=int(a[0])	
	for i in range(0,len(a)):
		s+=int(a[i])
		if(m<s):
			m=s
			pos=i
		prefix_sum.append(s)
	return prefix_sum[pos],pos

def suffix_cal(a):
	s=0
	pos=0
	suffix_sum=[]
	m=int(a[0])	
	for i in range(0,len(a)):
		s+=int(a[len(a)-i-1])
		if(m<s):
			m=s
			pos=i
		suffix_sum.append(s)
	return suffix_sum[pos],pos
	
def max_subarray_sum_lineararithmetic(a):
	if(len(a)==1):
		return int(a[0]),0,1	
	mid=len(a)//2
	sum1,st1,en1=max_subarray_sum_lineararithmetic(a[:mid])
	sum2,st2,en2=max_subarray_sum_lineararithmetic(a[mid:])
	suf_sum,suf_pos=suffix_cal(a[:mid])
	pre_sum,pre_pos=prefix_cal(a[mid:])
	if(sum1<sum2):
		if(sum2<suf_sum+pre_sum):
			return suf_sum+pre_sum,suf_pos,mid+pre_pos
		else:
			return sum2,mid+st2,mid+en2
	else:
		if(sum1<suf_sum+pre_sum):
			return suf_sum+pre_sum,suf_pos,pre_pos
		else:
			return sum1,st1,en1


start=time.time()	
a=input("> ").split(" ")
s,st,en=max_subarray_sum_lineararithmetic(a)
end=time.time()
run_time= end - start
n=len(a)
asym_time = n*n*n
ratio=run_time/asym_time
print('Max Sub_array : ',a[st:en+1])
print('Max sum       : ',s)	
print('input size    : ',n)
print('running time  : ',run_time)
print('ratio         : ',ratio)








































































































	

