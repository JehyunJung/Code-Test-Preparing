from math import inf
from bisect import bisect_left
def solution():
    heights=[0]*(h+1)
    tops=[]
    bottoms=[]

    #각각의 높이에 대해 장애물의 시작높이, 끝높이에 해당하는 값에 경계표시
    for index in range(n):
        height=stones[index]
        #석순
        if index % 2==0:
            bottoms.append(height)

        #종유석
        else:
            tops.append(height)
    
    tops.sort()
    bottoms.sort()

    min_obstacles=inf
    count=0

    for height in range(1,h+1):
        top_index=bisect_left(tops,(h+1)-height)
        bottom_index=bisect_left(bottoms,height)

        print(height,top_index,bottom_index)

        obstacle_count=n-top_index-bottom_index

        if obstacle_count < min_obstacles:
            min_obstacles=obstacle_count
            count=1
        elif obstacle_count==min_obstacles:
            count+=1
    
    print(min_obstacles,count)

    
if __name__ == "__main__":
    with open("input3020.txt","r") as file:
        n,h=map(int,file.readline().split())
        stones=[int(file.readline()) for _ in range(n)]
    solution()