# 請問全國有多少條路或街?
def Q1():
    # 匯入檔案 file_road.csv
    data = []
    with open("file_road.csv", "r", encoding="UTF-8-sig") as file:
        for line in file:
            data.append(line.split(","))
        count = 0
        # 判斷路名(i[2])中 "最後"一個字是否為「路」或「街」
        for i in data:
            dataTmp = [one for one in i[2]]
            if "路" in dataTmp[-2] or "街" in dataTmp[-2]:
                count += 1
    print("全國共有", count, "條路或街")


# 請問南投縣與彰化縣共有多少條路或街?


def Q2():
    # 匯入檔案 file_road.csv
    data = []
    with open("file_road.csv", "r", encoding="UTF-8-sig") as f:
        for line in f:
            data.append(line.split(","))
    # 計算南投縣與彰化縣的數量
    count = 0
    for i in data:
        if i[0] == "南投縣" or i[0] == "彰化縣":
            # 判斷路名(i[2])中 "最後"一個字是否為「路」或「街」
            dataTmp = [one for one in i[2]]
            if "路" in dataTmp[-2] or "街" in dataTmp[-2]:
                count += 1
    print("南投縣與彰化縣共有", count, "條路或街")


# 請用split函數將每列資料分成三部分，請列出路名中包含「中山」或者「台灣」兩個字的路或街?


def Q3():
    # 匯入檔案 file_road.csv
    data = []
    with open("file_road.csv", "r", encoding="UTF-8-sig") as f:
        for line in f:
            data.append(line.split(","))
    # 列出路名中包含「中山」或者「台灣」兩個字的路或街
    for i in data:
        if "中山" in i[2] or "臺灣" in i[2]:
            # 判斷路名(i[2])中 "最後"一個字是否為「路」或「街」
            dataTmp = [one for one in i[2]]
            if "路" in dataTmp[-2] or "街" in dataTmp[-2]:
                print(*i)


# 請用split函數將每列資料分成三部分，請算出路名中包含「龍富」兩個字的路或街的數目?


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
            # 判斷路名(i[2])中 "最後"一個字是否為「路」或「街」
            dataTmp = [one for one in i[2]]
            if "路" in dataTmp[-2] or "街" in dataTmp[-2]:
                count += 1
    print("路名中包含「龍富」兩個字的路或街共有", count, "條")


# 請問臺中市與臺北市共有幾個區?


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
        if i[0] == "臺中市" or i[0] == "臺北市":
            # 添加區名到list
            if i[1] not in data:
                data.append(i[1])
                count += 1
    print("臺中市及臺北市共有", count, "個區")

# 請問全國有幾個「中山區」?


def Q6():
    # 匯入檔案 file_road.csv
    data = []
    with open("file_road.csv", "r", encoding="UTF-8-sig") as f:
        for line in f:
            data.append(line.split(","))
    # 計算全國的「中山區」數量
    count = 0
    # 建立一個空的list
    dataTmp = []
    for i in data:
        # 判斷是否有「中山區」等字眼
        if "中山區" in i[1]:
            # 排除重複的「中山區」
            if i[0] not in dataTmp:
                count += 1
                dataTmp.append(i[0])
    print("全國共有", count, "個「中山區」")
