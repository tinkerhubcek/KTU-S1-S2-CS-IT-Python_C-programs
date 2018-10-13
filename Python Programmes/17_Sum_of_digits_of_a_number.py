# Program to find the sum of digts of a number
num=input("Enter the digits: ")
# s = 0 for eliminating any junk value that was in s 
s=0
# num is assigned to t for using in line 11
t=num

while num>0:
# this line inputs the last digit in the num to dig
	dig=num%10
# dig add to s for sum
	s=s+dig
# line decrese the number by one digit
	num=num/10
# prints the sum of digits
print "The sum of",t," is ",s
