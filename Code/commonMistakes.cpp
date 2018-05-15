#include <iostream>
#include "calculate.cpp"
using namespace std;

int main() {
  int first;
  int second;
  calculations x;
  // int calculate();

  cout << "Enter your numbers: " << endl;
  cin >> first >> second;

  cout << "The product is: " << x.calculate(first, second) << endl;
  return 0;
}
