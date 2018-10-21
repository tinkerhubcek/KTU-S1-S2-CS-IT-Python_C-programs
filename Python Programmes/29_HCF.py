def hcf(x,y):
    if x>y:
            small=y
    else:
        small=x
    for i in range(1,small+1):
        if(x%i==0 and y%1==0):
            hcf=i
    return hcf
a=int(input("Enter the 1st Number: "))    
b=int(input("Enetr the 2nd Number: "))
print(hcf(a,b))    
