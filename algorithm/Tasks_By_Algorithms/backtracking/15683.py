from math import inf
from copy import deepcopy
def check_empty_space(cctvs):
    temp_graph=deepcopy(graph)

    for cctv_row,cctv_col, cctv_directions in cctvs:
        for cctv_direction in cctv_directions:
            for times in range(max(height,width)):
                next_row=cctv_row +dy[cctv_direction]*times
                next_col=cctv_col +dx[cctv_direction]*times

                if next_row < 0 or next_row >= height or next_col < 0 or next_col >=width:
                    break
                if graph[next_row][next_col]==6:
                    break
                
                temp_graph[next_row][next_col]=7

    count=0
    for row in range(height):
        for col in range(width):
            if temp_graph[row][col] == 0:
                count+=1

    return count

    
def dfs(index, cctvs):
    global result
    if index == len(blanks):
        result=min(result,check_empty_space(cctvs))
        return

    row=blanks[index][0]
    col=blanks[index][1]
    cctv_type=blanks[index][2]

    for direction in cctv_types[cctv_type]:
        dfs(index+1,cctvs+[(row,col,direction)])

def solution():
    for row in range(height):
        for col in range(width):
            if graph[row][col] !=6 and graph[row][col] !=0:
                blanks.append((row,col,graph[row][col]))
    dfs(0,[])
    print(result)
    


if __name__ == "__main__":
    height,width=0,0
    graph=[]
    blanks=[]

    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    cctv_types={
        1: [[0],[1],[2],[3]],
        2: [[0,2],[1,3]],
        3: [[0,1],[1,2],[2,3],[3,0]],
        4: [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
        5: [[0,1,2,3]]
    }
    result=inf
    with open("input15683.txt","r") as file:
        height,width=map(int,file.readline().split())
        graph=[list(map(int,file.readline().split())) for _ in range(height)]

    solution()