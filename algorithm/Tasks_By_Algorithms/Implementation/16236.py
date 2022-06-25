from heapq import heappush,heappop
from collections import deque
from turtle import shapesize
def bfs(start_row,start_col,size):
    queue=deque([(start_row,start_col,0)])
    visited=[[False]*n for _ in range(n)]
    visited[start_row][start_col]=True
    heap=[]

    while queue:
        row,col,cost=queue.popleft()
        if graph[row][col] !=0 and graph[row][col] < size:
            heappush(heap,(cost,row,col))

        for dir in range(4):
            new_row=row+dy[dir]
            new_col=col+dx[dir]
            if new_row < 0 or new_row >=n or new_col <0 or new_col>=n:
                continue

            if graph[new_row][new_col] > size:
                continue

            if not visited[new_row][new_col]:
                queue.append((new_row,new_col,cost+1))
                visited[new_row][new_col]=True
    return heap

def solution():
    shark_row,shark_col=0,0
    for row in range(n):
        for col in range(n):
            if graph[row][col]==9:
                shark_row,shark_col=row,col
                graph[row][col]=0
                

    time=0
    shark_size=2
    prey_count=0
    while True:
        print("shark_row,shark_col,size",shark_row,shark_col,shark_size)
        result=bfs(shark_row,shark_col,shark_size)
        
        print("Prey",result)
        if len(result)==0:
            break
        else:
            prey_count+=1
            if prey_count==shark_size:
                shark_size+=1
                prey_count=0
            prey=result[0] #(cost,row,col)

            shark_row=prey[1]
            shark_col=prey[2]

            graph[shark_row][shark_col]=0
            time+=prey[0]

    print(time)
            

if __name__ =="__main__":
    n=0;
    graph=[]
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    with open("input16236.txt","r") as file:
        n=int(file.readline())
        graph=[list(map(int,file.readline().split())) for _ in range(n)]

    solution()