def if_possible_count_score(shape,row,col):
    count=0
    for dy,dx in shape:
        next_row=row+dy
        next_col=col+dx

        #경계를 넘어서는 경우
        if next_row < 0 or next_row >=n_rows or next_col < 0 or next_col >= n_cols:
            return False
        
        count+=graph[next_row][next_col]
    return count



def solution():
    shapes_group=[[] for _ in range(5)]
    shapes_group[0]=[[(0,0),(0,1),(0,2),(0,3)],[(0,0),(1,0),(2,0),(3,0)]] # 1번 모양
    shapes_group[1]=[[(0,0),(0,1),(1,0),(1,1)]] #2번 모양
    shapes_group[2]=[[(0,0),(1,0),(2,0),(2,1)],[(0,0),(0,1),(0,2),(1,0)],[(0,1),(1,1),(2,0),(2,1)],[(0,0),(1,0),(1,1),(1,2)],[(0,2),(1,0),(1,1),(1,2)],[(0,0),(0,1),(1,1),(2,1)],[(0,0),(0,1),(0,2),(1,2)],[(0,0),(0,1),(1,0),(2,0)]] # 3번 모양
    shapes_group[3]=[[(0,0),(1,0),(1,1),(2,1)],[(0,1),(0,2),(1,0),(1,1)],[(0,0),(0,1),(1,1),(1,2)],[(0,1),(1,0),(1,1),(2,0)]] # 4번 모양
    shapes_group[4]=[[(0,0),(0,1),(0,2),(1,1)],[(0,1),(1,0),(1,1),(2,1)],[(0,1),(1,0),(1,1),(1,2)],[(0,0),(1,0),(1,1),(2,0)]]# 5번 모양

    max_count=0
    for start_row in range(n_rows):
        for start_col in range(n_cols):
            for shapes in shapes_group:
                for shape in shapes:
                    result=if_possible_count_score(shape,start_row,start_col)
                    if result == False:
                        continue
                    else:
                        max_count=max(max_count,result) 
    return max_count


if __name__ == "__main__":

    n_rows,n_cols=0,0
    graph=[]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input14500.txt","r" ) as file:
        n_rows,n_cols=map(int,file.readline().split())
        graph=[list(map(int,file.readline().split())) for _ in range(n_rows)]

    solution()