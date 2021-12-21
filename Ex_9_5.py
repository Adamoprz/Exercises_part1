class Manager:
    def __init__(self):
        self.orders = {}
    def add_order(self, order_ob_, number_):
        if order_ob_ in self.orders.keys():
            self.orders[order_ob_] = self.orders[order_ob_] + number_
        else:
            self.order_ob_ = order_ob_
            self.number_ = number_
            self.orders[self.order_ob_] = self.number_

    def sell(self, id_to_sell):
        for order in self.orders:
            if order == id_to_sell:
                self.orders[order] -= 1


    def show_manager(self):
        print(self.orders)

class Order:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


def main():
    new_manager = Manager()
    new_manager.add_order("kasza" , 10)
    new_manager.add_order("kasza2", 10)
    new_manager.add_order("kasza2", 1)
    new_manager.add_order("kasza2", 7)

    new_manager.show_manager()
    new_manager.sell("kasza2")
    new_manager.sell("kasza")
    new_manager.show_manager()

if __name__ == "__main__":
    main()