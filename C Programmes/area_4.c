#include<stdio.h>
void main(){
int l,b,peri,area;
printf("Enter the Length: ");
scanf("%d",&l);
printf("Enter the Breadth: ");
scanf("%d",&b);
peri=2*(l+b);
area=l*b;
printf("The area of the rectangle is %d\n",area);
printf("The perimeter is %d \n",peri);
}
