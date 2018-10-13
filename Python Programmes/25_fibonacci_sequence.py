# Program to print the fibonacci sequence
lim=input("Enter the Limit:")
# first number is assigned as 0
a=0
# second number is assigned as 1
b=1
count=0
# prints the first two numbers
print b,b"\t"
while (count<lim-1):	
# adds two numbers for third number in series	
	c=a+b
# prints the next number
	print c,"\t"
# now b becomes a and b becomes c 
	a=b
	b=c
	count+=1
