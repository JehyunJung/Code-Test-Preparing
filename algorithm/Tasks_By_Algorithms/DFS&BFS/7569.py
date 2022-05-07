from collections import deque
def solution():
    queue=deque()
    max_day=-1

    dz=[-1,1,0,0,0,0]
    dy=[0,0,-1,0,1,0]
    dx=[0,0,0,1,0,-1]
    for box in range(n_boxes):
        for row in range(n_rows):
            for col in range(n_cols):
                if graph[box][row][col]==1:
                    queue.append((box,row,col))

    while queue:
        box,row,col=queue.popleft()

        for dir in range(6):
            new_box=box+dz[dir]
            new_row=row+dy[dir]
            new_col=col+dx[dir]

            if new_box<0 or new_box >=n_boxes or new_row <0 or new_row >=n_rows or new_col <0 or new_col>=n_cols:
                continue
            if graph[new_box][new_row][new_col]==0:
                graph[new_box][new_row][new_col]=graph[box][row][col]+1
                queue.append((new_box,new_row,new_col))

    for box in range(n_boxes):
        for row in range(n_rows):
            for col in range(n_cols):
                if graph[box][row][col]==0:
                    max_day=-1
                    return max_day
            max_day=max(max(graph[box][row]),max_day)

    return max_day-1
    

if __name__ == "__main__":
    n_cols,n_rows,n_boxes=0,0,0

    with open("input7569.txt","r") as file:
        n_cols,n_rows,n_boxes=map(int,file.readline().split())
        graph=[[list(map(int,file.readline().split())) for _ in range(n_rows)] for _ in range(n_boxes)]

    print(solution())
    