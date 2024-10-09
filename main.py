print("Selamat Datang di Pasar Buah")
crud_menu = '''List Menu:
1. Menampilkan Daftar Buah
2. Menambah Buah
3. Menghapus Buah
4. Membeli Buah
5. Exit Program'''
print(crud_menu)
crud_exe = input("Masukkan angka Menu yang ingin dijalankan: ")
stock = {"Nama":['Apel  ','Jeruk ','Anggur'],
                 "Stock":[20,15,25],
                 "Harga":[10_000,15_000,20_000]}
while crud_exe.isdigit() == False or int(crud_exe) not in range(1,6):
    print("Input tidak valid")
    print(crud_menu)
    crud_exe = input("Masukkan angka Menu yang ingin dijalankan: ")
while crud_exe.isdigit() and int(crud_exe) in range(1,6):
    if int(crud_exe) == 1:
        print('''Daftar Harga Buah
Index  |Nama        |Stock   |Harga''')
        for a in range(len(stock["Nama"])):
            print(f"{a}      |{stock['Nama'][a]}      |{stock['Stock'][a]}      |{stock['Harga'][a]}")
        print(crud_menu)
        crud_exe = input("Masukkan angka Menu yang ingin dijalankan: ")
    elif int(crud_exe) == 2:
        new_fruit_name = input("Masukkan Nama Buah  : ")
        new_fruit_stock = int(input("Masukkan Stock Buah : "))
        new_fruit_price = int(input("Masukkan Harga Buah : "))
        stock["Nama"].append(new_fruit_name)
        stock["Stock"].append(new_fruit_stock)
        stock["Harga"].append(new_fruit_price)
        print('''Daftar Harga Buah
Index  |Nama        |Stock   |Harga''')
        for a in range(len(stock["Nama"])):
            print(f"{a}      |{stock['Nama'][a]}      |{stock['Stock'][a]}      |{stock['Harga'][a]}")
        print(crud_menu)
        crud_exe = input("Masukkan angka Menu yang ingin dijalankan: ")
    elif int(crud_exe) == 3:
        print('''Daftar Harga Buah
Index  |Nama        |Stock   |Harga''')
        for a in range(len(stock["Nama"])):
            print(f"{a}      |{stock['Nama'][a]}      |{stock['Stock'][a]}      |{stock['Harga'][a]}")
        stock_del = int(input("Masukkan index buah yang akan dihapus: "))
        stock["Nama"].pop(stock_del)
        stock["Stock"].pop(stock_del)
        stock["Harga"].pop(stock_del)
        print('''Daftar Harga Buah
Index  |Nama        |Stock   |Harga''')
        for a in range(len(stock["Nama"])):
            print(f"{a}      |{stock['Nama'][a]}      |{stock['Stock'][a]}      |{stock['Harga'][a]}")
        print(crud_menu)
        crud_exe = input("Masukkan angka Menu yang ingin dijalankan: ")
    elif int(crud_exe) == 4:
        print('''Daftar Harga Buah
Index  |Nama        |Stock   |Harga''')
        for a in range(len(stock["Nama"])):
            print(f"{a}      |{stock['Nama'][a]}      |{stock['Stock'][a]}      |{stock['Harga'][a]}")
        option = "ya".lower()
        total_pay = 0
        list_buy={"Nama":[],"Stock":[],"Harga":[]}
        while option.lower() == "ya":
            buy_fruit = int(input("Masukkan index buah yang ingin dibeli: "))
            if buy_fruit <= len(stock["Nama"])-1:
                stock_buy = int(input("Masukkan jumlah buah yang ingin dibeli: "))
                if stock_buy <= stock["Stock"][buy_fruit]:
                    stock["Stock"][buy_fruit] = stock["Stock"][buy_fruit]-stock_buy
                    list_buy["Nama"].append(stock["Nama"][buy_fruit])
                    list_buy["Stock"].append(stock_buy)
                    list_buy["Harga"].append(stock["Harga"][buy_fruit])
                else:
                    print(f"Stok buah tidak cukup, stock {stock["Nama"][buy_fruit]} tinggal {stock["Stock"][buy_fruit]}")
            else:
                print("Index tidak ada dalam daftar")
                buy_fruit = int(input("Masukkan index buah yang ingin dibeli: "))
            print("Isi cart: ")
            print("Nama    |   Harga   |   Qty")
            for b in range(len(list_buy["Nama"])):
                print(f'{list_buy["Nama"][b]}   |   {list_buy["Harga"][b]}   |   {list_buy["Stock"][b]}')
            option = input("Mau beli yang lain?(Ya/Tidak) ").lower()
        else:
            for b in range (len(list_buy["Nama"])):
                total_pay = total_pay + (list_buy["Harga"][b]*list_buy["Stock"][b])
            print("Total yang harus dibayar: ", total_pay)
            money = 0
            while total_pay > money:
                money = int(input("Masukkan jumlah uang: "))
                if total_pay > money:
                    money_diff = total_pay - money
                    print("Transaksi anda dibatalkan")
                    print(f"Uang kurang sebesar {money_diff}")
                elif total_pay >= money:
                    print("Terimakasih")
                    if total_pay > money:
                        print(f"Uang kembali anda: {money - total_pay}")
        break
    elif int(crud_exe) == 5:
        print("Terima kasih telah mengunjungi Pasar Buah")
        break
    # #Input
    # amount_apple = int(input("Jumlah apel yg dibeli: "))
    # while amount_apple > stock_apple:
    #     print("Jumlah yang dimasukkan terlalu banyak")
    #     amount_apple = int(input("Masukkan Jumlah Apel: "))
    # amount_orange = int(input("Jumlah jeruk yg dibeli: "))
    # while amount_orange > stock_orange:
    #     print("Jumlah yang dimasukkan terlalu banyak")
    #     amount_orange = int(input("Masukkan Jumlah jeruk: "))
    # amount_grape = int(input("Jumlah anggur yg dibeli: "))
    # while amount_grape > stock_grape:
    #     print("Jumlah yang dimasukkan terlalu banyak")
    #     amount_grape = int(input("Masukkan Jumlah anggur: "))
    # #Price
    # price_apple_total = price_apple*amount_apple
    # price_orange_total = price_orange*amount_orange
    # price_grape_total = price_grape*amount_grape
    # total_all = price_apple_total+price_orange_total+price_grape_total
    # #Detail belanja
    # print(f"Apel: {amount_apple} x {price_apple} = {price_apple_total}")
    # print(f"Jeruk: {amount_orange} x {price_orange} = {price_orange_total}")
    # print(f"Anggur: {amount_grape} x {price_grape} = {price_grape_total}")
    # print("Total belanja: ", total_all)
    # #Pembayaran
    # money = input("Masukkan Jumlah Uang: ")
    # money = float(money)
    # if money >= 0:
    #     while money < total_all:
    #         money_difference = abs(money-total_all)
    #         print("Uang anda kurang sebesar: ", abs(money_difference))
    #         money = money+(float(input("Masukkan Jumlah Uang: ")))
    #     if money >= total_all:
    #         print("Terima kasih")
    #         if money > total_all:
    #             print("Uang kembali anda: ", money-total_all)
    # else:
    #     print("Input tidak valid")