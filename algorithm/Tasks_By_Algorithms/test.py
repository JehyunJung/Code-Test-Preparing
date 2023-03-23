from collections import deque
from math import inf
from os.path import dirname,join
class Node:
    def __init__(self,id,weight):
        self.id=id
        self.weight=weight
        self.left=None
        self.right=None
    
    def __str__(self):
        return "[id: %d, weight: %d]" % (self.id,self.weight)

    def connect(self,left,right):
        self.left=left
        left.right=self
        self.right=right
        right.left=self
        

def print_status(heads,tails):
    for head,tail in zip(heads,tails):
        print(f"head:{head},tail:{tail}")

def find_parent_compressed(parents,x):
    if x!=parents[x]:
        parents[x]=find_parent_compressed(parents,parents[x])
    return parents[x]

def union_parents(parents,x,y):
    pre_x=find_parent_compressed(parents,x)
    pre_y=find_parent_compressed(parents,y)

    parents[pre_x]=pre_y


def solution():
    n,m=queries[0][1],queries[0][2]
    box_indexes=queries[0][3:n+3]
    weights=queries[0][n+3:]
    error_conveyors=set()
    conveyor_indexes=[i for i in range(m)]
    

    #box index에 대한 무게 매핑
    node_maps={}
    unit=n//m
    heads=[]
    tails=[]

    #노드 생성
    for conveyor_index in range(m):
        start,end=unit*conveyor_index,unit*conveyor_index+unit
        for i in range(start,end):
            if weights[i] == 14811316:
                print("key found")
            node_maps[box_indexes[i]]=[conveyor_index,Node(box_indexes[i],weights[i])]

    #노드 연결
    for conveyor_index in range(m):
        start,end=unit*conveyor_index,unit*conveyor_index+unit
        heads.append(node_maps[box_indexes[start]][1])
        for i in range(start+1,end-1):
            node_maps[box_indexes[i]][1].connect(node_maps[box_indexes[i-1]][1],node_maps[box_indexes[i+1]][1])

        tails.append(node_maps[box_indexes[end-1]][1])
    

    for command, option in queries[1:]:

        #물건 하차
        if command == 200:
            weight_sum=0
            for conveyor_index in range(m):
                #컨베이어 벨트가 고장인 경우
                if option != conveyor_index[option]:
                    print(-1)
                    continue
                head=heads[conveyor_index]
                tail=tails[conveyor_index]
                #빈 노드인 경우
                if head == None:
                    continue

                if head.weight <= option:
                    weight_sum+=head.weight
                    #헤드 제거
                    if head.right != None:
                        head.right.left=None
                    del node_maps[head.id]
                    heads[conveyor_index]=head.right
                #맨 앞의 박스를 맨 뒤로 옮긴다. 이때, 박스가 1개 뿐인 경우 작업 수행 X
                elif head!=tail:
                    tail.right=head
                    head.left=tail
                    tails[conveyor_index]=head
                
                    head.right.left=None
                    heads[conveyor_index]=head.right
                    head.right=None
                    
            print(weight_sum)
        #물건 제거
        elif command==300:
            #해당 박스가 없으면 -1 출력
            if option not in node_maps.keys():
                print(-1)
                continue
            conveyor_index,node=node_maps[option]
            conveyor_index=find_parent_compressed(conveyor_indexes,conveyor_index)

            if node.left != None:
                node.left.right=node.right
            if node.right !=None:
                node.right.left=node.left
            
            #헤드 인경우
            if node.left ==None:
                heads[conveyor_index]=node.right
            #테일인 경우
            if node.right==None:
                tails[conveyor_index]=node.left

                
            print(option)
            del node_maps[option]
        #물건 확인
        elif command == 400:
            #해당 박스가 없으면 -1 출력
            if option not in node_maps.keys():
                print(-1)
                continue
            conveyor_index,node=node_maps[option]
            conveyor_index=find_parent_compressed(conveyor_indexes,conveyor_index)
            
            tail=tails[conveyor_index]
            head=heads[conveyor_index]
            #이미 헤드인 경우 작업 생략
            if node != head:
                head.left=tail
                tail.right=head

                node.left.right=None
                tails[conveyor_index]=node.left

                node.left=None
                heads[conveyor_index]=node

            print(conveyor_index+1)
        #벨트 고장
        else:
            option-=1
            #이미 고장 인경우
            if option != conveyor_index[option]:
                print(-1)
                continue
            #정상적인 컨테이너를 찾아서 옮기는 작업 수행
            for i in range(1,m):
                if (option + i)%m in error_conveyors:
                    continue
                
                moved_conveyor_index=(option + i)%m
                #해당 컨테이너에 있던 노드의 컨테이너 인덱스를 변경한다.
                union_parents(conveyor_index,option,moved_conveyor_index)
                head=heads[option]
                tail=tails[option]

                tails[moved_conveyor_index].right=head
                head.left=tail
                
                tails[moved_conveyor_index]=tail

                heads[option]=None
                tails[option]=None
                
                error_conveyors.add(option)
                break
            
            print(option+1)


if __name__ == "__main__":
    scriptpath = dirname(__file__)
    filename = join(scriptpath, 'input.txt')
    
    with open(filename,"r") as file:
        q=int(file.readline())
        queries=[list(map(int,file.readline().split())) for _ in range(q)]

    solution()
  