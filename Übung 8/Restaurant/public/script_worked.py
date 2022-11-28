class Restaurant:

    def __init__(self, restaurant_name, menu_list):
        self.__restaurant_name = restaurant_name
        self.__menu_list = menu_list
        self.__placed_orders = []

    def get_restaurant_name(self):
        return self.__restaurant_name

    def get_menu_list(self):
        return self.__menu_list[:]

    def get_order_list(self):
        if self.__placed_orders == []:
            return "No order yet"
        else:
            return self.__placed_orders[:]

    def set_order(self, item_list):
        order = []
        for item in item_list:
            if item in self.__menu_list:
                order.append(item)
        if len(order) != 0:
            order_1 = Order(order)
            self.__placed_orders.append(order_1)

    def get_revenue(self):
        total_revenue = 0
        for order in self.__placed_orders:
            total_revenue += order.get_bill_amount()
        return total_revenue