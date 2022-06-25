from collections import deque
def move(row,col,dy,dx):
    cnt=0
    while graph[row+dy][col+dx] != "#" and graph[row][col] != "O":
        row+=dy
        col+=dx
        cnt+=1
    return row,col,cnt

def solution():
    ry,rx,by,bx=0,0,0,0
    visited=[[[[False]*width for _ in range(height)]for _ in range(width)]for _ in range(height)]
    
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    queue=deque()

    for i in range(height):
        for j in range(width):
            if graph[i][j]=="B":
                by,bx=i,j
            if graph[i][j]=="R":
                ry,rx=i,j
    queue.append((ry,rx,by,bx,1))
    visited[ry][rx][by][bx]=True

    while queue:
        ry,rx,by,bx,depth=queue.popleft()
        print(ry,rx,by,bx)
        if depth >10:
            continue

        for dir in range(4):
            new_ry,new_rx,r_cnt=move(ry,rx,dy[dir],dx[dir])
            new_by,new_bx,b_cnt=move(by,bx,dy[dir],dx[dir])
            print("new: ",new_ry,new_rx,new_by,new_bx)
            if graph[new_by][new_bx]!="O":
                if graph[new_ry][new_rx]=="O":
                    print(depth)
                    return
                if new_ry==new_by and new_rx==new_bx:
                    if r_cnt > b_cnt:
                        new_ry -=dy[dir]
                        new_rx -=dx[dir]
                    else:
                        new_by -=dy[dir]
                        new_bx -=dx[dir]
            
                if not visited[new_ry][new_rx][new_by][new_bx]:
                    visited[new_ry][new_rx][new_by][new_bx]=True
                    queue.append((new_ry,new_rx,new_by,new_bx,depth+1))
    print(-1)

   
if __name__ == "__main__":
    height,width=0,0
    graph=[]
    with open("input13460.txt","r") as file:
        height,width=map(int,file.readline().split())

        graph=[list(file.readline().strip()) for _ in range(height)]
    solution()