# 學號 : 109213075
# 姓名 : 黃令瑋

def findsol(data,r,c,fold):
    #print(data,fold)
    for i in range(len(fold)):#執行直到摺疊指令都完成
        if fold[i]==0:#上下對折
            (data,r,c) =   up_down_fold(data,r,c)
        elif fold[i]==1:#左右對折
            (data,r,c)= left_right_fold(data,r,c)
    for i in range(len(data)):#輸出答案
            print(*data[i])

def up_down_fold(data,r,c):#上下對折
    if (len(data)%2==1):#1.行為奇數
        #temp用來暫存折疊的結果
        temp=[[1]*(c) for empty in range(r//2+1)]#折疊後的列數為原本的列數//2+1，行數不變
        for i in range( len(temp)):#分別填入結果
            for j in range(len(temp[i])):
                if i!=len(temp)-1:#最中間一行的結果與原始相同
                    temp[i][j]=data[i][j]+data[len(data)-1-i][j]#一行中對稱的數字相加
                else:
                    temp[i][j]=data[i][j]#最中間一行的結果與原始相同

    else:#2.行為偶數
        temp=[[1]*(c) for empty in range(r//2)]#折疊後的行數為原本的行數/2，列數不變
        for i in range( len(temp)):#分別填入結果
            for j in range(len(temp[i])):
                temp[i][j]=data[i][j]+data[len(data)-1-i][j]#一行中對稱的數字相加


    return (temp,len(temp),len(temp[0]))#回傳折疊後的結果


def left_right_fold(data,r,c):#左右對折
    if (len(data[0])%2==1): #1.列為奇數
        #temp用來暫存折疊的結果
        temp=[[1]*(c//2+1) for empty in range(r)]#折疊後的行數為原本的行數//2+1，列數不變
        for i in range( len(temp)):#分別填入結果
            for j in range(len(temp[i])):
                if j!=len(temp[i])-1:#最中間一列的結果與原始相同，要另外填入
                    temp[i][j]=data[i][j]+data[i][len(data[i])-1-j]#一列中對稱的數字相加
                else:
                    temp[i][j]=data[i][j]#最中間一列的結果與原始相同

    else:#2.列為偶數
        temp=[[1]*(c//2) for empty in range(r)]#折疊後的列數為原本的行數//2，行數不變
        for i in range( len(temp)):#分別填入結果
            for j in range(len(temp[i])):
                temp[i][j]=data[i][j]+data[i][len(data[i])-1-j]#一列中對稱的數字相加

    return (temp,len(temp),len(temp[0]))#回傳折疊後的結果

def main(): 
    r,c=map(int,input().split()) #輸入r,c，分別代表列數及行數
    data=[[int(v) for v in input().split()]for i in range(r)]#輸入資料
    fold=list(map(int,input().split()))#輸入摺疊指令
    findsol(data,r,c,fold)#執行

main()