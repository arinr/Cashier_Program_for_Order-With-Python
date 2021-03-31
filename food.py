#---Mengimport file menu_item.py sebagai module--#
from menu_item import MenuItem

#---Membuat class anak yang bernama Food---#
class Food(MenuItem):
    #---Mendefinisikan nama, harga, dan kalori makanan---#
    def __init__(self, name, price, calorie_count):
        super().__init__(name, price)
        self.calorie_count = calorie_count
        
    #---Mendefinisikan Method info---#
    def info(self):
        return self.name + ': Rp ' + str(self.price) + ' (' + str(self.calorie_count) + ' kal)'
    
    #---Mendefinisikan Method calorie_info---#
    def calorie_info(self):
        print(' kal: ' + str(self.calorie_count))
        
    #---Mendefinisikan total harga pembelian makanan---#
    def get_total_price_food(self, count_food):
        total_price_food = self.price * count_food
        return round(total_price_food)
