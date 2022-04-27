def solution(num):
    dp=[0] * (num+1)
    dp[1]=1
    dp[2]=2
    dp[3]=4
    for i in range(4,num+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    return dp
    
if __name__ == "__main__":
    testcases=0
    nums=[]
    with open("input9095.txt","r") as file:
        testcases=int(file.readline())
        nums=[int(file.readline()) for _ in range(testcases)]
    
    dp=solution(max(nums))
    for num in nums:
        print(dp[num])