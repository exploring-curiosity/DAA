def fibr(n):
	a=0
	b=1
	if(n==0):
		return 0
	for i in range(1,n):
		temp=b
		b=a+b
		a=temp
	return b
inp=int(input("Enter Number : "))
res=fibr(inp)
print("Result is " + str(res))
