from math import inf
def find_parent_compressed(parents,x):
    if x != parents[x]:
        parents[x]=find_parent_compressed(parents,parents[x])
    return parents[x]

def union_parents(parents,x,y):
    pre_x=find_parent_compressed(parents,x)
    pre_y=find_parent_compressed(parents,y)

    if pre_y<pre_x:
        parents[pre_y]=pre_x
    else:
        parents[pre_x]=pre_y
    

def solution():
    parents=[i for i in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j]==1:
                if find_parent_compressed(parents,i) != find_parent_compressed(parents,j):
                    union_parents(parents,i,j)
    
    for i in range(n):
        find_parent_compressed(parents,i)
        
    parent=parents[travel_route[0]]

    for i in range(1,m):
        if parents[travel_route[i]] != parent:
            print("NO")
            break
    else:
        print("YES")


if __name__ == "__main__":
    with open("input1976.txt","r") as file:
        n=int(file.readline())
        m=int(file.readline())
        graph=[list(map(int,file.readline().split())) for _ in range(n)]
        travel_route=list(map(lambda x: int(x)-1,file.readline().split()))
    
    solution()