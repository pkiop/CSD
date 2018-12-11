#include <iostream>

using namespace std;

struct S {
       int v1;
       double v2;
};

void increase(S v)
{
       ++v.v1;
       cout << v.v1 << endl;
}

void print(const S v)
{
       //++v.v1;
       cout << v.v1 << endl;
}

int main(void)
{
       S x = { 33,3.3 };

       increase(x);
       cout << x.v1 << endl;

       print(x);
       cout << x.v1 << endl;
       return 0;
}