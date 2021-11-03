n,m=0,0 
balls=[]
with open("input5.txt","r") as file:
  n,m=map(int,file.readline().split())
  balls=list(map(int,file.readline().split()))

combinations=0
weights=[0]*(m+1)

for i in range(n):
  weights[balls[i]]+=1

sum_balls=sum(weights)

for i in range(n):
  combinations+=(sum_balls-weights[balls[i]])
  weights[balls[i]]-=1
  sum_balls-=1

print(combinations)

