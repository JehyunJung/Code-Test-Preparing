from collections import deque

def check_if_zero():
    return belts.count(0) < K

def rotate():
    global is_robots,end_point

    #컨베이어 벨트 이동
    conveyor.rotate(1)

    #마지막 위치에 있는 로봇 내린다.
    end_point=conveyor[N-1]
    is_robots[end_point]=False

def robot_move():
    global belts,is_robots
    for i in range(N-2,-1,-1):
        location=conveyor[i]
        next_location=conveyor[i+1]
        #해당 자리에 로봇이 있고, 다음 자리에 로봇이 없고, 다음 벨트의 내구도가 0이 아니면 이동 가능하다.
        if is_robots[location] and is_robots[next_location]==False and belts[next_location]!=0:
            belts[next_location]-=1 
            is_robots[location],is_robots[next_location]=is_robots[next_location],is_robots[location]    
    
    #마지막 위치에 로봇이 도달한 경우 제거한다.
    is_robots[end_point]=False

def put_robot():
    location=conveyor[0]
    
    if belts[location]!=0:
        is_robots[location]=True
        belts[location]-=1

def solution():
    index=0
    while check_if_zero():
        #회전
        rotate()
        #로봇의 이동
        robot_move()
        #로봇 올리기
        put_robot()
        index+=1
    
    return index


if __name__  == "__main__":
    N,K=0,0
    belts=[]
    is_robots=[]
    end_point=0
    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input20055.txt","r") as file:
        N,K=map(int,file.readline().split())
        belts=list(map(int,file.readline().split()))
        is_robots=[False]*(2*N)

    conveyor=deque(list(range(2*N)))
    print(solution())
