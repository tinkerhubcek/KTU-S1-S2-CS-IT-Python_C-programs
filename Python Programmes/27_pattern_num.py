# program to Display the pattern
#  1

#  2	 3
	
#  4	 5     6
# n inputs the number of lines
n=input("Enter the limit: ")
# num = 1 not set any other junk value and as num 1 is printed
num=1
# for is nested for printing each line
for i in range(1,n+1):
	for j in range(1,i+1):
# print num in each line and "," is important to print next output in saame line
		print num,
		num+=1
# "/n" is next line
	print "\n"
