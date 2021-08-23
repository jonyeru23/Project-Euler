#include <iostream>
using namespace std;


int main() 
{
    int the_sum = 0;

    for(int i = 0; i < 1000; i++){
        if (i % 3 == 0)
        {
            the_sum += i;
        }
        else if (i % 5 == 0)
        {
            the_sum += i;
        }
        
    }
    cout<<the_sum<<"";
    return 0;
}