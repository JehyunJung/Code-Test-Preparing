from collections import deque
def solution():
    global count,answer
    queue=deque()
    queue.append(A)
  
    check[A]=0
  
    while queue:
        temp=queue.popleft()

        if temp==B:
          break
          
        for move in [temp-1,temp+1,temp*2]:
            if 0 <= move <= 100000:
              if check[move]==-1:
                check[move]=check[temp]+1
                path[move]=temp
                queue.append(move)
                
def print_path(path,point):
  ans=[point]
  while point!=A:
    ans.append(path[point])
    point=path[point]
  ans=ans[::-1]
  print(" ".join(map(str,ans)))
  
if __name__ == "__main__":
    A,B=0,0
    with open("input12851.txt","r") as file:
      A,B=map(int,file.readline().split())
    check=[-1 for _ in range(100001)]
    path=[-1 for _ in range(10001)]
    solution()
    print(check[B])
    print_path(path,B)