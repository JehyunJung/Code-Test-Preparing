from collections import deque
from collections import deque
def print_board():
    for row in range(n_rows):
        print(graph[row])
    print()

def components():
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    count=0
    visited=[[False] *n_cols for _ in range(n_rows)]
    
    for row in range(n_rows):
        for col in range(n_cols):
            if graph[row][col] != 0 and not visited[row][col]:
                queue=deque([(row,col)])
                while queue:
                    cur_row,cur_col=queue.popleft()

                    if visited[cur_row][cur_col]:
                        continue
                    
                    visited[cur_row][cur_col]=True
                
                    for dir in range(4):
                        new_row=cur_row+dy[dir]
                        new_col=cur_col+dx[dir]

                        if graph[new_row][new_col] !=0:
                            queue.append((new_row,new_col))
                count+=1

    return count

def solution():
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    time=0
    while True:
        candidates=[]
        for row in range(n_rows):
            for col in range(n_cols):
                if graph[row][col] != 0:
                    count=0
                    for dir in range(4):
                        new_row=row+dy[dir]
                        new_col=col+dx[dir]
                        
                        if graph[new_row][new_col]==0:
                            count+=1
                    candidates.append((row,col,count))
        
        #더 이상 빙산이 안 남아있는 경우
        if len(candidates) == 0:
            return 0

        #빙산에 대해서 녹이는 작업을 수행한다.
        for row,col,count in candidates:
            graph[row][col]-=min(count,graph[row][col])
        time+=1
        
        count=components()
        if count>=2:
            return time
    
if __name__ == "__main__":
    n_rows,n_cols=0,0
    graph=[]
    

    with open("input2573.txt","r") as file:
        n_rows,n_cols=map(int,file.readline().split())
        graph=[list(map(int,file.readline().split())) for _ in range(n_rows)]
    

    print(solution())