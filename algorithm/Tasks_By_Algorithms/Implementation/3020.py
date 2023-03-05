from math import inf
def solution():
    heights=[0]*(h+1)

    #각각의 높이에 대해 장애물의 시작높이, 끝높이에 해당하는 값에 경계표시
    for index in range(n):
        height=stones[index]
        #석순
        if index % 2==0:
            heights[height]+=1
            heights[0]-=1

        #종유석
        else:
            heights[h]+=1
            heights[h-height]-=1
        

    #각 높이에 대해 장애물이 있는 구간을 찾기 위해 누적합을 수행한다.
    min_height=inf
    count=0
    for index in range(h,0,-1):
        heights[index-1]+=heights[index]

        #최솟값 갱신 및 갯수 카운팅
        if min_height > heights[index]:
            min_height=heights[index]
            count=1
        elif min_height==heights[index]:
            count+=1
    
    print(min_height,count)
    
if __name__ == "__main__":
    with open("input3020.txt","r") as file:
        n,h=map(int,file.readline().split())
        stones=[int(file.readline()) for _ in range(n)]
    solution()