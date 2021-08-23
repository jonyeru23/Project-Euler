#include <iostream>
#include <list>
#include <iterator>
#include <cmath>
using namespace std;


bool is_devided_by(long long int my_number, long long int the_checker);
bool is_prime(long long int the_checker);
//The prime factors of 13195 are 5, 7, 13 and 29.

//What is the largest prime factor of the number 600851475143 ?


int main()
{
    long long int my_number = 600851475143;

    long long int largest_prime_factor = 0;
    
    for (long long int the_checker = my_number; the_checker > 1; the_checker--)
    {
        if (is_devided_by(my_number, the_checker) && is_prime(the_checker))
        {
            largest_prime_factor = the_checker;
            break;
        }
    }
    cout<<largest_prime_factor<<"";

    return 0;    
}

bool is_devided_by(long long int my_number, long long int the_checker)
{
    return my_number % the_checker == 0;
}

bool is_prime(long long int the_checker)
{
    for (long long int i = 2; i < sqrt(the_checker); i++)
    {
        if (the_checker % i == 0)
        {
            return false;            
        }
    }
    return true;
}
