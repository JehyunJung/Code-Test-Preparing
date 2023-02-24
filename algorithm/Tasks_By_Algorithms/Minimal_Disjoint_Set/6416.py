from collections import defaultdict,deque
def isTree(edge_infos):
    #노드가 0개 인경우
    if len(edge_infos)==0:
        return True

    indegree=defaultdict(int)
    vertices=set()
    edges=[]

    #들어오는 간선 확인
    for edge_info in edge_infos:
        v1,v2=map(int,edge_info.split())
        vertices.add(v1)
        vertices.add(v2)
        edges.append((v1,v2))
        indegree[v2]+=1

    zero_indegree_count=0
    root_node=0

    for vertex in vertices:
        if indegree[vertex]==0:
            zero_indegree_count+=1
            root_node=vertex
        #들어오는 간선이 2개 이상인 경우 Tree 성립 안 함
        if indegree[vertex]>1:
            return False
    
    #들어오는 간선이 없는 노드가 여러 개일 수 없다.
    if zero_indegree_count>1:
        return False
    
    #트리 생성
    tree=defaultdict(list)

    for v1,v2 in edges:
        tree[v1].append(v2)

    #bfs을 수행해서 중복된 경로가 있는지 확인
    visited=set()

    queue=deque([(root_node)])
    visited.add(root_node)

    while queue:
        vertex=queue.popleft()

        for adj_vertex in tree[vertex]:
            if adj_vertex in visited:
                return False
            visited.add(adj_vertex)
            queue.append(adj_vertex)
    
    return True

def solution():
    for index,testcase in enumerate(testcases):
        print(f"CASE {index} is a tree." if isTree(testcase) else f"CASE {index} is not a tree.")


if __name__ == "__main__":
    with open("input6416.txt","r") as file:
        testcases=[]
        test_case=[]
        while True:
            temp=file.readline().strip().split("  ")
            #줄 뛰우기 
            if temp[-1]=="":
                continue

            #데이터의 끝을 의미
            if temp[-1][0]=="-" and temp[-1][3]=="-":
                break
            
            
            #각각의 테스트케이스의 끝을 의미
            if temp[-1]=="0 0":
                test_case.extend(temp[:-1])
                testcases.append(test_case)
                test_case=[]
                continue
            
            test_case.extend(temp)

    solution()

        