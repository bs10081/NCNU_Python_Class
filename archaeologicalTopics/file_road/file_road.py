# 1. 請問全國有多少條路或街？


def Q1():
    # 匯入檔案 file_road.csv
    data = []
    with open("file_road.csv", "r", encoding="UTF-8-sig") as file:
        for line in file:
            data.append(line.split())
    print("全國共有", len(data), "條路或街")

# 2. 請問南投縣有多少條路或街？


def Q2():
    # 匯入檔案 file_road.csv
    data = []
    with open("file_road.csv", "r", encoding="UTF-8-sig") as f:
        for line in f:
            data.append(line.split(","))
    # 計算南投縣的數量
    count = 0
    for i in data:
        if i[0] == "南投縣":
            count += 1
    print("南投縣共有", count, "條路或街")

# 3. 請用split函數將每列資料分成三部分，請列出路名中包含「中山」兩個字的路或街？


def Q3():
    # 匯入檔案 file_road.csv
    data = []
    with open("file_road.csv", "r", encoding="UTF-8-sig") as f:
        for line in f:
            data.append(line.split(","))
    # 列出路名中包含「中山」兩個字的路或街
    for i in data:
        if "中山" in i[2]:
            print(*i)

# 4. 請用split函數將每列資料分成三部分，請算出路名中包含「龍富」兩個字的路或街的數目？


def Q4():
    # 匯入檔案 file_road.csv
    data = []
    with open("file_road.csv", "r", encoding="UTF-8-sig") as f:
        for line in f:
            data.append(line.split(","))
    # 計算路名中包含「龍富」兩個字的路或街的數目
    count = 0
    for i in data:
        if "龍富" in i[2]:
            count += 1
    print("路名中包含「龍富」兩個字的路或街共有", count, "條")

# 5. 請問台中市有幾個區？


def Q5():
    # 匯入檔案 file_road.csv
    data = []
    with open("file_road.csv", "r", encoding="UTF-8-sig") as f:
        for line in f:
            data.append(line.split(","))
    print("// 本題需計算較長時間, 請稍候😄")
    # 計算臺中市的區數
    count = 0
    for i in data:
        if i[0] == "臺中市":
            # 添加區名到list
            if i[1] not in data:
                data.append(i[1])
                count += 1
    print("臺中市共有", count, "個區")


# 6. 請問全國有幾個「中山區」？
def Q6():
    # 匯入檔案 file_road.csv
    data = []
    with open("file_road.csv", "r", encoding="UTF-8-sig") as f:
        for line in f:
            data.append(line.split(","))
    # 計算全國的「中山區」數量
    count = 0
    for i in data:
        # 判斷是否有「中山區」等字眼
        if "中山區" in i[1]:
            # 排除重複的「中山區」
            if i[0] not in data:
                count += 1
    print("全國共有", count, "個「中山區」")

# 選擇要輸出的題目


def main():
    # 輸入要輸出的題目
    while True:
        set = input("請輸入要輸出的題目(1 ~ 6, 輸入 q 退出)：")
        # 判斷輸入的題目
        if set == "1":
            Q1()
        elif set == "2":
            Q2()
        elif set == "3":
            Q3()
        elif set == "4":
            Q4()
        elif set == "5":
            Q5()
        elif set == "6":
            Q6()
        elif set == "q":
            print("拜拜👋")
            quit()
        else:
            print("輸入錯誤, 只能輸入 1 ~ 6 或 q 哦")


if __name__ == "__main__":
    main()
