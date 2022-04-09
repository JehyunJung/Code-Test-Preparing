def solution():
    dp=[0 for _ in range(n+1)]
    max_prize=0
    for i in range(n):
        time,prize=schedules[i][0],schedules[i][1]
        max_prize=max(dp[i],max_prize)
        if i+time <=n:
            dp[i+time]=max(dp[i+time],prize+max_prize)

    print(dp[n])

if __name__ == "__main__":
  n=0
  schedules=[]
  with open("input15486.txt","r") as file:
    n=int(file.readline())
    schedules=[list(map(int,file.readline().split())) for _ in range(n)]
  
  solution()