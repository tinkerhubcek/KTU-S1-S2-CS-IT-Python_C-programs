# Program to check whether given numbers in a range is prime or not 
# lw is to input the lower limit of range
# uw is to input the upper limit of range
lw=input("Enter the Lower Bound: ")
uw=input("Enter the Upper Bound: ")
# for loop to check each number not in the range
for num in range(lw,uw+1):
# checks whether num is > 1
	if num>1:
# loop for prime or not 
		for i in range(2,num):
			if num%i==0:
# there is no remainder the number is not prime loop breaks		
				break
# prints the prime number 
		else:
			print num
