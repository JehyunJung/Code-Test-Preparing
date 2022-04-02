from collections import deque
def solution():
    global count,answer
    queue=deque()
    queue.append(A)
  
    check[A][0]=0
    check[A][1]=1
  
    while queue:
        temp=queue.popleft()

        for move in [temp-1,temp+1,temp*2]:
            if 0 <= move <= 100000:
              if check[move][0]==-1:
                check[move][0]=check[temp][0]+1
                check[move][1]=check[temp][1]
                queue.append(move)
              elif check[move][0]==check[temp][0]+1:
                check[move][1]+=check[temp][1]


  
if __name__ == "__main__":
    A,B=0,0
    with open("input12851.txt","r") as file:
      A,B=map(int,file.readline().split())
    check=[[-1,0] for _ in range(100001)]
    solution()
    print(check[B][0])
    print(check[B][1])