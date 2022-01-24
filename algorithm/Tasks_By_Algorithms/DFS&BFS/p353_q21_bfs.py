from math import pow
from collections import deque
def bfs(row,col):
    unions[bfs_count].append((row,col))
    visited[row][col]=True
    q=deque()
    q.append((row,col))
    sumOfCitizens=graph[row][col]
    count=1
    while q:
        row,col=q.popleft()
        
        for dir in range(4):
            new_row=row+dy[dir]
            new_col=col+dx[dir]

            if new_row < 0 or new_row >=n or new_col <0 or new_col>=n:
                continue

            if visited[new_row][new_col]:
                continue

            if L<=abs(graph[new_row][new_col]-graph[row][col])<=R:
                unions[bfs_count].append((new_row,new_col))
                q.append((new_row,new_col))
                sumOfCitizens+=graph[new_row][new_col]
                count+=1
                visited[new_row][new_col]=True
                
    for row,col in unions[bfs_count]:
        graph[row][col]= sumOfCitizens//count

if __name__ == "__main__":
    n,L,R=0,0,0
    graph=[]
    with open("input21.txt","r") as file:
      n,L,R=map(int,file.readline().split())
      for _ in range(n):
        graph.append(list(map(int,file.readline().split())))

    answer=0  
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
  
    while True:
        bfs_count=0
        unions=[]
        visited=[[False]*n for _ in range(n)]
        for i in range(n):
          print(graph[i])  
        for row in range(n):
            for col in range(n):
                if visited[row][col]:
                    continue
                unions.append([(row,col)])
                visited[row][col]=True
                bfs(row,col)
                bfs_count+=1

        if len(unions) == int(pow(n,2)):
            break
        answer+=1
print(answer)
