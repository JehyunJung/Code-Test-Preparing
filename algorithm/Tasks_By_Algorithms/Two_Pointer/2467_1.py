from math import inf

def binary_search(l,r,value):
    min_sum=inf
    min_index=0
    while l <= r:
        mid=(l+r)//2
        temp=value + numbers[mid]

        if abs(temp) < min_sum:
            min_sum=abs(temp)
            min_index=mid
            if min_sum==0:
                break
                
        if temp <0:
            l=mid+1
        else:
            r=mid-1

    return min_sum,numbers[min_index]



def solution():
    min_sum=inf
    answer=[]
    for i in range(n-1):
        number=numbers[i]
        temp,value=binary_search(i+1,n-1,number)

        if temp < min_sum:
            min_sum=temp
            answer=[number,value]
    
    print(*answer)
            


 
if __name__ =="__main__":
    with open("input2467.txt","r") as file:
        n=int(file.readline())
        numbers=list(map(int,file.readline().split()))
    solution()