def solution():
    dp=[0]*(5001)
    dp[0]=1
    for n in range(2,5001,2):
        for i in range(2,n+1,2):
            dp[n]+=(dp[i-2]*dp[n-i])
          
    for num in nums:
        print(dp[num]% 1000000007)
      
if __name__ == "__main__":
    testcases=0
    nums=[]
    with open("input10422.txt","r") as file:
      testcases=int(file.readline())
      nums=[int(file.readline()) for _ in range(testcases)]
    solution()