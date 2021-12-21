class Manager:
    def __init__(self):
        self.dict = {}
    def add_order(self, order_ob_, number_):
        self.order_ob_ = order_ob_
        self.number_ = number_
        self.dict[self.order_ob_] = self.number_
    def show_manager(self):
        print(self.dict)

class Order:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


def main():
    new_manager = Manager()
    new_manager.add_order("kasza" , 10)
    new_manager.show_manager()

if __name__ == "__main__":
    main()