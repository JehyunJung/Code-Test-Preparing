def solution(n):
  ugly=[0]*n
  ugly[0]=1

  i2,i3,i5=0,0,0
  next2,next3,next5=2,3,5

  for index in range(1,n):
    ugly[index]=min(next2,next3,next5)

    if ugly[index]==next2:
      i2+=1
      next2=ugly[i2]*2
    if ugly[index]==next3:
      i3+=1
      next3=ugly[i3]*3
    if ugly[index]==next5:
      i5+=1
      next5=ugly[i5]*5

  print(ugly)
  return ugly[n-1]


n=0
m=1000
with open("input35.txt","r") as file:
  n=int(file.readline())

print(solution(n))
