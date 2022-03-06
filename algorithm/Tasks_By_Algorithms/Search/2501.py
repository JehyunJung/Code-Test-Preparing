def solution(n,k):
  fragments=[]
  
  for i in range(1,n+1):
      if n%i ==0:
          fragments.append(i)
  if len(fragments) < k:
      print(0)
  else:
      print(fragments[k-1])

if __name__ == "__main__":
  n,k=0,0
  with open("input2501.txt","r") as file:
    n,k=map(int,file.readline().split())

  solution(n,k)