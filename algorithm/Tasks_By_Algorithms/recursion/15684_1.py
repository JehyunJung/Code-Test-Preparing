from math import inf

min_result=inf
def propose_ladder_game(lines):
    for i in range(1,N+1):
        row,col=1,i

        while row <= H:
            #왼쪽으로 가로선이 있는 경우
            if (row,col-1) in lines:
                col=col-1
            #오른쪽으로 가로선이 있는 경우
            elif (row,col) in lines:
                col=col+1

            row=row+1
        if col !=i:
            return False

    return True

def dfs(count,index,blank_spots,lines):
    global min_result

    if count >3 or index==len(blank_spots):
        return

    if propose_ladder_game(lines):
        min_result=min(min_result,count)
        return

    #현재 칸에 가로 선을 넣는 경우
    row,col=blank_spots[index]
    if (row,col-1) not in lines and (row,col+1) not in lines:
        dfs(count+1,index+1,blank_spots,lines+[(row,col)])
    #현재 칸에 가로 선을 넣지 않는 경우
    dfs(count,index+1,blank_spots,lines)
    

def solution():
    blank_spots=[]
    lines=[]
    for row in range(1,H+1):
        for col in range(1,N):
            if graph[row][col]:
                lines.append((row,col))
            elif graph[row][col-1] == False and graph[row][col+1] == False:
                blank_spots.append((row,col))
    
    dfs(0,0,blank_spots,lines)

    if min_result > 3:
        return -1
    
    return min_result




if __name__ == "__main__":
    N,M,H=0,0,0
    graph=[]
    lines=[]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\recursion\\input15684.txt","r") as file:
        N,M,H=map(int,file.readline().split())
        graph=[[False] *(N+1) for _ in range(H+1)]
        for _ in range(M):
            a,b=map(int,file.readline().split())
            graph[a][b]=True
            lines.append((a,b))
    
    print(solution())
