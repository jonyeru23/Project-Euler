from calc import *


def main():
    upper_lim = 999
    lower_lim = 899
    the_largest_poli = 0

    for i in range(upper_lim, lower_lim, -1):
        for j in range(upper_lim, lower_lim, -1):
            a_number = Calc(i*j)
            if a_number.is_poli():
                the_largest_poli = max(the_largest_poli, a_number.get_number())
    print(the_largest_poli)




if __name__ == '__main__':
    main()