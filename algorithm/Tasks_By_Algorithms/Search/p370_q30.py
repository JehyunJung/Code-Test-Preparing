from bisect import bisect_left, bisect_right

def count_by_range(a,left_value,right_value):
  left_index=bisect_left(a,left_value)
  right_index=bisect_right(a,right_value)
  return right_index-left_index

words=[]
queries=[]
answers=[]

with open("input30.txt","r") as file:
  words=list(map(str,file.readline().split()))
  queries=list(map(str,file.readline().split()))

  word_array=[[] for _ in range(10001)]
  reversed_word_array=[[] for _ in range(10001)]
    
for word in words:
  word_array[len(word)].append(word)
  reversed_word_array[len(word)].append(word[::-1])

for i in range(10001):
  word_array[i].sort()
  reversed_word_array[i].sort()
    
for query in queries:
  if query[0] != '?':
    answers.append(count_by_range(word_array[len(query)],query.replace('?','a'),query.replace('?','z')))
  else:
    reversed_query=query[::-1]
    answers.append(count_by_range(reversed_word_array[len(query)],reversed_query.replace('?','a'),reversed_query.replace('?','z')))
    
print(answers)