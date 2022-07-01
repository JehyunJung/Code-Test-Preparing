from itertools import accumulate
from collections import defaultdict

def solution():
    balls.sort(key=lambda x:x[2])

    index_counts=[0 for i in range(num)]

    print(color_accums)
    j=0
    total=0
    for i in range(num):
        index=balls[i][0]
        color=balls[i][1]
        size=balls[i][2]
        while balls[j][2] < size:
            total+=balls[j][2]
            color_accums[balls[j][1]]+=balls[j][2]
            j+=1
        index_counts[index]=total-color_accums[color]

    for i in range(num):
        print(index_counts[i])

if __name__ == "__main__":
    num=0
    balls=[]
    sizes=[]
    color_accums=defaultdict(int)
    with open("input10800.txt","r") as file:
        num=int(file.readline())
        for i in range(num):
            color,size=map(int,file.readline().split())
            balls.append((i,color,size))
            sizes.append(size)

    solution()

