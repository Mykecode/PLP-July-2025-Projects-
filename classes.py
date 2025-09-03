class Phone:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
        
    def phone_info(self):
        print(f'{self.model} {self.brand}')


class Smartphone(Phone):
    def __init__(self, model, brand, color, storage, battery):
        super().__init__(model, brand)
        self.color = color
        self.storage = storage
        self.battery = battery
    
    def call(self):
        print(f'{self.brand} calling....')
    
    def message(self):
        print(f'{self.brand} messagin....')
        
    def charge(self):
        print(f'{self.brand} Charging.....')
        
    def phone_detail(self):
        print(f'Smartphone: {self.model},{self.brand}, {self.color}, {self.storage}GB {self.battery}mah')
        
phone1 = Smartphone('Andriod', 'Samsung S23 Ultra', 'Gold',256, 5000)

phone2 = Smartphone('Apple','Iphone 16 Pro Max', 'White', 512, 3000)

phone3 = Smartphone('Windows','Microsoft Lumia 950', 'black', 128, 5000)

phone1.phone_detail()
phone1.call()
phone1.message()
phone1.charge()
print(' ')

phone2.phone_detail()
phone2.call()
phone2.message()
phone2.charge()
print(' ')

phone3.phone_detail()
phone3.call()
phone3.message()
phone3.charge()
print(' ')
        
     