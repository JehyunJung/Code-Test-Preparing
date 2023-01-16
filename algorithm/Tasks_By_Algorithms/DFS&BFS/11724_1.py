def find_parent_compressed(parents,x):
    while x!=parents[x]:
        parents[x]=find_parent_compressed(parents,parents[x])
    return parents[x]

def union_parents(parents,x,y):
    pre_x=find_parent_compressed(parents,x)
    pre_y=find_parent_compressed(parents,y)
    if pre_x < pre_y:
        parents[pre_x]=pre_y
    else:
        parents[pre_y]=pre_x

def solution():
    parents=[i for i in range(n_vertex)]
    for v1,v2 in edges:
        union_parents(parents,v1-1,v2-1)

    for i in range(n_vertex):
        find_parent_compressed(parents,i) 

    print(len(set(parents)))

    

if __name__ == "__main__":
    with open("input11724.txt","r") as file:
        n_vertex,n_edge=map(int,file.readline().split())
        edges=[sorted(list(map(int,file.readline().split()))) for _ in range(n_edge)]

    solution()