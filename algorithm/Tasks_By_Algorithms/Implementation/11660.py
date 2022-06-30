def solution():
    accum_matrix=[[0]*(num+1) for _ in range(num+1)]

    for i in range(1,num+1):
        for j in range(1,num+1):
            accum_matrix[i][j]= matrix[i-1][j-1]+accum_matrix[i-1][j]+accum_matrix[i][j-1]-accum_matrix[i-1][j-1]


    for start_row,start_col, end_row, end_col in queries:
        print(accum_matrix[end_row][end_col]-accum_matrix[end_row][start_col-1]-accum_matrix[start_row-1][end_col]+accum_matrix[start_row-1][start_col-1])



if __name__ == "__main__":
    num,n_queries=0,0
    matrices=[]
    queries=[]

    with open("input11660.txt","r") as file:
        num,n_queries=map(int,file.readline().split())
        matrix=[list(map(int,file.readline().split())) for _ in range(num)]

        queries=[list(map(int,file.readline().split())) for _ in range(n_queries)]
    solution()


