from math import inf

def solution():
    start,end=0,n-1
    answer=(numbers[start],numbers[end])
    min_sum=abs(numbers[start]+numbers[end])

    while start<end:
        temp=numbers[start]+numbers[end]

        if abs(temp) < min_sum:
            min_sum=abs(temp)
            answer=(numbers[start],numbers[end])
            if min_sum==0:
                break
        
        if min_sum >0:
            end-=1
        else:
            start+=1
        
    print(answer[0],answer[1])
 
if __name__ =="__main__":
    with open("input2467.txt","r") as file:
        n=int(file.readline())
        numbers=list(map(int,file.readline().split()))
    solution()