
from math import inf

min_result=inf

def propose_ladder_game():
    for i in range(1,N+1):
        row,col=1,i

        while row <= H:
            #왼쪽으로 가로선이 있는 경우
            if graph[row][col-1]==True:
                col=col-1
            #오른쪽으로 가로선이 있는 경우
            elif graph[row][col]==True:
                col=col+1

            row=row+1
        if col !=i:
            return False

    return True

def print_graph():
    for i in range(1,H+1):
        print(graph[i])

def dfs(count,last_row,added_lines):
    global min_result

    if count == added_lines:
        if propose_ladder_game():
            min_result=count
            return
    
    for row in range(last_row,H+1):
        for col in range(1,N):
            if graph[row][col-1] == False and graph[row][col] == False and graph[row][col+1] == False:
                graph[row][col] = True
                dfs(count+1,row,added_lines+1)
                graph[row][col] = False


def solution():

    for i in range(4):
        dfs(0,1,i)
        if min_result != inf:
            break

    if min_result == inf:
        return -1
    
    return min_result



if __name__ == "__main__":
    N,M,H=0,0,0
    graph=[]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\recursion\\input15684.txt","r") as file:
        N,M,H=map(int,file.readline().split())
        graph=[[False] *(N+1) for _ in range(H+1)]
        for _ in range(M):
            a,b=map(int,file.readline().split())
            graph[a][b]=True
    
    print(solution())
