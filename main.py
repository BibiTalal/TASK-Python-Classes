class Wallet:
    def __init__(self, money=0):
        self.money=money

    def credit(self,amount):
        self.money+=amount
    
    def debit(self,amount):
        self.money-=amount
    
    def __str__(self):
        return f"Money = {self.money}"
        


wallet = Wallet(6)
#wallet = Wallet()  # This should default money inside the wallet to 0
print(wallet)


class Person:
    def __init__(self,name,location,money):
        self.name=name
        self.location=location
        self.wallet=Wallet(money)

    def moveto(self,point):
        self.location=point

    def __str__(self):
        return f"New Location = {self.location}"
        
        



person = Person("Moh", 5, 50)
print(person)

class Vendor(Person):
    def __init__ (self,name,location,money):
        super().__init__(name,location,money)
        self.range=5
        self.price=1

    def sellto(self,customer,number_of_icecreams):
        self.location=customer.location
        self.wallet.credit(number_of_icecreams*self.price)
        customer.wallet.debit(number_of_icecreams*self.price)




vendor = Vendor("Abdallah", 3, 6)


class Customer(Person):
    def __init__(self,name,location,money):
        super().__init__(name,location,money)

    def _is_in_range(self,vendor):
        distance=vendor.location-self.location
        if distance>vendor.range:
            return True
        else:
            return False

    def _have_enough_money(self,vendor,number_of_icecreams):
        if self.wallet.money>=vendor.price*number_of_icecreams:
            return True
        else:
            return False

    def request_icecream(self,vendor,number_of_icecreams):
        if self._is_in_range(vendor) and self._have_enough_money(vendor,number_of_icecreams):
            vendor.sellto(self,number_of_icecreams)



customer = Customer("Abdallah", 3, 6)

vendor_bibi=Vendor("Bibi",2,3)
near_customer=Customer("Lulu", 11, 7)
far_customer=Customer("Dalal",200,16)
broke_customer=Customer("Dana",16,0)

near_customer.request_icecream(vendor_bibi,10)
print(near_customer.wallet.money)
print(vendor_bibi.wallet.money)
print(vendor_bibi.location)

far_customer.request_icecream(vendor_bibi,10)
print(far_customer.wallet.money)
print(vendor_bibi.wallet.money)
print(vendor_bibi.location)

broke_customer.request_icecream(vendor_bibi,1)
print(broke_customer.wallet.money)
print(vendor_bibi.wallet.money)
print(vendor_bibi.location)

