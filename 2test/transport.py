# def addPrice(number, many, data, original ,deadLine, data_time, data_price):
#     original_time, original_price = original
#     addTime = original_time + data_time
#     addPrice = original_price + data_price
#     return process(number, many, data, deadLine, [addTime, addPrice], )
    
# def process(number, many, data, deadLine, timeAndPrice, temPrice, result, res_time):
#     # 如果可行，且不會超過deadLine的話，那麼便回傳數值，否則下一個
#     # time = 0
#     # result = 0
#     # 把參數丟進去算
#     print("- - -")
#     print(temPrice)
#     time, price = timeAndPrice
#     for item in data:
#         new_time, new_price = checkDeadLine(number, many, item, [time, price], deadLine)
#         result += new_price
#         print(result)
#         res_time += new_time
#         print(res_time)
#     # if result > temPrice:
#     #     temTime, temPrice = original
#     print(result, res_time)
#     if res_time <= deadLine and result > temPrice:
#         return result
#     temPrice = result

#     return process(number, many, data, deadLine, [new_time, new_price], temPrice, result, res_time)




# def checkDeadLine(number, many, data, original ,deadLine):
#     # 導出濃縮的參數
#     data_time, data_price = data
#     time, price = original
#     # 加總時間

#     # new_time, new_price = [time + data_time, price + data_price]
#     if new_time > deadLine:
#         return 0, 0
#     print(new_time,new_price)
#     return addPrice(number, many, data, original ,deadLine, data_time, data_price)
#     # return new_time, new_price

# def checkPrice(price,orig):

#     return 

# def main():
#     # 輸入各項參數
#     number = int(input())
#     many = int(input())
#     data = [
#                 [int(j) for j in input().split()]  # 工人的資料 
#                     for i in range(many)]
#     deadLine = int(input())
#     temPrice = 0
#     res_time = 0
#     time = 0
#     price = 0
#     result = 0
#     seed = 0
#     result = process(number, many, data, deadLine, [time, price], temPrice, result, res_time)
#     print(result)



def main():
    # 輸入各項參數
    number = int(input())
    many = int(input())
    data = [
                [int(j) for j in input().split()]  # 工人的資料 
                    for i in range(many)]
    deadLine = int(input())
    seed = 0
    result = process(number, data, deadLine,seed)
    print(result)

def process(number, data, deadLine, seed):

    result = 0
    origin = [0,0]
    for item in data:
        result += checkDeadLine(number, item, origin, deadLine, seed)
    return result

def checkDeadLine(number, data, original, deadLine, seed):
    data_time, data_price = data
    #導出濃縮的參數
    # data_time, data_price = data
    time, price = original
    # 加總時間
    new_time, new_price = [time + data_time, price + data_price]
    seed += 1 
    if new_time > deadLine and seed > number:
        return 0
    return checkPrice([new_time, new_price], [time, price], number, data, seed, deadLine)

def checkPrice(pos, origin_pos, number, item, seed, deadLine):
    origin_time, origin_price = pos
    item_time, item_price = item
    time, price = [origin_time + item_time, origin_price + item_price]
    if time > deadLine and seed > number:
        return 0
    return process(number, item, deadLine, seed)

if __name__ == "__main__":
    main()