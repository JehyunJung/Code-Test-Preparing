from collections import defaultdict
def solution():
    number_range=defaultdict(int)

    start,end=0,0
    max_length=0
    while end < n:
        number_range[numbers[end]]+=1
        while start < end and number_range[numbers[end]]>k:
            number_range[numbers[start]]-=1
            start+=1
        
        max_length=max(max_length,end-start+1)
        end+=1
    

    print(max_length)

if __name__ == "__main__":
    with open("input20922.txt","r") as file:
        n,k=map(int,file.readline().split())
        numbers=list(map(int,file.readline().split()))
    solution()