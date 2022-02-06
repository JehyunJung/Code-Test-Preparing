def solution():
  max_weight=sum(app_weights)
  bag=[[0]*(max_weight+1) for _ in range(items+1)]

  min_weight=max_weight
  for item in range(1,items+1):
    for weight in range(1,max_weight+1):
      if app_weights[item] > weight:
        bag[item][weight]=bag[item-1][weight]
      else:
        bag[item][weight]=max(bag[item-1][weight],bag[item-1][weight-app_weights[item]]+app_memories[item])
      
      if bag[item][weight]>=required_memories:
        min_weight=min(min_weight,weight)
  for i in range(items+1):
    print(bag[i])
  return min_weight

if __name__ == "__main__":
  items,required_memories=0,0
  app_memories=[]
  app_weights=[]

  with open("input7579.txt","r") as file:
    items,required_memories=map(int,file.readline().split())
    app_memories=list(map(int,file.readline().split()))
    app_weights=list(map(int,file.readline().split()))

  app_memories.insert(0,0)
  app_weights.insert(0,0)


  print(solution())