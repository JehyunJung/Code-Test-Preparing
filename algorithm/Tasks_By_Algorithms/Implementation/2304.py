from collections import deque
def solution():
    pillars.sort(key=lambda x: x[0])
    warehouse=[0]*1001

    max_index=0
    max_height=0

    #최대 지점 찾기
    for index in range(n):
        point,height=pillars[index]
        if height > max_height:
            max_height=height
            max_index=index
    

    warehouse[pillars[max_index][0]]=max_height

    previous_height=0

    #최대값 기준으로 왼쪽 방향
    for index in range(0,max_index):
        point,height=pillars[index]
        if previous_height < height:
            warehouse[point]=height
            previous_height=height

    previous_height=0
    #최대값 기준으로 오른쪽 방향s
    for index in range(n-1,max_index,-1):
        point,height=pillars[index]
        if previous_height < height:
            warehouse[point]=height
            previous_height=height
    
    previous_height=0
    for index in range(pillars[0][0],pillars[max_index][0]):

        if previous_height < warehouse[index]:
            previous_height=warehouse[index]
        else:
            warehouse[index]=previous_height
    
    previous_height=0
    for index in range(pillars[n-1][0],pillars[max_index][0],-1):

        if previous_height < warehouse[index]:
            previous_height=warehouse[index]
        else:
            warehouse[index]=previous_height
    
    print(sum(warehouse))

if __name__ == "__main__":
    with open("input2304.txt","r") as file:
        n=int(file.readline())
        pillars=[list(map(int,file.readline().split())) for _ in range(n)]
    solution()