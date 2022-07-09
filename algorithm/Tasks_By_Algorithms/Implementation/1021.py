from collections import deque
def solution():
    global n
    queue=deque()

    for i in range(1,n+1):
        queue.append(i)

    count=0
    for query in queries:
        if query==queue[0]:
            queue.popleft()
        else:
            if queue.index(query) <= len(queue)//2:
                while queue[0] != query:
                    queue.append(queue.popleft())
                    count+=1
                queue.popleft()
            else:
                while queue[0] != query:
                    queue.appendleft(queue.pop())
                    count+=1
                queue.popleft()

    print(count)

if __name__ == "__main__":
    n,m=0,0
    queries=[]

    with open("input1021.txt","r") as file:
        n,m=map(int,file.readline().split())
        queries=list(map(int,file.readline().split()))
    
    solution()