from collections import deque
def bfs(graph,visited,start_row,start_col):

    queue=deque([(start_row,start_col)])
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    count=0
    while queue:
        row,col=queue.popleft()

        if visited[row][col]:
            continue
        visited[row][col]=True
        count+=1
        for dir in range(4):
            next_row=row+dy[dir]
            next_col=col+dx[dir]

            if next_row <0 or next_row>=n_rows or next_col < 0 or next_col>= n_cols:
                continue
            if graph[next_row][next_col]!=0:
                continue
            queue.append((next_row,next_col))
    
    return count

        
            

def solution():
    graph=[[0] * (n_cols+1) for _ in range(n_rows+1)]
    
    #경계값 표현

    for start_col,start_row,end_col,end_row in rectangles:
        graph[n_rows-end_row][start_col]+=1
        graph[n_rows-end_row][end_col]-=1
        graph[n_rows-start_row][start_col]-=1
        graph[n_rows-start_row][end_col]+=1
    
    #열 누적합
    for row in range(n_rows+1):
        for col in range(1,n_cols+1):
            graph[row][col]+=graph[row][col-1]
    #행 누적합
    for col in range(n_cols+1):
        for row in range(1,n_rows+1):
            graph[row][col]+=graph[row-1][col]
    
    visited=[[False]*n_cols for _ in range(n_rows)]
    areas=[]

    for row in range(n_rows):
        for col in range(n_cols):
            if graph[row][col]==0 and not visited[row][col]:
                areas.append(bfs(graph,visited,row,col))

    areas.sort()
    
    print(len(areas))
    print(*areas)




if __name__ == "__main__":
    n_rows,n_cols,n_rectangles=0,0,0
    rectangles=[]

    with open("input2583.txt","r") as file:
        n_rows,n_cols,n_rectangles=map(int,file.readline().split())
        rectangles=[list(map(int,file.readline().split())) for _ in range(n_rectangles)]
    
    solution()
