def query(trees,index,start,end,left,right):
    if right < start or end < left:
        return 0
    
    if left <= start and end <=right:
        return trees[index]
    
    mid=(start+end)//2
    return query(trees,index*2,start,mid,left,right) + query(trees,index*2+1,mid+1,end,left,right)


def update(trees,index,start,end,changed_index):
    if changed_index < start or end < changed_index:
         return
    
    trees[index]+=1

    if start==end:
        return
    
    mid=(start+end)//2
    update(trees,index*2,start,mid,changed_index)
    update(trees,index*2+1,mid+1,end,changed_index)

def solution():
    segment_tree=[0]*(4*n)

    numbers.sort()

    rankings=[0]*n

    for number,index in numbers: 
        count=query(segment_tree,1,1,n,1,index-1)
        rankings[index-1]=(index-count)
        
        update(segment_tree,1,1,n,index)
    
    for ranking in rankings:
        print(ranking)
        
if __name__ == "__main__":
    with open("input2517.txt","r") as file:
        n=int(file.readline())
        numbers=[(int(file.readline()),i+1) for i in range(n)]
    solution()