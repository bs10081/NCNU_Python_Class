# 12
# 3 33 27 44 2 21 47 43 29 19 6 0
# [['S', '4'], ['D', '8'], ['D', '2'], ['C', '6'], ['S', '3'], ['H', '9'], ['C', '9'], ['C', '5'], ['D', '4'], ['H', '7'], ['S', '7'], ['S', 'A']]

def main():
    n = int(input())
    data =list(map(int,input().split()))
    data = sameSuit(data)
    del data[0]
    # 丟完第一次牌，然後在進行比較
    result = (findSol(n ,data, seed = 1))
    print(result)
    
def sameSuit(data):
    color = ['S' , 'H' , 'D' , 'C']
    card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    result = []
    for s in data:
        # for c in range(4):
        result.append([color[s//13],card[(s%13)]])
    return result

def findSol(n,data,seed):
    del data[0]
    if n == 1:
        print(seed)
    for i in range(len(data)):
            if data[i][0] == data[i+1][0] or data[i][1] == data[i+1][1]:
                seed+= 1
                del data[i]
                
                print(seed)
                findSol(n-1,data,seed)

# # def findSol(n, data, seed):
#     if n == 1:
#         return seed
#     value = [i[0] for i in data]
#     value1 = [i[1] for i in data]
#     # print(data[0])
#     print()
#     # print(value)
#     # for i in range(len(data)):
#     #     if value[] in data[i+1] or value1[i] in data[i+1]:
#     #         print(value[i])
#     #         print(data[i+1])
#     #         # print(value1)
#     #         del data[i]
#     #         del data[i+1]
#     #         seed += 1
#     #         findSol(n-1, data, seed)
#     for i in range(len(value)):
#         print(value[i])
#         print(value[i+1])
#         print(value1[i])
#         print(value1[i+1])
#         if value[i] == value[i+1] or value1[i] == value1[i+1]:
#             seed += 1
#             print(seed)
#             # findSol(n-1, data, seed)
if __name__ == "__main__":
    main()