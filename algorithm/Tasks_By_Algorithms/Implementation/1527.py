from collections import deque
def solution():
    count=0
    queue=deque([4,7])
    while queue:
        value=queue.popleft()

        if min_num<=value<=max_num:
            count+=1
        if value> max_num:
            break

        for concat_value in [4,7]:
            queue.append(value*10 + concat_value)
    return count

if __name__ == "__main__":
    min_num,max_num=0,0
    with open("input1527.txt","r") as file:
        min_num,max_num=map(int,file.readline().split())
    print(solution())