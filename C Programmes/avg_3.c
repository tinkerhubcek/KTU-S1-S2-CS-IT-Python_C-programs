#include<stdio.h>
void main(){
float a,b,c,avg;
printf("Enter the first number:\n");
scanf("%f",&a);
printf("Enter the second number:\n");
scanf("%f",&b);
printf("Enter the third number:\n");
scanf("%f",&c);
avg=(a+b+c)/3.0;
printf("The average of %f,%f and %f is %f\n",a,b,c,avg);
}
