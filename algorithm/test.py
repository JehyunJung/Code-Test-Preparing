from math import inf
from copy import deepcopy
def check_if_possible(start_row,start_col,dir):
    locations=[]
    for i in range(1,n+1):
        next_row=start_row+dy[dir]*i
        next_col=start_col+dx[dir]*i
        #전선이 정상적으로 코어에 설치되는 경우 해당 코어에 전선을 부착한다.
        if next_row < 0 or next_row >=n or next_col < 0 or next_col>=n:
            return locations
        #해당 공간이 빈칸이 아니거나 이미 전선이 설치되어 있는 경우 전선을 놓지 않는다.
        if board[next_row][next_col]!=0 or cable_info[next_row][next_col]:
            return None
        locations.append((next_row,next_col))


def solution(index,core_count,cable_length):
    global max_count,min_length
    if index==n_cores:
        if max_count <= core_count:
            max_count=core_count
            min_length=min(min_length,cable_length)

        return
    #각각의 코어에 대해 케이블을 설치 가능한지 판단한다.
    for i in range(index,n_cores):
        row,col=cores[i]
        for dir in range(4):
            result=check_if_possible(row,col,dir)
            if result==None:
                continue
            else:
                for r,c in result:
                    cable_info[r][c]=True
                solution(i+1,core_count+1,cable_length+len(result))
                for r,c in result:
                    cable_info[r][c]=False


if __name__ == "__main__":
    n=0
    board=[]

    with open("input.txt","r") as file:
        n=int(file.readline())
        board=[list(map(int,file.readline().split())) for _ in range(n)]

    cores=[]
    n_cores=0
    for row in range(n):
        for col in range(n):
            if board[row][col]==1:
                #벽에 붙어 있는 core인 경우 이미 전원 공급이 되는 상황임
                if row==0 or row==n-1 or col==0 or col==n-1:
                    continue
                n_cores+=1
                cores.append((row,col))

    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    min_length=inf
    max_count=0
    cable_info=[[False] * n for _ in range(n)]
    solution(0,0,0)

    print(min_length)