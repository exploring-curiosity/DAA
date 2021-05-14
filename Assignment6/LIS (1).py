def LengthES(n):
	best=0		
	for i in range(0,n):
		for j in range(i):
			x=LengthES(j)
			if(A[j]<A[i] and x>best):
				best=x
	return best+1
			
A=list(map(int,input("> ").split()))


print("The max length of sequence is ",LengthES(len(A)))	

