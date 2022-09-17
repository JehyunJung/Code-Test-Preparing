from math import inf
def check_rectangle(size,start_row,start_col):
    for row in range(start_row,start_row+size):
        for col in range(start_col,start_col+size):
            if graph[row][col]==0:
                return False
    return True

def cover_rectangle(size,start_row,start_col):
    global graph
    for row in range(start_row,start_row+size):
        for col in range(start_col,start_col+size):
            graph[row][col]=0

def uncover_rectangle(size,start_row,start_col):
    global graph
    for row in range(start_row,start_row+size):
        for col in range(start_col,start_col+size):
            graph[row][col]=1

def dfs(count,row,col):
    global min_result,rectangles
 
    if row >=10:
        min_result=min(min_result,count)
        return 
    
    if col >=10:
        dfs(count,row+1,0)
        return

    if graph[row][col]==1:
        for size in range(5,0,-1):
            #범위를 벗어나는 경우
            if (row+size) >10 or (col+size)>10:
                continue
            #색종이를 다 쓴 경우
            if rectangles[size-1]==0:
                continue      
                    
            if check_rectangle(size,row,col):
                cover_rectangle(size,row,col)
                rectangles[size-1]-=1
                dfs(count+1,row,col+size)                
                rectangles[size-1]+=1
                uncover_rectangle(size,row,col)
    else:
        dfs(count,row,col+1)



def solution():
    dfs(0,0,0)
    print(min_result)
    return -1 if min_result==inf else min_result


if __name__ =="__main__":
    graph=[]
    rectangles=[5,5,5,5,5]
    min_result=inf
    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input17136.txt","r") as file:
        graph=[list(map(int,file.readline().split())) for _ in range(10)]

    print(solution())