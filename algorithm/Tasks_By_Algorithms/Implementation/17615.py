def solution():
    blue_count=balls.count("B")
    red_count=n-blue_count
    
    #한 종류의 공만 존재하는 경우
    if blue_count == n or red_count == n:
        return 0

    #왼쪽 끝에 있는 같은 색깔의 공의 갯수
    left_ball=balls[0]
    left_ball_count=0

    for index in range(n):
        ball=balls[index]
        if ball==left_ball:
            left_ball_count+=1
        else:
            break

    #오른쪽 끝에 있는 같은 색깔의 공의 갯수
    right_ball=balls[-1]
    right_ball_count=0

    for index in range(n-1,-1,-1):
        ball=balls[index]
        if ball==right_ball:
            right_ball_count+=1
        else:
            break

    if left_ball==right_ball:
        if left_ball == "B":
            return min(red_count,blue_count-left_ball_count,blue_count-right_ball_count)
        else:
            return min(blue_count,red_count-left_ball_count,red_count-right_ball_count)
    else:
        if left_ball=="B":
            return min(blue_count-left_ball_count,red_count-right_ball_count)
        else:
            return min(red_count-left_ball_count,blue_count-right_ball_count)
    

if __name__ == "__main__":
    with open("input17615.txt","r") as file:
        n=int(file.readline())
        balls=file.readline()
    print(solution())
