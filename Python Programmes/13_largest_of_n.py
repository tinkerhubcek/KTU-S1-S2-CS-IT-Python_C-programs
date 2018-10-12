#Program to find the largest of n numbers"
# x is to input the limit
x=input("Enter the Limit:")
# now largest is set to 0
i=0
large=0
#while is to input the n numbers and compare them to find the largest
while(i<x):
	n=input("Enter the number:")
#this if checks for the largest"
	if n>large:
		large=n
		i=i+1
#statement to print the largest
print "Largest Number is ",large
