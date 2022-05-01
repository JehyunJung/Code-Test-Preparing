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
    parents=[i for i in range(n+1)]
    edges.sort(key=lambda x:x[2])
    edge_num=0
    MST_value=0
    while edge_num < n-1:
        v1,v2,weight=edges.pop(0)
  
        if find_parent(parents,v1) != find_parent(parents,v2):
            union_parents(parents,v1,v2)
            edge_num+=1
            MST_value+=weight
        else:
            continue

    return MST_value
if __name__ == "__main__":
    n,e=0,0
    edges=[]
    with open("input1922.txt","r") as file:
        n=int(file.readline())
        e=int(file.readline())
        edges=[list(map(int,file.readline().split())) for _ in range(e)]

    print(solution())