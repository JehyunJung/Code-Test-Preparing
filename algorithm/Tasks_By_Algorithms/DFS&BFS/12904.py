from collections import deque
def solution():
    global end
    while len(end)!=len(start):
        if end==start:
            return True
        
        if end[-1]=="B":
            end.pop()
            end.reverse()
        elif end[-1]=="A":
            end.pop()
    
    return False

if __name__ == "__main__":
    with open("input12919.txt","r") as file:
        start=deque(file.readline().strip())
        end=deque(file.readline().strip())
    print(1 if solution() else 0)