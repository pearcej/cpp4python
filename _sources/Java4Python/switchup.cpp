#include <iostream>
using namespace std;

int main() {

  int grade = 85;

  int tempgrade = grade / 10;
  switch(tempgrade) {
  case 10:
  case 9:
      cout<<'A'<<endl;
      break;
  case 8:
      cout<<'B'<<endl;
      break;
  case 7:
      cout<<'C'<<endl;
      break;
  case 6:
      cout<<'A'<<endl;
      break;
  default:
      cout<<'F'<<endl;
  }

  return 0;
}
