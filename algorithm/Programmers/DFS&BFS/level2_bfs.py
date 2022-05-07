from collections import deque
def solution(numbers, target):
    answer = 0
    queue=deque()
    queue.append((numbers[0],1))
    queue.append((-numbers[0],1))
    
    while queue:
        sub_sum,idx=queue.popleft()
        if idx==len(numbers):
            if sub_sum==target:
                answer+=1
        else:
            queue.append((sub_sum+numbers[idx],idx+1))
            queue.append((sub_sum-numbers[idx],idx+1))
    
    return answer
if __name__ == "__main__":
    numbers=[]
    target=0
    with open("level2.txt","r") as file:
        numbers=list(map(int,file.readline().split()))
        target=int(file.readline())
    print(solution(numbers,target))