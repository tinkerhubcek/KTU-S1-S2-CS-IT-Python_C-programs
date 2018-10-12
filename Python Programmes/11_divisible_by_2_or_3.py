#A Given Number is Divisible By 2 or 3
n1=input("Enter the number:")

div=n1%10#For finding the final Term

if div%2==0:
	print ("The given number  a divisible of 2")
elif n1%3== 0:
	print("The given number is  divisible by 3")
elif div%2!=0:
	print("The given number is not divisible by 2")

	
	
