#Price List
price_apple = 10000
price_orange = 15000
price_grape = 20000
PriceList = f'''
Harga Apel = {price_apple}
Harga Jeruk = {price_orange}
Harga Anggur = {price_grape}'''
#Item Stock
stock_apple = 40
stock_orange = 30
stock_grape = 20
#Input
amount_apple = int(input("Jumlah apel yg dibeli: "))
while amount_apple > stock_apple:
    print("Jumlah yang dimasukkan terlalu banyak")
    amount_apple = int(input("Masukkan Jumlah Apel: "))
amount_orange = int(input("Jumlah jeruk yg dibeli: "))
while amount_orange > stock_orange:
    print("Jumlah yang dimasukkan terlalu banyak")
    amount_orange = int(input("Masukkan Jumlah jeruk: "))
amount_grape = int(input("Jumlah anggur yg dibeli: "))
while amount_grape > stock_grape:
    print("Jumlah yang dimasukkan terlalu banyak")
    amount_grape = int(input("Masukkan Jumlah anggur: "))
#Price
price_apple_total = price_apple*amount_apple
price_orange_total = price_orange*amount_orange
price_grape_total = price_grape*amount_grape
total_all = price_apple_total+price_orange_total+price_grape_total
#Detail belanja
print(f"Apel: {amount_apple} x {price_apple} = {price_apple_total}")
print(f"Jeruk: {amount_orange} x {price_orange} = {price_orange_total}")
print(f"Anggur: {amount_grape} x {price_grape} = {price_grape_total}")
print("Total belanja: ", total_all)
#Pembayaran
money = input("Masukkan Jumlah Uang: ")
money = float(money)
if money >= 0:
    while money < total_all:
        money_difference = abs(money-total_all)
        print("Uang anda kurang sebesar: ", abs(money_difference))
        money = money+(float(input("Masukkan Jumlah Uang: ")))
    if money >= total_all:
        print("Terima kasih")
        if money > total_all:
            print("Uang kembali anda: ", money-total_all)
else:
    print("Input tidak valid")