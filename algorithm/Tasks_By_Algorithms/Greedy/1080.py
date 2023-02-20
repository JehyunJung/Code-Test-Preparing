def flip(arr,row,col):
    for next_row in range(row,row+3):
        for next_col in range(col,col+3):
            arr[next_row][next_col]=1-arr[next_row][next_col]

def solution():
    count=0
    
    for i in range(n_rows-2):
        for j in range(n_cols-2):
            if before[i][j]!= after[i][j]:
                flip(before,i,j)
                count+=1
            
            if before==after:
                print(count)
                return
    
    #행 또는 열의 크기가 3미만일 경우에 대한 예외 처리
    print(0 if before==after else -1)

if __name__ == "__main__":
    with open("input1080.txt","r") as file:
        n_rows,n_cols=map(int,file.readline().split())
        before=[list(map(int,file.readline().strip())) for _ in range(n_rows)]
        after=[list(map(int,file.readline().strip())) for _ in range(n_rows)]
    
    solution()