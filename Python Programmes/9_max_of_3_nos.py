#Max of 3 Numbers

n1=input("Enter the 1st number: ")
n2=input("Enter the 2nd number: ")
n3=input("Enter the 3rd number: ")

#Using The Max Function

m1=max(n1,n2)
m2=max(n2,n3)
m3=max(n1,n3)

#Conditional Block

if m1>m2:
	print(m1)
elif m2>m3:
	print(m2)	
elif m3>m1 or m3>m2:
	print(m3)
