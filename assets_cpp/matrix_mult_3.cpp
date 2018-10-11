#include <iostream>
using namespace std;

int main()
{
  int size = 3;

  int a[3][3] = {{2,0,1},{0,0,0},{1,1,2}};
  int b[3][3] = {{1,1,2},{1,2,0},{0,0,1}};
  int mult[3][3] = {{0,0,0},{0,0,0},{0,0,0}};
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
