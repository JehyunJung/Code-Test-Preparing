from itertools import combinations
from collections import Counter

def solution(depth,learned_words):
    global max_readable
    if depth==N:
        readable=0
        for word in words:
            if not set(Counter(word).keys()) - set(combination):
                readable+=1
        max_readable=max(readable,max_readable)
        return
    else:
        solution(depth+1,learned_words+[])
N,k=map(int,input().split())
words=[]
for _ in range(N):
    words.append(input().strip())
alpha_sets=[]
for word in words:
    word_counter=Counter(word)
    alpha_sets+=word_counter.keys()
alpha_sets=set(alpha_sets)
max_readable=0
for combination in list(combinations(alpha_sets,k)):
    readable=0
     
print(max_readable)