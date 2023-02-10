from collections import Counter
def solution():
    start_word=words[0]
    count=0
    for word in words[1:]:
        diff_count=0
        for char in start_word:
            if char in word:
                word.remove(char)
                continue
            else:
                diff_count+=1
        
        if diff_count>1 or len(word)>=2:
            continue

        count+=1
    
    print(count)
                

    
if __name__ == "__main__":
    with open("input2607.txt","r") as file:
        n=int(file.readline())
        words=[list(file.readline().strip()) for _ in range(n)]
    solution()