def solution():
    range_sum=sum(visitors[:x])
    max_value,max_count=range_sum,1
    start=0

    for i in range(x,n):
        range_sum+=visitors[i]
        range_sum-=visitors[start]
        start+=1

        if range_sum > max_value:
            max_count=1
            max_value=range_sum
        elif range_sum == max_value:
            max_count+=1
              
        
    #최대값이 0인 경우에 "SAD" 출력
    if max_value ==0 :
        print("SAD")
    else:
        print(max_value)
        print(max_count)


if __name__ == "__main__":
    with open("input21921.txt","r") as file:
        n,x=map(int,file.readline().split())
        visitors=list(map(int,file.readline().split()))

    solution()