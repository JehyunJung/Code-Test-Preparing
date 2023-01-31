def solution():
    maximum_uplimit=0
    start,end=0,1000000000

    while start <= end:
        mid=(start+end)//2
        total_request=0
        highest_request=0
        for request in requests:
            temp=min(request,mid)
            total_request+=temp
            highest_request=max(highest_request,temp)
        
        if total_request > budget:
            end=mid-1
        else:
            maximum_uplimit=max(maximum_uplimit,highest_request)
            start=mid+1
    
    print(maximum_uplimit)

if __name__ == "__main__":
    with open("input2512.txt","r") as file:
        n=int(file.readline())
        requests=list(map(int,file.readline().split()))
        budget=int(file.readline())
    solution()