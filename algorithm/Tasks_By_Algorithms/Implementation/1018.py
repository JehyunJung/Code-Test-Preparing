from math import inf
def solution():
    chess_rows=[["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"]]
    min_count= inf
    for row in range(n_rows-7):
        for col in range(n_cols-7):
            count=0
            #B 부터 시작하는 경우
            for dy in range(8):
                for dx in range(8):
                    chess_index=dy%2

                    if board[row+dy][col+dx]!=chess_rows[chess_index][dx]:
                        count+=1
            min_count=min(min_count,count)
            count=0

            #W 부터 시작하는 경우
            for dy in range(8):
                for dx in range(8):
                    chess_index=1-(dy%2)
                    if board[row+dy][col+dx]!=chess_rows[chess_index][dx]:
                        count+=1
            min_count=min(min_count,count)

    return min_count
if __name__== "__main__":
    n_rows,n_cols=0,0
    board=[]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input1018.txt","r") as file:
        n_rows,n_cols=map(int,file.readline().split())
        board=[list(file.readline()) for _ in range(n_rows)]

    print(solution())