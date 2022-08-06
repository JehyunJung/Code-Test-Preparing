from itertools import combinations
from math import inf,sqrt
def solution():
    result=inf
    lines=list(combinations(range(num),num//2))
    half_length=len(lines)//2
    for indexes in lines[:half_length]:
        x1,y1=0,0
        for index in indexes:
            x1+=points[index][0]
            y1+=points[index][1]
        
        x2=total_x-x1
        y2=total_y-y1
        result=min(result,sqrt((x1-x2)**2 + (y1-y2)**2))
    print('{:.12f}'.format(result))

if __name__ == "__main__":
    num=0
    points=[]
    total_x=0
    total_y=0
    with open("input1007.txt","r") as file:
        num=int(file.readline())
        for _ in range(num):
            x,y=map(int,file.readline().split())
            total_x+=x
            total_y+=y
            points.append((x,y))
    solution()