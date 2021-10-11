import sys
def tile_construct(n):
  d = [0] * (n + 1)

  if n == 1:
    return 1

  d[:3]=[0,1,3]

  for temp in range(3,n+1):
    d[temp] = d[temp - 1] + 2 * d[temp - 2]
  
  return d[n]


n = int(sys.argv[1])
print(tile_construct(n))
