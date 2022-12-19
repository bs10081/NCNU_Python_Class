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
    # 讀取a檔案的紀錄, 從第二行開始讀取
    for line in a.readlines()[1:]:
        # 移除字串尾巴的\n新行符號
        rows = line.replace("\n", "")
        # 把字串切割成不同欄位
        cols = rows.split(',')
        # 將 ID 與 Income 做成字典
        rows = {"ID": cols[0], "Income": cols[1]}
        # 將家戶收入(Income)資料存入income串列
        income.append(int(rows["Income"]))
    # 泡沫排序法
    for i in range(len(income) - 1):
        for j in range(len(income) - 1 - i):
            if income[j] < income[j + 1]:
                income[j], income[j + 1] = income[j + 1], income[j]
    # 根據rows字典,匹配 家戶編號(ID)與家戶收入(income)資料, 並寫入b檔案
    for i in range(len(income)):
        for line in a.readlines()[1:]:
            rows = line.replace("\n", "")
            cols = rows.split(',')
            rows = {"ID": cols[0], "Income": cols[1]}
            if income[i] == int(rows["Income"]):
                new_row = rows["ID"] + "," + rows["Income"] + "\n"
    b.write(new_row)

    a.close()
    b.close()


if __name__ == "__main__":
    main()
