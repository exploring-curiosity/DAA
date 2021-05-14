def print_array(a,low,high):
    for i in range(low,high):
        print(a[i],end=" ")
a=input("> ").split(" ")
low=int(input("Enter lower limit : "))
high=int(input("Enter higher limit : "))
print_array(a,low,high)