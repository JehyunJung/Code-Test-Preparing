from collections import deque
#모든 빈칸에 폭탄을 설치하는 함수
def set_bomb():
    global board
    board=[["O"] * n_cols for _ in range(n_rows)]
    

#폭발할 폭탄 찾기
def find_bomb():
    return deque([(row,col) for row in range(n_rows) for col in range(n_cols) if board[row][col]=="O"])

#폭탄을 처리하는 함수    
def clear_bomb(queue):
    global board
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    while queue:
        row,col=queue.popleft()
        board[row][col]="."

        for dir in range(4):
            next_row=row+dy[dir]
            next_col=col+dx[dir]

            if next_row < 0 or next_row >=n_rows or next_col<0 or next_col>=n_cols:
                continue
            
            board[next_row][next_col]="."

def solution():
    queue=find_bomb()

    for time in range(2,n+1):
        if time % 2==0:
            set_bomb()
        else:
            clear_bomb(queue)
            queue=find_bomb()

    for row in board:
        print("".join(row))
        


if __name__ == "__main__":
    with open("input16918.txt","r") as file:
        n_rows,n_cols,n=map(int,file.readline().split())
        board=[list(file.readline().strip()) for _ in range(n_rows)]
    solution()