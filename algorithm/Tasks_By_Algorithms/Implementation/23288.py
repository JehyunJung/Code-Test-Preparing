from collections import deque
def bfs(start_row,start_col,number):
    queue=deque([(start_row,start_col)])
    visited=[[False] * M for _ in range(N)]    
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

            if next_row< 0 or next_row >=N or next_col <0 or next_col >=M:
                continue
            if graph[next_row][next_col] != number:
                continue
            queue.append((next_row,next_col))

    return count
def move(rows,cols,dir):
    #북
    if dir==0:
        rows.append(rows.pop(0))
        cols[1]=rows[1]
    #동
    elif dir==1:
        cols.insert(0,rows.pop())
        rows.append(cols.pop())
        rows[1]=cols[1]
    #남
    elif dir==2:
        rows.insert(0,rows.pop())
        cols[1]=rows[1]
    #서
    elif dir==3:
        cols.append(rows.pop())
        rows.append(cols.pop(0))
        rows[1]=cols[1]
    

def solution():
    dir=1
    rows=[2,1,5,6]
    cols=[4,1,3]
    result=0
    row,col=0,0

    inverse_dir=[2,3,0,1]
    for _ in range(K):
        next_row=row+dy[dir]
        next_col=col+dx[dir]

        #칸이 없는 경우 이동방향을 반대로 해서 다시 이동한다.
        if next_row < 0 or next_row >=N or next_col < 0 or next_col >=M:
            dir=inverse_dir[dir]
            next_row=row+dy[dir]
            next_col=col+dx[dir]

        move(rows,cols,dir)
        bottom_number=rows[3]
        graph_number=graph[next_row][next_col]
        result+=(graph_number*bfs(next_row,next_col,graph_number))
        row,col=next_row,next_col

        if bottom_number > graph_number:
            dir=(dir+1)%4
        elif bottom_number < graph_number:
            if dir==0:
                dir=4
            dir-=1
        else:
            continue
    
    return result



if __name__ == "__main__":
    N,M,K=0,0,0
    graph=[]
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input23288.txt","r") as file:
        N,M,K=map(int,file.readline().split())
        graph=[list(map(int,file.readline().split())) for _ in range(N)]
    
    print(solution())