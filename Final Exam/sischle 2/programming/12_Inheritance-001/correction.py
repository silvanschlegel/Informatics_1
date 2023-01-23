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
        super()
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

