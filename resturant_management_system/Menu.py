class Menu:
    def __init__(self):
        self.items = [] # item er data base

    def Add_menu_item(self,item):
        self.items.append(item)

    def find_item(self,item_name):
        print(self.items[0].name)
        for item in self.items:
           
            if item.name.lower() == item_name.lower():
                return item
        
                
    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item delected Successfully..!")
        else:
            print("Item not found..!")

    def show_Menu(self):
        print("Menu\tprice\tQuantity")
        print(self.items)
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')
