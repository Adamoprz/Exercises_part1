class Manager:
    def __init__(self) -> None:
        self.orders = {}
    def add_order(self, a:list, number_:int) -> None:
        order_ = Order(a)
        temp_order = order_.return_order()
        if temp_order in self.orders.keys():
            self.orders[temp_order] = self.orders[temp_order] + number_
        else:
            self.order_ob_ = temp_order
            self.number_ = number_
            self.orders[self.order_ob_] = self.number_

    def sell(self, id_to_sell: list) -> None:
        for order in self.orders:
            id_to_sell_temp = ((id_to_sell[0],id_to_sell[1],id_to_sell[2]))
            if order == id_to_sell_temp:
                self.orders[order] -= 1


    def show_manager(self) -> str:
        print(self.orders)

class Order:
    def __init__(self, id_name_price) -> None:
        self.id = id_name_price[0]
        self.name = id_name_price[1]
        self.price = id_name_price[2]
    def return_order(self):
        return (self.id, self.name, self.price)

def main():
    new_manager = Manager()
    new_manager.add_order([1, "kasza", 125], 10)
    new_manager.add_order([2, "kasza2", 125], 10)
    new_manager.add_order([3, "kasza3", 125], 10)
    new_manager.add_order([2, "kasza2", 125], 10)

    new_manager.show_manager()
    new_manager.sell([2, "kasza2", 125])
    new_manager.show_manager()

if __name__ == "__main__":
    main()