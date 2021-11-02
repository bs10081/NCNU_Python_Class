def checkIfDuplicates_1(indexStr, word):
    ''' Check if given list contains any duplicates '''
    if len(indexStr) == len(set(word)):
        return False
    else:
        return True

def main():
    indexStr = list(*input().split())
    word = list(*input().split())
    print(word) 
    # result = checkIfDuplicates_1(indexStr, word)
    # if result:
    #     print("yes")
    # else:
    #     print("no")

main()