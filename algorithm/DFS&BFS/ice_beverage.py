graph=[]
n,m=0,0

n,m=map(int,input().split())
for _ in range(n):
  graph.append(list(map(int,input())))

def dfs(y,x):
  if y<=-1 or y>=n or x <= -1 or x>=m:
    return False

  if graph[y][x]==0:
    graph[y][x]=1
    dfs(y-1,x)
    dfs(y,x+1)
    dfs(y+1,x)
    dfs(y,x-1)
    return True
  else:
    return False
result=0

"""
모든 노드에 대해서 DFS을 진행함으로써 서로 연결되어 있는 총 DFS 시행회수를 조사함으로써 
component 개수를 찾을 수 이다.
"""
for row in range(n):
  for col in range(m):
    if dfs(row,col):
      result+=1
      
print(result)
