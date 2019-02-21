#include<stdio.h>
void main(){
int num,digit,sum=0;
printf("Enter a 3 digit number: \n");
scanf("%d",&num);
for(int i=0;i<=3;i++)
{
digit=num%10;
sum=sum+digit;
num=num/10;
}
printf("The sum of digits is %d\n",sum);
}
