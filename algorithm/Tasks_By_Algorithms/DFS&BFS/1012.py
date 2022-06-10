from collections import deque
def bfs(row,col):
    queue=deque([(row,col)])
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    while queue:
        row,col=queue.popleft()
        for dir in range(4):
            new_row=row+dy[dir]
            new_col=col+dx[dir]

            if new_row<0 or new_row >=n or new_col <0 or new_col >=m:
                continue
            if visited[new_row][new_col]:
                continue

            if graph[new_row][new_col]==1:
                queue.append((new_row,new_col))
                visited[new_row][new_col]=True

if __name__ =="__main__":
    num=0
    m,n,k=0,0,0
    graph=[]
    visited=[]

    with open("input1012.txt","r") as file:
        num=int(file.readline())
        for _ in range(num):  
            m,n,k=map(int,file.readline().split())
            graph=[[0]*(m) for _ in range(n)]
            visited=[[False]*(m) for _ in range(n)]
            cabagges=[]
            for _ in range(k):
                col,row=map(int,file.readline().split())
                cabagges.append((row,col))
                graph[row][col]=1
            index=0
            for row,col in cabagges:
                if not visited[row][col]:
                    index+=1
                    visited[row][col]=True
                    bfs(row,col)
            print(index)



            
          
        
    