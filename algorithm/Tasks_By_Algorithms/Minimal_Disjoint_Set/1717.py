def find_parent(parents,x):
    if parents[x]!=x:
        parents[x]=find_parent(parents,parents[x])
    return parents[x]

def union_parents(parents,x,y):
    pre_x=find_parent(parents,x)
    pre_y=find_parent(parents,y)

    if pre_x < pre_y:
        parents[pre_x]=pre_y
    else:
        parents[pre_y]=pre_x
    
def solution():
    parents=[i for i in range(nodes+1)]

    for op,a,b in operations:
        if op==1:
            if find_parent(parents,a) == find_parent(parents,b):
                print("YES")
            else:
                print("NO")
        else:
            union_parents(parents,a,b)
    
if __name__ == "__main__":
    nodes,num=0,0
    operations=[]
    with open("input1717.txt","r") as file:
        nodes,num=map(int,file.readline().split())
        operations=[list(map(int,file.readline().split())) for _ in range(num)]

    solution()