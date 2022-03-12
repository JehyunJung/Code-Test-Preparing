def solution(N,s,nums):
    start,end=0,0
    count=len(nums)
    sub_sum=nums[start]
    while True:
        if sub_sum==s:
            count=min(end-start+1,count)
            sub_sum-=nums[start]
            start+=1

        elif sub_sum < s:
            end+=1
            if end == N:
                break
            sub_sum+=nums[end]
        else:
            sub_sum-=nums[start]
            start+=1

    return count
    
if __name__ =="__main__":
  N,s=0,0
  nums=[]
  with open("input1806.txt","r") as file:
    N,s=map(int,file.readline().split())
    nums=list(map(int,file.readline().split()))

  print(solution(N,s,nums))