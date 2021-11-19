#呼叫自己的同伴來解決事情
#迴圈深度不確定的時候

def sumR(data):
    #最後一個
    if len(data) == 1:
        return data[0]
    return data[0]+sumR(data[1::]) #sumR(data[1::])類似一個迴圈，因為一直找同伴

#找最大()
def maxR(data):
    #最後一個同伴 #如果data長度為1(代表最後一個留下的人)
    if (len(data)==1):
        #回傳自己
        return data[0]
    #不是最後一個同伴 #不是呼叫自己，是呼叫自己的同伴
    if data[0] < maxR(data[1::]): #data[1::]移除1個
        return maxR(data[1::])
    else:
        return data[0]

def main():
    print(maxR([41,28,71,69,44]))
main()