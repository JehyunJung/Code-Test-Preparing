def solution():
    movements={
        "R":(0,1),
        "L":(0,-1),
        "B":(-1,0),
        "T":(1,0),
        "RT":(1,1),
        "LT":(1,-1),
        "RB":(-1,1),
        "LB":(-1,-1)
    }

    conversion=[0,"A","B","C","D","E","F","G","H"]
    king_row,king_col=int(king[1]),conversion.index(king[0])
    stone_row,stone_col=int(stone[1]),conversion.index(stone[0])
    for move in moves:
        dy,dx=movements[move]
        king_next_row,king_next_col=king_row+dy,king_col+dx
        #킹의 다음 위치가 격자를 넘어서는 경우
        if king_next_row < 1 or king_next_row >8 or king_next_col < 1 or king_next_col >8:
            continue

        #킹의 다음 위치가 돌의 위치랑 겹치는 경우
        if king_next_row==stone_row and king_next_col==stone_col:
            stone_new_row,stone_new_col=stone_row+dy,stone_col+dx
            #돌의 이동해야하는 데 다음 위치가  격자를 넘어서는 경우
            if stone_new_row < 1 or stone_new_row >8 or stone_new_col < 1 or stone_new_col >8:
                continue

            stone_row,stone_col=stone_new_row,stone_new_col
        
        king_row,king_col=king_next_row,king_next_col

    print(conversion[king_col]+str(king_row))
    print(conversion[stone_col]+str(stone_row))


if __name__ == "__main__":
    king,stone,N=0,0,0
    moves=[]

    with open("input1063.txt","r") as file:
        king,stone,N=file.readline().split()
        N=int(N)
        moves=[file.readline().strip() for _ in range(N)]
    
    solution()
