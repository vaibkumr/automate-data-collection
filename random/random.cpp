#include <stdafx.h>
# include <iostream>
# include <ctime>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
int number;

srand(50);
//sets the numbers to 50

cout<<"What is the range of numbers you would like to use?"<<endl;
cin>>number;
cin.ignore();

cout<<"The numbers are:"<<endl;

for(int i=1;i<50; i++)
{
cout<<rand()%number<<endl;
// number is used to represent the range
}
cin.get();
return 0;
}
