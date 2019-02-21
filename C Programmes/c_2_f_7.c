#include<stdio.h>
void main(){
float faren,celc;
printf("Enter the Temperature in Celcius: \n");
scanf("%f",&celc);
faren=(1.8*celc)+32;
printf("The temperature in Fahrenheit is %f \n",faren);
}
