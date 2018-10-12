# program to find the factorial of a number
# x is to input the number
n=input("Enter the number:")
# f is assigned 1 to eliminate any junk values in f 
f=1
t=n
# while loop is to find the factorial
while(n>0):
	f=f*n
# n is decremented by 1
	n-=1
# the factorial is printed
print "The facorial of ",t ,"is ",f
