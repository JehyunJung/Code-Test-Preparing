from collections import deque

def print_checked_row(graph):
  for i in range(num):
    print(graph[i])
  print()
  
def solution(row,col):
  if row==num-1 and col==num-1:
    return 1
  if dp[row][col] == -1:
    dp[row][col]=0
    
    value=graph[row][col]
    for new_row,new_col in [(row+value,col),(row,col+value)]:
      if new_row < 0 or new_row >= num or new_col <0 or new_col >=num:
        continue
      dp[row][col]+=solution(new_row,new_col)
    
  return dp[row][col]
  
if __name__ == "__main__":
  num=0
  graph=[]
  with open("input1890.txt","r") as file:
    num=int(file.readline())
    graph=[list(map(int,file.readline().split())) for _ in range(num)]
  dp=[[-1] * num for _ in range(num)]
  print(solution(0,0))
  