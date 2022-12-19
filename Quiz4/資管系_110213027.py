# 請用 file_road.csv 檔案，剔除 site_id 欄位值的縣市名稱，例如，將「金門縣金城鎮」改為「金城鎮」，並將新紀錄另外存成「01_file_road_鄉鎮.csv」。
def Q1():
    a = open("file_road.csv", "r", encoding="UTF-8")  # only read
    b = open("01_file_road_鄉鎮.csv", "w", encoding="UTF-8")  # only write
    for line in a:
        # 移除字串尾巴的\n新行符號
        row = line.replace("\n", "")
        # 把字串切割成不同欄位
        cols = row.split(',')
        # 準備寫入b檔案的紀錄
        new_row = ""
        # 選擇符合條件的紀錄，寫入b檔案中
        if cols[0] in cols[1]:
            # 刪除縣市名稱
            new_row = cols[0] + "," + \
                cols[1].replace(cols[0], "") + "," + cols[2] + "\n"
            b.write(new_row)

    a.close()
    b.close()

# 請用 file_road.csv 檔案，找出南投縣、彰化縣與臺中市的路與街，並將這些記錄另存成檔案「02_file_road_南投彰化台中.csv」。


def Q2():
    a = open("file_road.csv", "r", encoding="UTF-8")
    b = open("02_file_road_南投彰化台中.csv", "w", encoding="UTF-8")
    for line in a:
        # 移除字串尾巴的\n新行符號
        row = line.replace("\n", "")
        # 把字串切割成不同欄位
        cols = row.split(',')
        # 準備寫入b檔案的紀錄
        new_row = ""
        # 選擇符合條件的紀錄，寫入b檔案中
        if ('南投縣' in cols[0] or '彰化縣' in cols[0] or '臺中市' in cols[0]) and cols[2] != "" and (cols[2][-1] == "路" or cols[2][-1] == "街"):
            new_row = cols[0]+","+cols[1]+","+cols[2]+"\n"
            b.write(new_row)

    a.close()
    b.close()

# 請找出 file_road_null.csv 檔案中各欄位有下列情況的紀錄，將這些紀錄另存成「03_file_road_error.csv」。情況一，各欄位有空值，也就是沒有任何值。情況二，各欄位值的前、後、與中間出現空格,@,$,或者%的情況，例如，「金 門縣」、「 中山路」、「中山區 」、或者「中@山區 」。情況三，各欄位中出現阿拉伯數字。


def Q3():
    a = open("file_road_null.csv", "r", encoding="UTF-8")
    b = open("03_file_road_error.csv", "w", encoding="UTF-8")
    for line in a:
        # 移除字串尾巴的\n新行符號
        row = line.replace("\n", "")
        # 把字串切割成不同欄位
        cols = row.split(',')
        # 準備寫入b檔案的紀錄
        new_row = ""
        # 各欄位有空值，也就是沒有任何值。
        if cols[0] == "" or cols[1] == "" or cols[2] == "":
            new_row = cols[0]+","+cols[1]+","+cols[2]+"\n"
            b.write(new_row)

        # # 各欄位值的前、後、與中間出現空格,@,$,或者%的情況，例如，「金 門縣」、「 中山路」、「中山區 」、或者「中@山區 」
        # elif " " in cols[0] or " " in cols[1] or " " in cols[2] or "@" in cols[0] or "@" in cols[1] or "@" in cols[2] or "$" in cols[0] or "$" in cols[1] or "$" in cols[2] or "%" in cols[0] or "%" in cols[1] or "%" in cols[2]:
        #     new_row = cols[0]+","+cols[1]+","+cols[2]+"\n"
        #     b.write(new_row)

        # 各欄位中出現亂碼或非中文字
        elif not isChinese(cols[0]) or not isChinese(cols[1]) or not isChinese(cols[2]):
            new_row = cols[0]+","+cols[1]+","+cols[2]+"\n"
            b.write(new_row)
    a.close()
    b.close()


def isChinese(word):
    # 判斷是否為中文
    for ch in word:
        # 中文範圍
        if not '\u4e00' <= ch <= '\u9fff':
            return False
    return True


# 如果 file_road_null.csv 檔案中 city 或 site_id 欄位中有空值，請用前一筆紀錄的相同欄位的值取代目前的紀錄的空值，並將補值之後的紀錄另存新檔「04_file_road_error.csv」。提醒：只儲存有補值的紀錄即可。


def Q4():
    a = open("file_road_null.csv", "r", encoding="UTF-8")
    b = open("04_file_road_error.csv", "w", encoding="UTF-8")
    for line in a:
        # 移除字串尾巴的\n新行符號
        row = line.replace("\n", "")
        # 把字串切割成不同欄位
        cols = row.split(',')
        # 準備寫入b檔案的紀錄
        new_row = ""
        # 如果city欄位中有空值
        if cols[0] == "":
            # 用前一筆紀錄的city欄位值取代目前的紀錄的空值
            new_row = last_city+","+cols[1]+","+cols[2]+"\n"
            b.write(new_row)
        else:
            # 如果city欄位中沒有空值，則 pass
            new_row = cols[0]+","+cols[1]+","+cols[2]+"\n"
            last_city = cols[0]
    a.close()
    b.close()

# 建立包含 city, site_id, road, roadno 等四個欄位的「05_file_road_no.csv」。找出file_road.csv 檔案中臺北市的路與街，並將這些路與街從 1001 開始編號存入「05_file_road_no.csv」，roadno 欄位存放路與街的編號。


def Q5():
    a = open("file_road_null.csv", "r", encoding="UTF-8")
    b = open("05_file_road_no.csv", "w", encoding="UTF-8")
    # 準備寫入b檔案的欄位名稱
    new_row = "city,site_id,road,roadno\n"
    b.write(new_row)
    # 準備寫入b檔案的紀錄
    new_row = ""
    # 路與街的編號
    roadno = 1001
    for line in a:
        # 移除字串尾巴的\n新行符號
        row = line.replace("\n", "")
        # 把字串切割成不同欄位
        cols = row.split(',')
        # 選擇符合條件的紀錄，寫入b檔案中
        if '臺北市' in cols[0] and cols[2] != "" and (cols[2][-1] == "路" or cols[2][-1] == "街"):
            new_row = cols[0] + "," + cols[1] + "," + \
                cols[2] + "," + str(roadno) + "\n"
            b.write(new_row)
            roadno += 1
    a.close()
    b.close()

# 寫一支程式讓使用者可以依序輸入檔案名字、縣市、鄉鎮、與街道等資料，然後將輸入的資料存放到使用者所設定檔名的檔案中。


def Q6():
    # 輸入檔案名字
    file_name = input("請輸入檔案名字：")
    # 輸入縣市
    city = input("請輸入縣市：")
    # 輸入鄉鎮
    site_id = input("請輸入鄉鎮：")
    # 輸入與街道
    road = input("請輸入與街道：")
    # 寫入檔案
    a = open(file_name, "w", encoding="UTF-8")
    # 標頭
    new_row = "city,site_id,road\n"
    a.write(new_row)
    # 紀錄
    new_row = ""  # 準備寫入a檔案的紀錄
    new_row = city+","+site_id+","+road+"\n"
    a.write(new_row)  # 寫入a檔案的紀錄
    a.close()
