from math import inf

def init(tree,index,start,end):
    if start==end:
        tree[index]=[numbers[start],numbers[start]]
        return numbers[start],numbers[start]

    mid=(start+end)//2
    
    left=init(tree,index*2,start,mid)
    right=init(tree,index*2+1,mid+1,end)


    tree[index]=[min(tree[index][0],left[0],right[0]),max(tree[index][1],left[1],right[1])]

    return tree[index]


def query(tree,index,start,end,left,right):
    if right < start or end < left:
        return [inf,-inf]
    
    if left <=start and end <=right:
        return tree[index]
    
    if start==end:
        return tree[index]
    mid=(start+end)//2
    left_child=query(tree,index*2,start,mid,left,right)
    right_child=query(tree,index*2+1,mid+1,end,left,right)

    return [min(left_child[0],right_child[0]),max(left_child[1],right_child[1])]

def solution():
    init(segment_tree,1,0,n-1)

    for index,segment in enumerate(segment_tree):
        if segment != [inf,-inf]:
            print(index, segment)

    for left,right in queries:
        print(query(segment_tree,1,0,n-1,left-1,right-1))

if __name__ == "__main__":
    with open("input2357.txt","r") as file:
        n,m=map(int,file.readline().split())
        numbers=[int(file.readline()) for _ in range(n)]
        queries=[list(map(int,file.readline().split())) for _ in range(m)]
    segment_tree=[[inf,-inf]]*(4*n)
    solution()