from collections import deque
def solution():
    queue=deque([i for i in range(1,n+1)])
    
    for _ in range(n-1):
        queue.popleft()
        queue.append(queue.popleft())
    
    print(queue[0])

if __name__ == "__main__":
    with open("input2164.txt","r") as file:
        n=int(file.readline())
    
    for n in range(1,101):
        solution()