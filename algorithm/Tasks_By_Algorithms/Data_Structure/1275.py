def init(tree,index,start,end):
    if start == end:
        tree[index]=numbers[start-1]
        return tree[index]

    mid=(start+end)//2

    left=init(tree,index*2,start,mid)
    right=init(tree,index*2+1,mid+1,end)

    tree[index]=left+right
    return tree[index]

def query(tree,index,start,end,left,right):
    if end < left or start > right:
        return 0
    if left <= start and end <=right:
        return tree[index]
    
    if start ==end:
        return tree[index]
    
    mid=(start+end)//2
    left=query(tree,index*2,start,mid,left,right)
    right=query(tree,index*2+1,mid+1,right,left,right)

    return left+right

def update(tree,index,start,end,changing_index,difference):
    if changing_index < start or changing_index > end:
        return
    tree[index] += difference

    if start == end:
        return
    mid=(start+end)//2
 
    update(tree,index*2,start,mid,changing_index,difference)
    update(tree,index*2+1,mid+1,end,changing_index,difference)

    
def solution():
    init(tree,1,1,n)

    for start,end,changing_index,changing_value in queries:
        start,end=(start,end) if start < end else (end,start)
        print(query(tree,1,1,n,start,end))
        update(tree,1,1,n,changing_index,changing_value-numbers[changing_index-1])
        numbers[changing_index-1]=changing_value


if __name__ == "__main__":
    with open("input1275.txt","r") as file:
        n,turns=map(int,file.readline().split())
        numbers=list(map(int,file.readline().split()))
        queries=[list(map(int,file.readline().split())) for _ in range(turns)]
    tree=[0]*(n*4)
    solution()