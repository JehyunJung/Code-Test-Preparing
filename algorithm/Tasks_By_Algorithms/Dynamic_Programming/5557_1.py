def solution():
  dp=[[0] * 21 for _ in range(num-1)]
  dp[0][numbers[0]]=1
  
  for i in range(1,num-1):
    for value in range(21):
        if dp[i-1][value]!=0:
          if value+numbers[i]<=20:
            dp[i][value+numbers[i]]+=dp[i-1][value]
          if value-numbers[i]>=0:
            dp[i][value-numbers[i]]+=dp[i-1][value]

  print(dp[-1][numbers[-1]])
  
if __name__ == "__main__":
  num=0
  numbers=[]

  with open("input5557.txt","r") as file:
    num=int(file.readline())
    numbers=list(map(int,file.readline().split()))

  solution()
