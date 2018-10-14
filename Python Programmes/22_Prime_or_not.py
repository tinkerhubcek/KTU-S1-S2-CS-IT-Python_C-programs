# Program to check whether given numbers is prime or not 
# num inputs the number to be checked 
num=input("Enter the number:")
# if statement checks whether num is larger than 1
if num>1:
# for loop is divide num with all numbers less than it check its prime or not
	for i in range(2,num):
		if num%i==0:
			print "Number is not prime"
# there is no remainder the number is not prime loop breaks			
			break
# prints the prime number
	else:
		print num,"is prime"
