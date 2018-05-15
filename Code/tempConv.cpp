using namespace std;
#include <iostream>

void TempConv() {
  double fahr;
  double cel;
  
  cout<<"Enter the temperature in F: ";
  cin>>fahr;
  
  cel = (fahr - 32) * 5.0/9.0;
  cout<<"The temperature in C is: "<<cel<<endl;
}

int main() {
  TempConv();
  
  return 0;
}
