def bingo(board):
    #가로 조시
    for i in range(3):
        if board[i*3] != "." and (board[i*3]==board[i*3+1]==board[i*3+2]):
            return True
    
    #세로 조사
    for i in range(3):
        if board[i] != "." and (board[i]==board[i+3]==board[i+6]):
            return True
    
    #대각선 조사
    if board[0] != "." and (board[0]==board[4]==board[8]):
        return True
    
    if board[2] != "." and (board[2]==board[4]==board[6]):
        return True

    return False

def make_boards(index):
    global boards,board
    #끝까지 다 놓은 경우 최종상태에 포함한다.
    if index==9:
        boards.append("".join(board))
        return
    #이미 빙고가 완성된 경우 최종상태에 포함한다.
    if bingo(board):
        boards.append("".join(board))
        return

    
    for i in range(9):
        #이미 해당 위치에 차 있는 경우 넘어간다.
        if board[i] != ".":
            continue
        board[i]=turns[index%2]
        make_boards(index+1)
        board[i]="."

    
if __name__ == "__main__":
    boards=[]
    board=["."]*9
    turns=["X","O"]
    make_boards(0)
    boards=set(boards)

    with open("input7682.txt","r") as file:
        while True:
            testcase=file.readline().strip()

            #끝인 경우
            if testcase=="end":
                break

            if testcase in boards:
                print("valid")
            else:
                print("invalid")
