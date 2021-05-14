def fibr(n):
	if(n==0):
		return 0
	elif(n==1):
		return 1
	else:
		return fibr(n-1)+fibr(n-2)
inp=int(input("Enter number :"))
fib=fibr(inp)
print("result is " + str(fib))
