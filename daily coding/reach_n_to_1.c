
// Given a positive integer N, find the smallest number of steps it will take to reach 1

// You can perform any one of the following 3 steps

// 1.) Subtract 1 from it. ( n = n - 1 )

// 2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2 )

// 3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3 )

#include <stdio.h>

int min(int a, int b)
{
    return a < b ? a : b;
}

int reach_n_to_1(int n)

{   
    if (n == 1)
        return 0;
    int res = reach_n_to_1(n - 1);
    if (n % 2 == 0)
        res = min(res, reach_n_to_1(n / 2));
    if (n % 3 == 0)
        res = min(res, reach_n_to_1(n / 3));
    return res + 1;
}


int main()
{
    int n = 100;
    printf("Minimum steps required to reach 1 from %d is %d", n, reach_n_to_1(n));
    return 0;
}