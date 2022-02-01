def solution(letter):
  letter_counter=dict()

  for char in letter:
    if char.upper() in letter_counter.keys():
      letter_counter[char.upper()]+=1
    else:
      letter_counter[char.upper()]=1
  
  max_count=max(letter_counter.values())
  
  count=0
  max_key=""
  for key,value in letter_counter.items():
    if value==max_count:
      max_key=key
      count+=1
  
  print(letter_counter,max_key,count)
  if count==1:
    return max_key

  else:
    return "?"

letter=""

with open("input1157.txt","r") as file:
  letter=file.readline()

print(solution(letter))