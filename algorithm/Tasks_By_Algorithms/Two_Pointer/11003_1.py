from collections import deque

def solution():
    queue=deque()

    for i in range(n):
        while queue and queue[-1][0] >= numbers[i]:
            queue.pop()
        while queue and i-queue[0][1] >= l:
            queue.popleft()
        queue.append((numbers[i],i))
        print(queue)
        print(queue[0][0])

if __name__ == "__main__":
    with open("input11003.txt","r") as file:
        n,l=map(int,file.readline().split())
        numbers=list(map(int,file.readline().split()))
    
    solution()