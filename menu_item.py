#---Membuat class induk yang bernama MenuItem---#
class MenuItem:
    #---Mendefinisikan nama dan harga item---#
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    #---Mendefinisikan Method info---#
    def info(self):
        #---Menampilkan nama dan harga item---#
        return self.name + ': Rp ' + str(self.price)

