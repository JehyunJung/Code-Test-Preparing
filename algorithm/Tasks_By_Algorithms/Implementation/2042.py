from collections import defaultdict
from bisect import bisect_right

def init(index,start,end):
    global tree
    #리프 노드에 다달한 경우
    if start==end:
        tree[index]=numbers[start-1]
        return tree[index]
    
    mid=(start+end)//2

    tree[index]=init(index*2,start,mid)+init(index*2+1,mid+1,end)
    return tree[index]

def sum_of_interval(index,start,end,left,right):
    #범위를 벗어나는 경우
    if right < start or end < left:
        return 0
    #범위 안에 있는 경우
    if left<=start and end <=right:
        return tree[index]
    #범위가 걸쳐있는 경우
    mid=(start+end)//2
    return sum_of_interval(index*2,start,mid,left,right)+sum_of_interval(index*2+1,mid+1,end,left,right)

def update_value(index,start,end,change_index,diff):
    #범위 밖에 있는 경우
    if change_index < start or end < change_index:
        return
    tree[index]+=diff
    
    #리프 노드에 도달한 경우
    if start==end:
        return

    mid=(start+end)//2

    update_value(index*2,start,mid,change_index,diff)
    update_value(index*2+1,mid+1,end,change_index,diff)
    

def solution():
    init(1,1,n)
   
    for a,b,c in commands:
        #수를 바꾸는 옵션
        if a==1:
            diff=(c-numbers[b-1])
            numbers[b-1]=c
            update_value(1,1,n,b,diff)
                 
        #구간합을 구하는 옵션
        else:
            print(sum_of_interval(1,1,n,b,c))


if __name__ == "__main__":
    with open("input2042.txt","r") as file:
        n,m,k=map(int,file.readline().split())
        numbers=[int(file.readline()) for _ in range(n)]
        commands=[list(map(int,file.readline().split())) for _ in range(m+k)]
    tree=[0]*(4*n)
    solution()