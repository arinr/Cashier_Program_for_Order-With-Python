#---Mengimport file food.py dan drink.py sebagai module---#
from food import Food
from drink import Drink

#---Membuat variable instance dengan menu makanan---#
food1 = Food('Nasi Goreng', 15000, 267)
food2 = Food('Mie Goreng', 10000, 350)
food3 = Food('CapCay', 15000, 110)
food4 = Food('Udang Saus Tiram', 20000, 240)
food5 = Food('Seblak', 8000, 315)
foods = [food1, food2, food3, food4, food5]

#---Membuat variable instance dengan menu minuman---#
drink1 = Drink('Kopi', 5000, 180)
drink2 = Drink('Jus Jeruk', 6000, 200)
drink3 = Drink('Yoghurt', 8000, 200)
drink4 = Drink('Es Teh Manis', 3000, 350)
drink5 = Drink('Air Putih', 2000, 200)
drinks = [drink1, drink2, drink3, drink4, drink5]

#---Menanyakan nama pembeli---#
nama_pembeli=input("Selamat datang di Arins Resto. Memesan atas nama siapa? ")

#---Menampilkan daftar menu makanan dan minuman---#
print('Daftar Menu Arins Resto ')
print('Makanan')
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

print('Minuman')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1

#---Memesan menu---#
food_order = int(input('Masukkan nomor makanan yang ingin Anda pesan: '))
selected_food = foods[food_order]
count_food = int(input("Ingin pesan berapa?"))

drink_order = int(input('Masukkan nomor minuman ingin Anda pesan: '))
selected_drink = drinks[drink_order]
count_drink = int(input("Ingin pesan berapa?"))

#---Panggil method get_total_price untuk food dan drink---#
total_price_foods = selected_food.get_total_price_food(count_food)
total_price_drinks = selected_drink.get_total_price_drink(count_drink)

#---Masukkan nama pesanan, quantity, harga satuan, dan total harga ke dalam list---#
name_order=[selected_food.name,selected_drink.name]
quantity=[count_food,count_drink]
item_price=[selected_food.price,selected_drink.price]
totals_price= [total_price_foods,total_price_drinks]


#---Jika ada tambahan pesanan---#
again=input("Apakah ada tambahan pesanan lagi? (makanan/minuman/tidak)")
again=again.lower()
while again != 'tidak' :
    if again == 'makanan':
        #---Memesan makanan kembali---#
        food_order = int(input('Masukkan nomor makanan yang ingin Anda pesan: '))
        selected_food = foods[food_order]
        count_food = int(input("Ingin pesan berapa?"))
        total_price_foods = selected_food.get_total_price_food(count_food)
        #---Memasukkan data pada list makanan yang sudah ada---#
        name_order.append(selected_food.name)
        quantity.append(count_food)
        item_price.append(selected_food.price)
        totals_price.append(total_price_foods)
        
    else :
        #---Memesan minuman kembali---#
        drink_order = int(input('Masukkan nomor minuman ingin Anda pesan: '))
        selected_drink = drinks[drink_order]
        count_drink = int(input("Ingin pesan berapa?"))
        total_price_drinks = selected_drink.get_total_price_drink(count_drink)
        #---Memasukkan data pada list minuman yang sudah ada---#
        name_order.append(selected_drink.name)
        quantity.append(count_drink)
        item_price.append(selected_drink.price)
        totals_price.append(total_price_drinks)
    
    #---Pertanyaaan ulangan---#
    again=input("Apakah ada tampahan pesanan lagi? (makanan/minuman/tidak)")
    again=again.lower()
    
#---Masukkan nama pesanan, quantity, harga satuan, dan total harga ke dalam data frame---#    
import pandas as pd 
df=pd.DataFrame()
df['Pesanan']=name_order
df['Total QTY']=quantity
df['Harga Satuan']=item_price
df['Total Harga']=totals_price
    
#---Membuat struk/tanda bukti pembayaran---#
print("------------------------------------------")
print("TERIMA KASIH TELAH MENGUNJUNGI ARINS RESTO")
print("------------------------------------------")
print(" ")
print("Rincian pesanan Anda:")
print(df)
print(" ")

#---Jumlah yang harus dibayar---#
print("------------------------------------------")
print("Total Bayar       Rp "+str(sum(df['Total Harga'])))
print("------------------------------------------")
print(" ")
print("Terima kasih "+nama_pembeli+"!")
print("Harap tunggu. Pesanan Anda sedang kami siapkan.")
