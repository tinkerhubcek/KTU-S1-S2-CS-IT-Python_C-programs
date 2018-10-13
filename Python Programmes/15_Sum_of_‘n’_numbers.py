# Program to find the sum numbers in a limit 
# n inputs the limit
n=input("Enter the Limit: ")
i=1
# s is the variable to store sum
s=0
while i<=n:
# line to input each number
	x=input("Enter the number ")
# s is added with x
	s=s+x
# loop variable i is incrimented by 1
	i+=1
# prints the sum
print("The sum of n numbers is",s)
