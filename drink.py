#---Mengimport file menu_item.py sebagai module--#
from menu_item import MenuItem

#---Membuat class anak yang bernama Drink---#
class Drink(MenuItem):
    #---Mendefinisikan nama, harga, dan volume minuman---#
    def __init__(self, name, price, volume):
        #--- Dengan menuliskan supper().methodName kita dapat menggunakan method instance yang didefinisikan di dalam class induk---#
        super().__init__(name, price)
        self.volume = volume

     #---Mendefinisikan Method info---#
    def info(self):
        return self.name + ': Rp ' + str(self.price) + ' (' + str(self.volume) + ' mL)'

    #mendefinisikan total harga pembelian minuman---#
    def get_total_price_drink(self, count_drink):
        total_price_drink = self.price * count_drink
        return round(total_price_drink)