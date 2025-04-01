#include <algorithm>
#include <queue>
#include <iostream>

using namespace std;

int n = 8;
int arr[8] = {1, 2, 3, 4, 4, 6, 7, 8};

int actual_diff = 0;
int count = 0;
int out = 1;
int diff = 0;

for(int i = 0; i<n; i++){
    diff = arr[i+1] - arr[i];
    actual_diff = diff;
    if(count==2){
        actual_diff = diff;
    }
    if(diff==actual_diff){
        count += 1;
    }
    else{
        out = i+1;
    }

}

printf("%d", out);