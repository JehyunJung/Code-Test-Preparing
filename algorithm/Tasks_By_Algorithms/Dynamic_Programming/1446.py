from math import inf
from collections import defaultdict
def solution():
    distances=[inf] * (d+1)
    distances[0]=0

    shortcut_index=defaultdict(list)

    for start,end,distance in shortcuts:
        shortcut_index[start].append((end,distance))
    
    for i in range(d):
        distances[i+1]=min(distances[i+1],distances[i]+1)
        for end,distance in shortcut_index[i]:
            if end > d:
                continue
            distances[end]=min(distances[end],distances[i]+distance)


    print(distances)

if __name__ =="__main__":
    with open("input1446.txt","r") as file:
        n,d=map(int,file.readline().split())
        shortcuts=[list(map(int,file.readline().split())) for _ in range(n)]
    solution()