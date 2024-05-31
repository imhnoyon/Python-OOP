class shop:
    def __init__(self,customer):
        self.customer=customer
        self.card=[]
    def add_to_card(self,item):
        self.card.append(item)

Noyon =shop('Mahedi')
Noyon.add_to_card('Shoe')
Noyon.add_to_card('phone')
print(Noyon.card)