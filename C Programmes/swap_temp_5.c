#include<stdio.h>
void main(){
int num1,num2,temp;
printf("Enter the first number:\n");
scanf("%d",&num1);
printf("Enter the second number:\n");
scanf("%d",&num2);
temp=num1;
num1=num2;
num2=temp;
printf("The numbers are %d and %d",num1,num2);
}
