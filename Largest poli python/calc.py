import copy

class Calc:
    def __init__(self, number):
        self.__number = number
        self.__poli_list = self._make_list()
        self.__reversed_list = self._reverse_list()

    def get_number(self):
        return self.__number

    def _make_list(self):
        poli_list = []
        number = self.__number
        while number != 0:
            poli_list.append(number % 10)

            number //= 10
        return poli_list

    def _reverse_list(self):
        reverse = copy.deepcopy(self.__poli_list)
        reverse.reverse()
        return reverse

    def is_poli(self):
        return self.__poli_list == self.__reversed_list
