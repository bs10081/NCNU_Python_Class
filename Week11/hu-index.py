# homework:
# input: give 34 ints represents each card's amount between 0 ~ 4
# 前27個是萬筒條，後面是東風、南風、西風、北風、紅中、青發、白板
# output: 可以胡哪幾張
# simple input:
# 3111111130000000000000000000000000
# output:
# 一萬 兩萬 三萬 四萬 五萬 六萬 七萬 八萬 九萬 
def disp(l):
    count = 0
    stack = []

    for index, item in enumerate(l):
        clearStack = False
        if(item > 0):
            if(item == 1):
                count += 1
                stack.append({
                    "type": int(index/9),
                    "pos": index % 9+1,
                    "num": item
                })
        else:
            clearStack = -1
        
        if(count >= 3):
            # for card in stack:
            #     print(card)
            # print("="*20)
            clearStack = True
        
        if(item == 3):
            # print(index, item)
            # print("="*20)
            clearStack = True
        
        if(clearStack):
            if(count > 0 and count < 3):
                print(stack)
            count = 0
            stack = []

        if(clearStack == -1 and item == 1):
            print(index, item)
            count = 0
            stack = []

def main():
    l = [int(i) for i in input().split(" ")]
    print(l)
    disp(l)

if __name__ == "__main__":
    main()