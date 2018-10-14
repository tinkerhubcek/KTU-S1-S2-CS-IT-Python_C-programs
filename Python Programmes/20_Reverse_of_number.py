# Program to print the reverse of the given number
## num inputs the number
num=input("Enter the number:")
# rev = 0 for eliminating any junk value that was in rev 
rev=0
# loop to reverse the number
while num>0:
# this line inputs the last digit in the number to r
	r=num%10
# this line multipies to revto 10 and add r to it
	rev=(rev*10)+r
# line decrese the number by one digit
	num=num/10
# prints the reverse
print "Reverse  is",rev
