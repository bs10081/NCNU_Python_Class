def main():
    # Input the index and word, finally print
    print(*findSol(list(*input().split()), list(*input().split())))
        #👆🏻 use "*" to format the list
def findSol(indexStr, word):
    # default read and wordList
    read = 0
    wordList = []
    # load index to the program, and check whether there is an index value in word
    for i in range(len(indexStr)):
        for v in range(len(word)):
            if word[v] == indexStr[i]:
                # add index position to the list
                wordList.append(read)
        # Record every time check
        read += 1
    return wordList

if __name__ == "__main__":
    main()