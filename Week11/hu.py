# 學號：110213027
# 姓名：簡齊君

def main():
    # input data
    data =list(map(int,input().split()))
    # set index
    card =["一萬","二萬","三萬","四萬","五萬","六萬","七萬","八萬","九萬","一筒","二筒","三筒","四筒","五筒","六筒","七筒","八筒","九筒","一條","二條","三條","四條","五條","六條","七條","八條","九條","東風","南風","西風","北風","紅中","青發","白板"]

    for i in range(len(data)):
        if data[i] <= 3:
            data[i] += 1
            if findSol(data,True):
                print(card[i])
            data[i] -= 1
# By returning true and false to judge whether the card is Hu.
def findSol(data, needMJ):
    # defined the result is false 
    result = False
    # do 34 times to check card.
    for i in range(34):
        # if card = 0, then continue
        if data[i] == 0:
            continue
        # if card > 2, then = "n"
        if data[i] > 2:
            # take the card
            data[i] -= 3
            if findSol(data, needMJ):
                result = True
            # put the card back
            data[i] += 3
        if needMJ and data[i] >= 2:
            data[i] -= 2
            if findSol(data,False):
                result = True
            data[i] += 2
        # Check whether the four types cards make up the result.
        if (data[i] >= 1) and (data[i+1] >= 1) and data[i+2] >= 1 and ((i < 7) or (8 < i < 16) or (17 < i < 25)):
            data[i] -= 1
            data[i+1] -= 1
            data[i+2] -= 1
            if findSol(data, needMJ):
                result = True
            data[i] += 1
            data[i+1] += 1
            data[i+2] += 1
        return result
    return True

if __name__ == "__main__":
    main()