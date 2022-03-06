import math
num1,num2=map(int,input().split())
bigger_num=max(num1,num2)
gcd=bigger_num
lcm=0

for i in range(bigger_num,-1,-1):
    if num1 % i==0 and num2 % i ==0:
        gcd=i
        break
lcm=num1//gcd * num2//gcd * gcd

print(lcm)
print(gcd)