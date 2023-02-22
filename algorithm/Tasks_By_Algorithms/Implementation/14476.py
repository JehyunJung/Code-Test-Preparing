from math import gcd

def solution():
    l2r=[numbers[0]]*n
    r2l=[numbers[n-1]]*n

    #왼쪽에서 오른쪽으로의 누적 최대공약수
    for i in range(1,n):
        l2r[i]=gcd(l2r[i-1],numbers[i])
    
    #오른쪽에서 왼쪽으로의 누적 최대공약수
    for i in range(n-2,-1,-1):
        r2l[i]=gcd(r2l[i+1],numbers[i])
    

    answer=[]

    for i in range(n):
        max_gcd=0
        if i==0:
            max_gcd=r2l[1]

        elif i==n-1:
            max_gcd=l2r[n-2]
        else:
            max_gcd=gcd(l2r[i-1],r2l[i+1])
        
        if numbers[i] % max_gcd !=0:
            answer.append((max_gcd,numbers[i]))

    answer.sort(key=lambda x: -x[0])
    print(" ".join(map(str,answer[0])) if answer else -1)

        

if __name__ == "__main__":
    with open("input14476.txt","r") as file:
        n=int(file.readline())
        numbers=list(map(int,file.readline().split()))
    solution()