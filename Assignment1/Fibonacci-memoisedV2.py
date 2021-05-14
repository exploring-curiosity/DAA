computed_dict ={#To store computed data in a dictionary
	0:0,
	1:1
}
def fibr(n):  #function to compute
	if(n in computed_dict):
		return computed_dict[n]
	elif(n==0):
		return 0
	elif(n==1):
		return 1
	else:
		res = fibr(n-2)+fibr(n-1)
		computed_dict[n]=res
		return res


#User interface
ch='y'
while(ch=='y'):
	inp=int(input("Enter number :"))
	fib=fibr(inp)
	print("result is " + str(fib))
	ch=input("Do you want to continue(y/n) : ")
