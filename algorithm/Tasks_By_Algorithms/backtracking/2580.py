def check_row(row,data):
    for col in range(9):
        if question_board[row][col]==data:
            return False
    return True

def check_col(col,data):
    for row in range(9):
        if question_board[row][col]==data:
            return False
    return True


def check_square(row,col,data):
    start_row=(row//3)*3
    start_col=(col//3)*3

    for row in range(start_row,start_row+3):
        for col in range(start_col,start_col+3):
            if question_board[row][col]==data:
                return False
    return True


def solution(index):
    if index==len(blanks):
        for row in range(9):
            print(*question_board[row])
        return

    
    for i in range(1,10):
        row=blanks[index][0]
        col=blanks[index][1]

        if check_row(row,i) and check_col(col,i) and check_square(row,col,i):
            question_board[row][col]=i
            solution(index+1)
            question_board[row][col]=0
        

    

if __name__ == "__main__":
    question_board=[]
    blanks=[]
    with open("input2580.txt","r") as file:
        question_board=[list(map(int,file.readline().split())) for _ in range(9)]

    for row in range(9):
        for col in range(9):
            if question_board[row][col]==0:
                blanks.append((row,col))

    solution(0)