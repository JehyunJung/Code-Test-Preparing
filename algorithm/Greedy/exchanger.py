from math import inf
def exchanger1(n):
    money_types=[500,100,50,10]
    count=0
    for money_type in money_types:
      count+=(n)//money_type
      n%=money_type

    print(count)

def exchanger2(n):
  dp=[inf] * (n+1)

  dp[0]=0

  for i in range(10,n+1,10):
    temp=inf
    if i >=500:
      temp=min(temp,dp[i-500])
    if i >=400:
      temp=min(temp,dp[i-400])
    if i >=100:
      temp=min(temp,dp[i-100])
    if i >=50:
      temp=min(temp,dp[i-50])
    dp[i]=temp+1

  print(dp)


if __name__ == "__main__":
  n=int(input())
  exchanger1(n)
  exchanger2(n)