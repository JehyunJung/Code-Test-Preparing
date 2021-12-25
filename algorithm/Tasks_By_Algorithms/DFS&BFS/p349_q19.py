from math import inf

def dfs(count,result,add,sub,mul,div):
  if count==n:
    global min_sum,max_sum
    min_sum=min(min_sum,result)
    max_sum=max(max_sum,result)
  
  else:
    if add>0:
      dfs(count+1,result+operands[count],add-1,sub,mul,div)
    if sub>0:
      dfs(count+1,result-operands[count],add,sub-1,mul,div)
    if mul>0:
      dfs(count+1,result*operands[count],add-1,sub,mul-1,div)
    if div>0:
      dfs(count+1,int(result/operands[count]),add,sub,mul,div-1)

n = 0
operands = []
add,sub,mul,div=0,0,0,0
temp = []
with open("input19.txt", "r") as file:
    n = int(file.readline())
    operands = list(map(int, file.readline().split()))
    add,sub,mul,div = map(int, file.readline().split())

min_sum = inf
max_sum = 0

dfs(1,operands[0],add,sub,mul,div)

print(max_sum, min_sum, sep="\n")
