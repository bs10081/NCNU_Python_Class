# file_Income.csv檔案中是家戶編號(ID)與家戶收入(Income)資料。請用泡沫排序法(課本8-7頁)將家戶收入由大到小重新排序
def main():
    a = open("file_Income.csv", "r", encoding="UTF-8")
    b = open("01_file_Income.csv", "w", encoding="UTF-8")
    # 準備寫入b檔案的欄位名稱
    new_row = "ID,Income\n"
    b.write(new_row)
    # 準備寫入b檔案的紀錄
    new_row = ""
    income = []
    rows = {}
    data = {}
    # 讀取a檔案的紀錄, 從第二行開始讀取
    for line in a:
        # 移除字串尾巴的\n新行符號
        rows = line.replace("\n", "")
        # 刪除第一行的欄位名稱
        if "ID,Income" in rows:
            continue
        # 把字串切割成不同欄位
        cols = rows.split(',')
        # 把家戶收入存入income串列
        income.append(int(cols[1]))
        # 把所有數據存到 data 字典中
        data[cols[0]] = cols[1]
    # 氣泡排序法
    bubbleSort(income)
    # 把氣泡排序法排序後的家戶收入寫入b檔案
    for i in range(len(income)):
        # 家戶編號 匹配 家戶收入
        for key, value in data.items():
            if str(income[i]) == value:
                new_row = key + "," + value + "\n"
                b.write(new_row)

    a.close()
    b.close()

# 氣泡排序法


def bubbleSort(income):
    for i in range(len(income)):
        for j in range(len(income) - 1):
            if income[j] < income[j + 1]:
                income[j], income[j + 1] = income[j + 1], income[j]
    return income


if __name__ == "__main__":
    main()
