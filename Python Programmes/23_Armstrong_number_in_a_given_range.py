#Program to check whether given numbers in a range is amstrong or not 
# lw is to input the lower limit of range
# uw is to input the upper limit of range
lw=input("Enter the lower Bound: ")
uw=input("Enter the upper bound: ")
# for loop to check each number is anstrong or not in the range
for num in range(lw,uw+1):
	sum=0
	temp=num
	while num>0:
		digit=num%10
#the cube of the last digit of num is added in each execution of loop
		sum+=digit**3
		num=num/10
#if statement checks whether the sum is equal to the first num 
	if sum==temp:
		print temp

