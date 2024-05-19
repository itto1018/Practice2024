def judge_money(money):
    while True:
        global error_money
        error_money = 1
        # 10000円を超える場合
        if money > 10000:
            print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
            break
        # 投入金額が最小価格の商品未満の場合
        elif drink_list[min(drink_list)] > money:
            print(str(money) + "円では購入できる商品がありません。再度投入金額を入力してください")
            break
        # 投入金額に1,5円玉がある場合
        elif (str(money)[len(str(money)) - 1]) != "0":
            print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
            break
        else:
            error_money = 0
            break

def change_money(money):
    numbers = [0, 0, 0, 0]
    coins = [500, 100, 50, 10]
    yukichi = 0

    while money >= 1000:    
        yukichi += 1
        money -= 1000

    for i, coin in enumerate(coins):
        while money >= coin:    
            numbers[i] += 1
            money -= coin
    
    # お釣りをPrintする
    print( "1000円札" + str(yukichi) + "枚")
    for i, num in enumerate(numbers):
        if num > 0:
            print( str(coins[i]) + "円玉" + str(num) + "枚")

drink_list = {"お茶": 110, "コーヒー": 100, "ソーダ": 160, "コンポタージュ": 130}
money = 0

is_continue = "Y"
while(is_continue == "Y"):
    for drink_name in drink_list:
        print( drink_name+ "：" + str(drink_list[drink_name]) + "円")
    money += int(input("投入金額を入力してください： \n"))
    judge_money(money)
    if error_money == 0:
        drink = input("何を購入しますか（商品名/cancel）： \n")
        if drink != "cancel":
            money = money - drink_list[drink]
            print("残金：" + str(money) + "円")
            is_continue = input("続けて購入しますか（Y/N）")
        else:
            is_continue = "N"
            break
    continue

if(money > 0):
    change_money(money)