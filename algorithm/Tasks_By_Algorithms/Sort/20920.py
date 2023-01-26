from collections import Counter
import sys
def solution():
    print(Counter(words))
    vocabulary=[]

    for word,value in Counter(words).items():
        vocabulary.append((-value,-len(word),word))
    
    vocabulary.sort()

    for count,length,word in vocabulary:
        print(word)



if __name__ == "__main__":
    with open("input20920.txt","r") as file:
        n,m=map(int,file.readline().split())
        words=[]
        for word in [file.readline().strip() for _ in range(n)]:
            if len(word) < m:
                continue
            words.append(word)
    solution()
