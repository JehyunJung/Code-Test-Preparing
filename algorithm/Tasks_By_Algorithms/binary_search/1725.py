import sys
#segment tree의 초기화
def init(index,start,end):
    #리프 노드에 다달한 경우
    if start == end:
        tree[index]=start
        return tree[index]
    
    mid=(start+end)//2
    left_min_index=init(index*2,start,mid)
    right_min_index=init(index*2+1,mid+1,end)

    tree[index]= left_min_index if histogram[left_min_index-1] <= histogram[right_min_index-1] else right_min_index

    return tree[index]

#segment tree에 대한 query
def query(index,start,end,left,right):
    if right < start or end < left:
        return -1

    if left <= start and end <=right:
        return tree[index]
    
    mid=(start+end)//2
    
    left_min_index=query(index*2,start,mid,left,right)
    right_min_index=query(index*2+1,mid+1,end,left,right)
    left_min,right_min=inf,inf
    
    if left_min_index != -1:
        left_min=histogram[left_min_index-1]
    if right_min_index != -1:
        right_min=histogram[right_min_index-1]


    return left_min_index if left_min <=right_min else right_min_index

def solution(left,right):
    global max_area
    if left>right:
        return
    
    min_index=query(1,1,n,left,right)
    max_area=max(max_area,histogram[min_index-1] * (right-left+1))

    solution(left,min_index-1)
    solution(min_index+1,right)


if __name__ == "__main__":
    sys.setrecursionlimit(10**5)
    sys.stdin=open("input1725.txt","r")
    n=int(input())
    histogram=[int(input()) for _ in range(n)]

    tree=[0] * (4*n)
    init(1,1,n)

    max_area=0
    solution(1,n)
    print(max_area)