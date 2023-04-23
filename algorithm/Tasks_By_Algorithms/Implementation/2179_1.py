from collections import defaultdict
def solution():
    prefix_map=defaultdict(list)

    for word_index in range(n):
        word=words[word_index]
        for letter_index in range(1,len(word)+1):
            prefix_map[word[:letter_index]].append(word_index)
    
    candidates=[]
    for prefix in prefix_map:
        word_list=prefix_map[prefix]
        if len(word_list) >= 2:
            candidates.append((len(prefix),word_list[0],word_list[1]))
    
    candidates.sort(key=lambda x:(-x[0],x[1],x[2]))

    _,first_index,second_index=candidates[0]
    print(words[first_index])
    print(words[second_index])

if __name__ == "__main__":
    with open("input2179.txt", "r") as file:
        n=int(file.readline())

        words=[file.readline().strip() for _ in range(n)]
    
    solution()