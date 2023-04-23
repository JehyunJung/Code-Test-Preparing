def count_prefix(word1,word2):
    length=min(len(word1),len(word2))
    count=0
    for index in range(length):
        if word1[index]==word2[index]:
            count+=1
        else:
            break
    return count

def solution():
    sorted_words=sorted(words)
    length=[0] * n

    #각각의 문자열이 가질 수 있는 최대 접두어 길이를 구한다.
    for index in range(1,n):
        previous_word,previous_index=sorted_words[index-1]
        current_word,current_index=sorted_words[index]
        prefix_size=count_prefix(previous_word,current_word)

        length[previous_index]=max(length[previous_index],prefix_size)
        length[current_index]=max(length[current_index],prefix_size)

    max_prefix_cont=max(length)

    first,second="",""
    prefix=""
    for i in range(n):
        if first == "":
            if length[i]==max_prefix_cont:
                first=words[i][0]
                prefix=words[i][0][:max_prefix_cont]
                continue
        else:
            if length[i]==max_prefix_cont and words[i][0][:max_prefix_cont] == prefix:
                second=words[i][0]
                break
        
    print(first)
    print(second)             

if __name__ == "__main__":
    with open("input2179.txt", "r") as file:
        n=int(file.readline())

        words=[(file.readline().strip(),i) for i in range(n)]
    
    solution()
if __name__ == "__main__":
    with open("input2179.txt", "r") as file:
        n=int(file.readline())

        words=[(file.readline().strip(),i) for i in range(n)]
    
    solution()