#include <iostream>
using namespace std;

int main()
{
  int size = 2;

  int a[2][2] = {{0,1},{1,0}};
  int b[2][2] = {{0,1},{0,1}};
  int mult[2][2] = {{0,0},{0,0}};
  int i,j,k;
    for(i = 0; i < size; ++i)
        for(j = 0; j < size; ++j)
            for(k = 0; k < size; ++k)
            {
                mult[i][j] += a[i][k] * b[k][j];
            }

    cout << endl << "Output Matrix: " << endl;
    for(i = 0; i < size; ++i)
    for(j = 0; j < size; ++j)
    {
        cout << " " << mult[i][j];
        if(j == size-1)
            cout << endl;
    }

    return 0;
}
