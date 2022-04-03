from collections import deque
from math import inf
def solution():
  queue=deque()
  queue.append((1,0))

  check[1][0]=0
  
  while queue:
    temp,clipboard=queue.popleft()

    if check[temp][temp]==-1:
        check[temp][temp]=check[temp][clipboard]+1
        queue.append((temp,temp))
        
    if 0<=temp + clipboard<=1000:
      if check[temp+clipboard][clipboard] ==-1:
        check[temp+clipboard][clipboard]=check[temp][clipboard]+1
        queue.append((temp+clipboard,clipboard))
                
    if 0<=temp-1<=1000:
      if check[temp-1][clipboard] == -1:
        check[temp-1][clipboard]=check[temp][clipboard]+1
        queue.append((temp-1,clipboard))
  
if __name__ =="__main__":
  target=0
  with open("input14226.txt","r") as file:
    target=int(file.readline())
    
  check=[[-1] *1001 for _ in range(1001)]
  
  solution()
  answer=inf
  for i in range(1001):
    if check[target][i] !=-1:
      answer=min(answer,check[target][i])

    
  print(answer)