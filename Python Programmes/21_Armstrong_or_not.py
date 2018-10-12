# Program to check whether given number is amstrong or not
# x is to input the number to be checked
num=input("Enter the number: ")
sum=0
#temp=num is to use first value of num at line 11
temp=num
# while loop to check for amstrong
while num>0:
	digit=num%10
# the cube of the last digit of num is added in each execution of loop
	sum+=digit**3
	num=num/10
# if statement checks whether the sum is equal to the first num 
if sum==temp:
	print "Number is Armstrong"
else:
	print "Not Armstrong"
