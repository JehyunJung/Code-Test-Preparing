def solution():
  bag=[[0]*(max_weight+1) for _ in range(items+1)]

  for item in range(1,items+1):
    for weight in range(1,max_weight+1):
      if weights[item] > weight:
        bag[item][weight]=bag[item-1][weight]
      else:
        bag[item][weight]=max(bag[item-1][weight],bag[item-1][weight-weights[item]]+prices[item])
      
  for i in range(items+1):
    print(bag[i])

if __name__ == "__main__":
  items,max_weight=0,0
  weights=[]
  prices=[]

  with open("inputtest.txt","r") as file:
    items,max_weight=map(int,file.readline().split())
    weights=list(map(int,file.readline().split()))
    prices=list(map(int,file.readline().split()))

  weights.insert(0,0)
  prices.insert(0,0)


  print(solution())