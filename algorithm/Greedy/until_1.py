n,k =0,0
with open("input.txt","r") as file:
  n,k=map(int,file.readline().split())

result=0
while n>1:
  target=(n//k) * k
  result+=(n-target)
  n=target

  if n < k :
    break
    
  n//=k
  result+=1
  
result += (n-1)

print(result)


