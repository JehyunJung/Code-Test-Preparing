from collections import deque
from math import inf
def string_difference(a,b):
    count=0
    for a_ch,b_ch in zip(a,b):
        if a_ch != b_ch:
            count+=1
    return count

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    queue=deque()
    distance=[inf] * len(words)
    
    for index,word in enumerate(words):
        if string_difference(begin,word) ==1:
            queue.append((word,1))
            distance[index]=1
            
    while queue:
        temp,step=queue.popleft()
        if temp==target:
            answer=step
            break
        
        for index,word in enumerate(words):
            if distance[index] >= step+1:
                if string_difference(temp,word)==1:
                    queue.append((word,step+1))
                    distance[index]=step+1    
        
    return answer
if __name__ == "__main__":
    begin,target="",""
    words=[]
    with open("level3_2.txt","r") as file:
        begin,taget=map(str,file.readline().split())
        words=list(map(str,file.readline().split()))

    print(solution())