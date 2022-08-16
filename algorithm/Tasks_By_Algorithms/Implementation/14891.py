from collections import deque
def clockwise(wheel):
    end=wheel.pop()
    wheel.appendleft(end)

def counter_clockwise(wheel):
    end=wheel.popleft()
    wheel.append(end)

def solution():
    for wheel_num,direction in rotations:
        wheel_num-=1

        rotated_wheels=[]

        rotated_wheels.append((wheel_num,direction))

        right_wheel=wheel_num
        right_direction=direction

        #왼쪽 비교
        for left_wheel in range(right_wheel-1,-1,-1):
            #극이 같은 경우 회전을 수행하지 않는다.
            if wheels[right_wheel][6] == wheels[left_wheel][2]:
                break
            #극이 다른 경우
            else:
                right_wheel=left_wheel
                right_direction*=-1
                rotated_wheels.append((right_wheel,right_direction))
        
        left_wheel=wheel_num
        left_direction=direction

        #오른쪽 비교
        for right_wheel in range(left_wheel+1,4):
             #극이 같은 경우 회전을 수행하지 않는다.
            if wheels[left_wheel][2] == wheels[right_wheel][6]:
                break
            #극이 다른 경우
            else:
                left_wheel=right_wheel
                left_direction*=-1
                rotated_wheels.append((left_wheel,left_direction))

        #마지막에 회전이 되는 톱니바퀴들을 회전시킨다.
        for wheel_num, direction in rotated_wheels:
            if direction == -1:
                counter_clockwise(wheels[wheel_num])
            else:
                clockwise(wheels[wheel_num])

    count=0
    for i in range(4):
        if wheels[i][0]==1:
            count += (2**i)

    return count

if __name__ == "__main__":

    wheels=[]
    num=0
    rotations=[]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input14891.txt","r") as file:
        wheels=[deque(list(map(int,file.readline().strip()))) for _ in range(4)]
        num=int(file.readline())

        rotations=[list(map(int,file.readline().split())) for _ in range(num)]
    
    print(solution())
