stages=0
players=[]

with open("input25.txt","r") as file:
  stages=int(file.readline())
  players=list(map(int,file.readline().split()))

answer=[]
num_players=len(players)

for i in range(1,stages+1):
  count=players.count(i)
  failure=0

  if num_players!=0:
    failure=count/num_players

  answer.append((failure,i))
  num_players-=count

answer.sort(key=lambda x: (-x[0],x[1]))

answer=[x[1] for x in answer]
print(answer)