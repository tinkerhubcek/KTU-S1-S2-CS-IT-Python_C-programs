# program to Display the pattern
#  *
#  * *	
#  * * *
# n inputs the number of lines
n=input("Enter the limit: ")
# num is set as *
num="*"
# nested for to printing each line 
for i in range(1,n+1):
	for j in range(1,i+1):
# print num in each line and "," is important to print next output in saame line
		print num,
# "/n" is next line
	print "\n"
