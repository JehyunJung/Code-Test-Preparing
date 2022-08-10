from ast import Continue
from collections import deque
def bfs(visited,start_row,start_col,color,option):

    queue=deque([(start_row,start_col)])
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    while queue:
        row,col=queue.popleft()

        if visited[row][col]:
            continue
        visited[row][col]=True

        for dir in range(4):
            new_row=row+dy[dir]
            new_col=col+dx[dir]

            if new_row <0 or new_row >=num or new_col < 0 or new_col >=num:
                continue
            
            if graph[new_row][new_col]==color:
                queue.append((new_row,new_col))

            #적록색맹인 경우
            if option :
                if (color=="G" and graph[new_row][new_col]=="R") or (color=="R" and graph[new_row][new_col]=="G"):
                    queue.append((new_row,new_col))
   

def solution():
    visited=[[False]*num for _ in range(num)]
    normal_count,abnormal_count=0,0
    for i in range(num):
        for j in range(num):
            if not visited[i][j]:
                bfs(visited,i,j,graph[i][j],False)
                normal_count+=1

    visited=[[False]*num for _ in range(num)]
    for i in range(num):
        for j in range(num):
            if not visited[i][j]:
                bfs(visited,i,j,graph[i][j],True)
                abnormal_count+=1


    print(normal_count,abnormal_count)

if __name__ == "__main__":
    num=0
    graph=[]

    with open("input10026.txt","r") as file:
        num=int(file.readline())
        graph=[list(file.readline()) for _ in range(num)]
    
    solution()