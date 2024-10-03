#Price List
price_apple = 10000
price_orange = 15000
price_grape = 20000
PriceList = f'''
Harga Apel = {price_apple}
Harga Jeruk = {price_orange}
Harga Anggur = {price_grape}'''
print(PriceList)
#Input
amount_apple = input("Jumlah apel yg dibeli: ")
amount_orange = input("Jumlah jeruk yg dibeli: ")
amount_grape = input("Jumlah anggur yg dibeli: ")
#Convert to int
amount_apple = int(amount_apple)
amount_orange = int(amount_orange)
amount_grape = int(amount_grape)
#Price
price_apple_total = price_apple*amount_apple
price_orange_total = price_orange*amount_orange
price_grape_total = price_grape*amount_grape
#Detail belanja
print(f"Apel: {amount_apple} x {price_apple} = {price_apple_total}")
print(f"Jeruk: {amount_orange} x {price_orange} = {price_orange_total}")
print(f"Anggur: {amount_grape} x {price_grape} = {price_grape_total}")
print("Total belanja: ", price_apple_total+price_orange_total+price_grape_total)