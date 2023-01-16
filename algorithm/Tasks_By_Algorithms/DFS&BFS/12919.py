from collections import deque
def solution():
    queue=deque([(end)])

    while queue:
        str=queue.popleft()
        print(str)
        if len(str) < len(start):
            continue
        elif len(str)==len(start) and str==start:
            return True
        
        if str[0]=="B":
            queue.append((str[:0:-1]))
        if str[-1]=="A":
            queue.append((str[:-1]))
    
    return False

if __name__ == "__main__":
    with open("input12919.txt","r") as file:
        start=list(file.readline().strip())
        end=list(file.readline().strip())

    print(1 if solution() else 0)