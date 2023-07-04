import sys

def init(index,start,end):

    if start == end:
        tree[index]=datas[start-1]
        return tree[index]
    mid=(start+end)//2

    tree[index]=(init(index*2,start,mid) * init(index*2+1,mid+1,end))%(1000000007)
    return tree[index]


def query(index,start,end,left,right):
    if right < start or end < left:
        return 1
    
    if left <= start and end <=right:
        return tree[index]

    mid=(start+end)//2

    return query(index*2,start,mid,left,right) * query(index*2+1,mid+1,end,left,right)


def update(index,start,end,change_index,old_value,new_value):
    #범위에 포함되지 않는 경우
    if change_index < start or end < change_index:
        return tree[index]
    
    #리프 노드인 경우
    if start == end:
        tree[index]=new_value
        return new_value
    

    mid=(start+end)//2

    tree[index]=update(index*2,start,mid,change_index,old_value,new_value)*update(index*2+1,mid+1,end,change_index,old_value,new_value)

    return tree[index]


    
if __name__ == "__main__":
    n,m,k=map(int,input().split())

    datas=[int(input()) for _ in range(n)]
    
    queries=[map(int,input().split()) for _ in range(m+k)]

    tree=[0] * (4*n)
    init(1,1,n)
    for option, a, b in queries:
        #수 바꾸기
        if option == 1:
            update(1,1,n,a,datas[a-1],b)
            datas[a-1]=b
            
        #쿼리
        if option == 2:
            print(query(1,1,n,a,b)%(1000000007))
