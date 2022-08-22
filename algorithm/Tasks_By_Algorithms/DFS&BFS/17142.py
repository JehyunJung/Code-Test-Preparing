from collections import deque
from itertools import combinations
from math import inf
import re

def bfs(queue,virus_locations):
    visited=[[False]*n_rows for _ in range(n_rows)]
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    
    while queue:
        row,col,count=queue.popleft()
        
        if visited[row][col]:
            continue
        visited[row][col]=count

        for dir in range(4):
            next_row=row+dy[dir]
            next_col=col+dx[dir]

            if next_row < 0 or next_row >=n_rows or next_col < 0 or next_col>=n_rows:
                continue

            if graph[next_row][next_col] == 1:
                continue
            
            queue.append((next_row,next_col,count+1))

    max_count=0
    
    for row in range(n_rows):
        for col in range(n_rows):
            #벽인 경우 넘어간다
            if graph[row][col]==1:
                continue
            #빈칸이 있는 경우 bfs 수행 불완전 -> inf 반환
            if visited[row][col] == False:
                return inf
            
            #바이러스가 있는 칸에 대해서는 초를 세지 않는다. --> 비활성 바이러스의 경우 고려
            if (row,col) in virus_locations:
                continue

            max_count=max(max_count,visited[row][col])

    return max_count

def print_graph(visited):
    print("visited")
    for row in visited:
        print(row)

def solution():
    virus_locations=[]
    for row in range(n_rows):
        for col in range(n_rows):
            if graph[row][col]==2:
                virus_locations.append((row,col))
                graph[row][col]=0
    min_time=inf

    for combination in combinations(virus_locations,n_viruses):
        queue=deque()
        for row,col in combination:
            graph[row][col]=2
            queue.append((row,col,0))

        time=bfs(queue,virus_locations)
        min_time=min(min_time,time)
        
        for row,col in combination:
            graph[row][col]=0

    if min_time == inf:
        return -1
    return min_time
        



if __name__ == "__main__":
    n_rows,n_viruses=0,0
    graph=[]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\DFS&BFS\\input17142.txt","r") as file:
        n_rows,n_viruses=map(int,file.readline().split())
        graph=[list(map(int,file.readline().split())) for _ in range(n_rows)]
    
    print(solution())