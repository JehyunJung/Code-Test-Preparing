homes,routers=0,0
coordinates=[]

with open("input29.txt","r") as file:
  homes,routers=map(int,file.readline().split())
  for _ in range(homes):
    coordinates.append(int(file.readline()))

coordinates.sort()

start=1
end=coordinates[homes-1]-coordinates[0]
result=0

while start<=end:
  mid=(start+end)//2

  count=1
  router=coordinates[0]

  for i in range(1,homes):
    if coordinates[i]-router >=mid:
      count+=1
      router=coordinates[i]

  if count>=routers:
    start=mid+1
    result=mid
  else:
    end=mid-1

print(result)




