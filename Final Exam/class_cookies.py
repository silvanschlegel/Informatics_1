from abc import ABC, abstractmethod

class Cookie:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price



class Container(ABC):



    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_number_of_cookies(self):
        pass

class Wrapper(Container):
    def __init__(self, cookies):
        if len(cookies) < 2 or len(cookies) > 5:
            raise ValueError
        self.__cookies = cookies


    def get_price(self):
        price =0
        for i in self.__cookies:
            price += i.get_price()
        return price

    def get_number_of_cookies(self):
        return len(self.__cookies)

    def get_contents(self):
        return cookies




class Box(Container):
    id = 1
    def __init__(self, wrappers):
        wrapper_count = 0
        for i in wrappers:
            wrapper_count +=  i.get_number_of_cookies()
        if wrapper_count > 200:
            raise ValueError
        self.__id = Box.id
        Box.id += 1

        self.__wrappers = wrappers


    def get_price(self):
        sum = 0
        for i in self.__wrappers:
            sum += i.get_price()
        return round(sum,2)

    def get_number_of_cookies(self):
        return sum(wrapper.get_number_of_cookies() for wrapper in self.__wrappers)

    def get_id(self):
        return self.__id









def make_cookies(n):
    return [Cookie("Chocolate", 0.50) if x % 2 == 0 else Cookie("Vanilla", 0.60) for x in range(n)]

cookies = make_cookies(4)
print(cookies[0].get_name())
print(cookies[0].get_price())
#
w1 = Wrapper(cookies)
print([c.get_name() for c in w1.get_contents()])

w2 = Wrapper(make_cookies(4))
b = Box([w1, w2])
print(f"\nCookies in box: {b.get_number_of_cookies()}")
print(f"  Price of box: {b.get_price()}")
print(f"     ID of box: {b.get_id()}\n")

more_wrappers = [Wrapper(make_cookies(4)) for x in range(52)] # 208 cookies
try:
    overfull = Box(more_wrappers)
except ValueError:
    print("Too many cookies for one box\n")