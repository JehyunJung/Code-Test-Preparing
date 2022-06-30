import os
def get_nextdir(dir):
    dir-=1
    if dir == -1:
        return 3
        
    return dir

def solution():
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    visited=[[False]*width for _ in range(height)]

    vacuum_count=1
    row,col,direction=start_row,start_col,start_direction
    visited[row][col]=True

    while True:
        checked=False
        for i in range(4):
            direction=get_nextdir(direction)

            next_row=row+dy[direction]
            next_col=col+dx[direction]

            if visited[next_row][next_col]:
                continue
            if graph[next_row][next_col] == 1:
                continue

            row=next_row
            col=next_col
            
            visited[row][col]=True
            vacuum_count+=1
            checked=True
            break

        if not checked:
            next_row=row-dy[direction]
            next_col=col-dx[direction]
            if graph[next_row][next_col] != 1:
                row=next_row
                col=next_col
                continue
            else:
                break

    print(vacuum_count)



if __name__ == "__main__":
    height,width=0,0
    start_row, start_col,start_direction=0,0,0
    graph=[]

    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, "input14503.txt")
    with open(filename,"r") as file:
        height,width=map(int,file.readline().split())
        start_row,start_col,start_direction=map(int,file.readline().split())

        graph=[list(map(int,file.readline().split())) for _ in range(height)]
    
    solution()