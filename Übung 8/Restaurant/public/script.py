from item import Item
from order import Order


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
        for item in item_list:
            if item not in self.__menu_list:
                item_list.remove(item)
        if len(item_list) != 0:
            self.__placed_orders.append(Order(item_list))

    def get_revenue(self):
        total_revenue = 0
        for order in self.__placed_orders:
            total_revenue += order.get_bill_amount()
        return total_revenue


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    # Create Item Objects with Name and Price
    steak = Item("Steak", 25)
    salad = Item("Salad", 10)
    fish = Item("Fish", 30)
    pizza = Item("Pizza", 40)
    # Create menu list
    menu_list = [steak]
    # Create order list
    order_list = [steak, fish, steak]
    # Create restaurant object with name and menu list
    restaurant = Restaurant("Zurich_1", menu_list)
    # Create an order with the order list
    restaurant.set_order(order_list)
    # Get the revenue of the restaurant object
    print(restaurant.get_revenue())
    print(restaurant.get_order_list())
