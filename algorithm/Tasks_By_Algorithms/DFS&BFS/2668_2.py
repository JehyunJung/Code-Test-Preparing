import sys

def dfs(vertex):
    global dfs_stack,components,id,finished
    #각 노드에 고유 id 값을 부여한다.
    discovered[vertex]=id
    id+=1

    stack.append(vertex)
    parent=discovered[vertex]

    for adj_vertex in graph[vertex]:
        #방문 이력이 없는 경우
        if discovered[adj_vertex] == -1:
            parent=min(parent,dfs(adj_vertex))
        #방문하였지만, 아직 처리 중인 경우
        elif not finished[adj_vertex]:
            parent=min(parent,discovered[adj_vertex])
    #부모노드가 자기 자신과 동일한 경우, 자기 자신 노드가 나올때 까지 스택에서 노드를 빼서 scc를 구한다.
    if parent==discovered[vertex]:
        component=[]
        while stack:
            temp=stack.pop()
            component.append(temp)
            #해당 노드에 대한 dfs 작업은 완료된 상태이므로 처리 상태를 완료로 변경한다.
            finished[temp]=True
            if temp == vertex:
                break
        components.append(sorted(component))

    return parent


def solution():
    #dfs 수행
    for vertex in range(n):
        if discovered[vertex]==-1:
            dfs(vertex)
    
    components.sort(key=lambda x : len(x), reverse=True)
    max_component=components[0] + cycles

    print(len(max_component))
    print("\n".join(map(lambda x: str(x+1),max_component)))

if __name__ == "__main__":
    sys.stdin=open("input2668.txt","r")
    n=int(input())
    
    graph=[[] for _ in range(n)]
    cycles=[]
    for src in range(n):
        dest=int(input())-1
        if src == dest:
            cycles.append(src)
        else:
            graph[src].append(dest)

    answer=set()

    id=1
    components=[]
    stack=[]
    discovered=[-1] * (n)
    finished=[False]*(n)

    solution()