with open("input.txt","r") as file:
  n,m=map(int,file.readline().split())
  result=0

  for i in range(n):
    data=list(map(int,file.readline().split()))
    min_data=min(data)

    result=max(result,min_data)

print(result)