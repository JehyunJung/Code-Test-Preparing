from collections import deque

def print_checked_row(graph):
  for i in range(num):
    print(graph[i])
  print()
  
def solution():
  checked=[[0] * (num) for _ in range(num)]
  checked[0][0]=1

  for i in range(num):
      for j in range(num): 
          if i==num-1 and j==num-1:
              return checked[num-1][num-1]
          value=graph[i][j]
          
          for new_i,new_j in [(i+value,j),(i,j+value)]:
              if new_i >=num or new_j >=num:
                  continue
                
              checked[new_i][new_j]+=checked[i][j]
            

    
if __name__ == "__main__":
  num=0
  graph=[]
  with open("input1890.txt","r") as file:
    num=int(file.readline())
    graph=[list(map(int,file.readline().split())) for _ in range(num)]

  print(solution())
  