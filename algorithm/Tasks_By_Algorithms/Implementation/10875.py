def solution():
    dy=[1,0,-1,0]
    dx=[0,1,0,-1]

    current_direction=1
    snake=[(0,0)]

    time=0
    previous_turn_time=0
    turn_index=0
    while True:
        time+=1
        row,col=snake[-1]

        #뱀의 이동 진행
        next_row=row+dy[current_direction]
        next_col=col+dx[current_direction]

        if next_row <-n or next_row >n or next_col <-n or next_col >n:
            break

        if (next_row,next_col) in snake:
            break
        
        snake.append((next_row,next_col))
        
        #뱀의 회전 여부 조사
        if turn_index <n_turns and previous_turn_time+int(turns[turn_index][0])==time:
            if turns[turn_index][1]=="L":
                current_direction=(current_direction-1)%4
            else:
                current_direction=(current_direction+1)%4
            previous_turn_time=time
            turn_index+=1
    
    print(time)

if __name__ == "__main__":
    with open("input10875.txt","r") as file:
        n=int(file.readline())
        n_turns=int(file.readline())
        turns=[list(file.readline().split()) for _ in range(n_turns)]
    solution()