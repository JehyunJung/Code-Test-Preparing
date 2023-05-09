import sys

def solution(index,current_row,current_col,probability):
    global total_probability
    #모든 이동을 수행한 이후
    if index == n:
        total_probability+=probability
        return
    
    for dir in range(4):
        dir_probability=probabilities[dir]
        #해당 방향으로 갈 수 있는 확률이 없는 경우
        if dir_probability ==0:
            continue

        next_row=current_row+dy[dir]
        next_col=current_col+dx[dir]
        #이미 이전에 방문한 경우
        if visited[next_row][next_col]:
            continue

        visited[next_row][next_col]=True
        solution(index+1,next_row,next_col,probability*dir_probability)
        visited[next_row][next_col]=False


if __name__ == "__main__":
    sys.stdin=open("input1405.txt","r")
    probabilities=list(map(int,input().split()))
    n=probabilities[0]
    probabilities=[probability/100.0 for probability in probabilities[1:]]
    
    visited=[[False] * (2*n+1) for _ in range(2*n+1)]
    total_probability=0

    dy=[0,0,1,-1]
    dx=[-1,1,0,0]

    visited[n][n]=True
    solution(0,n,n,1)
    print(total_probability)