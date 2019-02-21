#include<stdio.h>
void main(){
	int n1,n2,n3;
	printf("Enter the First number:");
	scanf("%d",&n1);
	printf("Enter the Second number:");
        scanf("%d",&n2);
n3=n1+n2;
n1=n3-n1;
n2=n3-n1;
printf("The first number is %d\n and the second number is %d\n",n1,n2);
}
