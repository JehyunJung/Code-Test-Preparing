import bisect
str1,str2=0,0
with open("input36.txt","r") as file:
  str1=list(file.readline().strip())
  str2=list(file.readline().strip())

str1.sort()
str2.sort()

count=len(str2)

for letter in str2:
  index=bisect.bisect_left(str1,letter,0,len(str1)-1)
  if str1[index] != letter:
    continue
  else:
    del str1[index]
    count-=1

print(count)