import numpy as np


class Polinome:
    def __init__(self, *coefficients, n=100000):

        """ input: coefficients are in the form a_n, ...a_1, a_0 """
        self.polinomial = np.polynomial.polynomial.Polynomial(np.array(coefficients))
        self.__results = self._get_natural_results(n)

    def get_results(self):
        return set(self.__results)

    def _get_natural_results(self, n):
        return [round(self.polinomial(i)) for i in range(1, n+1)]

    def intersection(self, other_set):
        return set(self.__results).intersection(other_set)

    def get_index(self, number):
        return self.__results.index(number) + 1
