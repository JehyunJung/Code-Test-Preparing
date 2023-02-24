from collections import deque
def solution():
    length=len(n)
    visited=set()

    candidates=[]

    queue=deque([(n,0)])

    while queue:
        numbers,count=queue.popleft()

        #변경횟수가 m번인 경우
        if count==m:
            candidates.append(numbers)
            continue
        
        for i in range(length-1):
            for j in range(i+1,length):
                temp=numbers[:i]+numbers[j]+numbers[i+1:j]+numbers[i]+numbers[j+1:]
                #앞자리에는 0이 올 수 없다.
                if temp[0]=="0":
                    continue
                #이미 처리된 경우인 경우 
                if (temp,count+1) in visited:
                    continue

                visited.add((temp,count+1))
                queue.append((temp,count+1))

    candidates.sort()

    print(candidates[-1] if candidates else -1)


   
if __name__ == "__main__":
    with open("input1039.txt","r") as file:
        n,m=file.readline().split()
    m=int(m)
    solution()