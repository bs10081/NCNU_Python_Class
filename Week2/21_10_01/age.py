def main():
    # 輸入年紀
    age = int(input())
    
    if age >= 20:               # 如果大於等於20歲
        print('vote all')       # 擁有完整投票權
    elif age >= 18:             # 如果大於等於18歲 
        print('vote partial')   # 部分投票權
    else:                       # 否則
        print('no vote')        # 沒有投票權
 main()
