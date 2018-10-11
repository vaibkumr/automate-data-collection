#include <iostream>
using namespace std;

int main()
{
  int size = SIZE;
  long long a[SIZE][SIZE] = ARRAY_1;
  long long b[SIZE][SIZE] = ARRAY_2;
  long long mult[SIZE][SIZE] = RESULT;
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
