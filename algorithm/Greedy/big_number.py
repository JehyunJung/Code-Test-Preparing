n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort()

first=data[-1]
second=data[-2]

count=int(m/(k+1))*k
count+=m%(k+1)

result=first*count
result+=second*(m-count)

print(result)