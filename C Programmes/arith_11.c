#include<stdio.h>
void main(){
int n1,n2,choice,sum,diff,prod;
float quo;
printf("Enter two numbers\n");
scanf("%d",&n1);
scanf("%d",&n2);
printf("Enter your choice \t 1 \t 2 \t 3 \t 4  \t:\n");
scanf("%d",&choice);
switch(choice){
case 1:
sum=n1+n2;
printf("Sum is %d\n",sum);
break;
case 2:
diff=n1-n2;
printf("Difference is %d\n",diff);
break;
case 3:
prod=n1*n2;
printf("Product is %d\n",prod);
break;
case 4:
quo=n1/n2;
printf("Quotient is %f\n",quo);
break;
}
}

