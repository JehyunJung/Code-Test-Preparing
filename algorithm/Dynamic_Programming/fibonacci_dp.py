import sys

def fibo(x):
  data=[0]*(x+1)
  if x < 2:
    return 1
  else:
    data[0]=1
    data[1]=1
    for i in range(2,x+1):
      data[i]=data[i-1]+data[i-2]
  return data[x]

n=int(sys.argv[1])
print(fibo(n))