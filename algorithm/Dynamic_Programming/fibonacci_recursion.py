import sys
def fibo(x):
  if x<2:
    return 1
  else:
    return fibo(x-1)+fibo(x-2)

n=int(sys.argv[1])
print(fibo(n))