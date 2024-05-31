class shopping:
    def  __init__(self,name):
        self.name=name
        self.card=[]

    def add_to_card(self,item,price,quantity):
        product={'item':item,'price': price,'quantity':quantity}
        self.card.append(product)

    def checkout(self,amount):
        total=0
        for item in self.card:
            total +=item['price'] * item['quantity']
        print('total amount',total)
        if amount < total:
            print(f'please provide: {total-amount} more')
        else:
            extra=amount-total
            print(f'Here is your product and extra money:{extra}')


noyon=shopping('Mahedi')
noyon.add_to_card('phone',1000,2)
noyon.add_to_card('laptop',22000,2)
noyon.add_to_card('tv',5000,2)

print(noyon.card)
noyon.checkout(60000)