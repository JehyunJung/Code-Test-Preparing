def solution(temp,data):
    dp=[0] * (data+1)
    money_types=[1,2,3]
    dp[0]=1
    for money_type in money_types:
        for i in range(1,data+1):
          prev_step=i-money_type
          if prev_step>=0:
            dp[i]+=dp[prev_step]
    print(dp[data])
  
if __name__ =="__main__":
    testcases=0
    datas=[]
    with open("input15986.txt","r") as file:
      testcases=int(file.readline())
      for _ in range(testcases):
        datas.append(int(file.readline()))
    for data in datas:
      solution(0,data)