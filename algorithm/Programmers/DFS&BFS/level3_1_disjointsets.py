def find_parent(parents,x):
    if x != parents[x]:
        parents[x]=find_parent(parents,parents[x])
    return parents[x]

def union_parents(parents,x,y):
    pre_x=find_parent(parents,x)
    pre_y=find_parent(parents,y)
    
    if pre_x < pre_y:
        parents[pre_y]=pre_x
        
    else:
        parents[pre_x]=pre_y
        
def solution(n, computers):
    answer = 0
    parents=[i for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
                
            if computers[i][j]==1:
                if find_parent(parents,i) != find_parent(parents,j):
                    union_parents(parents,i,j)
                    
    for i in range(n):
        find_parent(parents,i)
        
    answer=len(set(parents))
            
    return answer

if __name__ == "__main__":
    n=0
    computers=[]
    with open("level3_1.txt","r") as file:
        n=int(file.readline())
        computers=[list(map(int,file.readline().split())) for _ in range(n)]
    print(solution(n,computers))