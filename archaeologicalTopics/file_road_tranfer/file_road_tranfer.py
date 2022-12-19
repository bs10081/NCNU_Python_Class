# 1.	請用file_road_null.csv 檔案，剔除site_id欄位值的縣市名稱，例如，將「金門縣金城鎮」改為「金城鎮」，並將新紀錄另外存成「01_file_road_鄉鎮.csv」

def Q1():
    a = open("file_road_null.csv", "r", encoding="UTF-8")  # only read
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
            new_row = cols[1].replace(cols[0], "") + "," + cols[2] + "\n"
            b.write(new_row)

    a.close()
    b.close()

# 2. 請找出南投縣與彰化縣的路與街，並另存成檔案「02_file_road_南投彰化.csv」？


def Q2():
    a = open("file_road_null.csv", "r", encoding="UTF-8")
    b = open("02_file_road_南投彰化.csv", "w", encoding="UTF-8")
    for line in a:
        # 移除字串尾巴的\n新行符號
        row = line.replace("\n", "")
        # 把字串切割成不同欄位
        cols = row.split(',')
        # 準備寫入b檔案的紀錄
        new_row = ""
        # 選擇符合條件的紀錄，寫入b檔案中
        if ('南投縣' in cols[0] or '彰化縣' in cols[0]) and cols[2] != "" and (cols[2][-1] == "路" or cols[2][-1] == "街"):
            new_row = cols[0]+","+cols[1]+","+cols[2]+"\n"
            b.write(new_row)

    a.close()
    b.close()

# 3. 請找file_road_null.csv 檔案中各欄位有下列情況的紀錄，並將這些紀錄另存成「03_file_road_error.csv」。情況一，各欄位有空值，也就是沒有任何值。情況二，各欄位值前、後、與中間出現空格的情況，例如，「金 門縣」、「 中山路」、或者「中山區 」。情況三，各欄位中出現英文字。


def isChinese(word):
    for ch in word:
        if not '\u4e00' <= ch <= '\u9fff':
            return False
    return True


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
        # 各欄位值前、後、與中間出現空格的情況，例如，「金 門縣」、「 中山路」、或者「中山區 」。
        elif cols[0].strip() != cols[0] or cols[1].strip() != cols[1] or cols[2].strip() != cols[2]:
            new_row = cols[0]+","+cols[1]+","+cols[2]+"\n"
            b.write(new_row)
        # 各欄位中出現英文字。
        elif not isChinese(cols[0]) or not isChinese(cols[1]) or not isChinese(cols[2]):
            new_row = cols[0]+","+cols[1]+","+cols[2]+"\n"
            b.write(new_row)
    a.close()
    b.close()

# 4. 如果file_road_null.csv 檔案中city欄位中有空值，請用前一筆紀錄的city欄位值取代目前的紀錄的空值，並將補值之後的紀錄另存新檔


def Q4():
    a = open("file_road_null.csv", "r", encoding="UTF-8")
    b = open("04_file_road_null.csv", "w", encoding="UTF-8")
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
            new_row = cols[0]+","+cols[1]+","+cols[2]+"\n"
            b.write(new_row)
            last_city = cols[0]
    a.close()
    b.close()

# 5. 建立包含city, site_id, road, roadno等四個欄位的「05_file_road_no.csv」。找出file_road_null.csv檔案中臺中市的路與街，並將這些路與街從1開始編存入「05_file_road_no.csv」，roadno欄位存放路與街的編號。


def Q5():
    a = open("file_road_null.csv", "r", encoding="UTF-8")
    b = open("05_file_road_no.csv", "w", encoding="UTF-8")
    # 準備寫入b檔案的欄位名稱
    new_row = "roadno,city,site_id,road\n"
    b.write(new_row)
    # 準備寫入b檔案的紀錄
    new_row = ""
    # 路與街的編號
    roadno = 1
    for line in a:
        # 移除字串尾巴的\n新行符號
        row = line.replace("\n", "")
        # 把字串切割成不同欄位
        cols = row.split(',')
        # 選擇符合條件的紀錄，寫入b檔案中
        if '臺中市' in cols[0] and cols[2] != "" and (cols[2][-1] == "路" or cols[2][-1] == "街"):
            new_row = str(roadno) + "," + \
                cols[0] + "," + cols[1] + "," + cols[2] + "\n"
            b.write(new_row)
            roadno += 1
    a.close()
    b.close()


def main():
    while True:
        print("請輸入要執行的題號(1~5)，或輸入0結束程式")
        q = input()
        if q == "0":
            break
        elif q == "1":
            Q1()
        elif q == "2":
            Q2()
        elif q == "3":
            Q3()
        elif q == "4":
            Q4()
        elif q == "5":
            Q5()
        else:
            print("輸入錯誤，請重新輸入")


if __name__ == '__main__':
    main()
