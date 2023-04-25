import sys
from collections import deque
def solution():
    word_stack=["a"]*len(word)
    target_word_length=len(target_word)
    top_index=0

    for char in word:
        word_stack[top_index]=char
        top_index+=1

        if top_index >= target_word_length:
            if word_stack[top_index-target_word_length:top_index] == target_word:
                top_index-=target_word_length
    
    remaining_word="".join(word_stack[:top_index])

    if remaining_word:
        print(remaining_word)
    else:
        print("FRULA")



if __name__ == "__main__":
    sys.stdin=open("input9935.txt","r")

    word=input().strip()
    target_word=list(input().strip())
    solution()
    