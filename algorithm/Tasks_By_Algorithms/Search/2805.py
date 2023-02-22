def solution():
    start,end=0,20000000000
    max_tree_height=0
    while start<end:
        mid=(start+end)//2
        remaining_tree=0
        for tree in trees:
            remaining_tree+=max(tree-mid,0)
        
        if remaining_tree>=m:
            max_tree_height=max(max_tree_height,mid)
            start=mid+1
        else:
            end=mid-1
    
    print(max_tree_height)

if __name__ == "__main__":
    with open("input2805.txt","r") as file:
        n,m=map(int,file.readline().split())
        trees=list(map(int,file.readline().split()))
    solution()