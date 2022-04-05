from collections import deque

def print_checked_row(graph):
  for i in range(num):
    print(graph[i])
  print()
  
def solution():
  checked=[[0] * (num) for _ in range(num)]
  checked[0][0]=1

  queue=deque()
  queue.append((0,0))
  
  while queue:
    current_row,current_col=queue.popleft()
    value=graph[current_row][current_col]
    for new_row,new_col in [(current_row,current_col+value),(current_row+value,current_col)]:
      if new_row >=num or new_col >= num:
        continue

      checked[new_row][new_col]+=checked[current_row][current_col]
      
      if new_row==num-1 and new_col==num-1:
          continue
        
      queue.append((new_row,new_col))

  return checked[num-1][num-1]
    
if __name__ == "__main__":
  num=0
  graph=[]
  with open("input1890.txt","r") as file:
    num=int(file.readline())
    graph=[list(map(int,file.readline().split())) for _ in range(num)]

  print(solution())
  