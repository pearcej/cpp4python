#include <iostream>
using namespace std;

int main() {
  int nums[] = {1,3,6,2,5};

    int numsSize = sizeof(nums)/sizeof(nums[0]); // Get size of the nums array

    for (int index=0; index<numsSize; index++) {
        cout<<nums[index]<<endl;
    }

    // Simpler Implementation that may only work in
    // Newer versions of C++

    // for (int item:nums) {
    //     cout<<item<<endl;
    // }

  return 0;
}
