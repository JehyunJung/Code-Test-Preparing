from collections import deque
from math import inf
def solution():
    visited=[False] * (F+1)
    queue=deque([(S,0)])
    min_count=inf
    while queue:
        floor,count=queue.popleft()

        if floor == G:
            min_count=count
            break
        
        if visited[floor]:
            continue
        visited[floor]=True

        if floor + U <=F:
            queue.append((floor+U,count+1))

        if floor - D > 0:
            queue.append((floor-D,count+1))

    if min_count == inf:
        print("use the stairs")
    else:
        print(min_count)

if __name__ == "__main__":
    F,S,G,U,D=0,0,0,0,0

    with open("input5014.txt","r") as file:
        F,S,G,U,D=map(int,file.readline().split())

    solution()