def mining(data,n,m):
  for j in range(1,m):
    left_up,left,left_down=0,0,0
    for i in range(n):
      if i!=0:
        left_up=data[i-1][j-1]
      if i!=n-1:
        left_down=data[i+1][j-1]
      left=data[i][j-1]

      data[i][j]=data[i][j]+max(left_up,left,left_down)
  result=0

  for i in range(n):
    result=max(result,data[i][m-1])
  
  return result

test=0

with open("input31.txt","r") as file:
  test=int(file.readline())
  for _ in range(test):
    n,m=map(int,file.readline().split())
    data_list=[]
    temp=list(map(int,file.readline().split()))

    for i in range(n):
      data_list.append(temp[i*m:(i+1)*m])
    print(mining(data_list,n,m))

  