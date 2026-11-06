#include<stdio.h>
#include<iostream>
using namespace std;

class Solution {
public:
    int numberOfStableArrays(int zero, int one, int limit) {
        int size = zero + one;
        int arr[size];
        for(int i=0;i<size;i++){
            arr[i] = 0;
        }
        int count = 0;
        count = stableArray(zero,one,size,count,arr);
        return count;
    }

    int stableArray(int zero, int one, int size, int count,int arr[]){
        if(size < 0){
            return count;
        }
        arr[size-1] = 1;
        if(isStable(zero,one,size,arr))
        return 1;
        return count+max(stableArray(zero,one,size-1,count,arr),stableArray(zero,one,size,count,arr));
    }

    bool isStable(int zero,int one,int size, int arr[]){
        int countZero = 0;
        int countOne = 0;
        for(int i=0;i<size;i++){
            if(arr[i]==0){
                countZero++;
            }else{
                countOne++;
            }
            if(countZero>zero)
            return false;
            if(countOne>one)
            return false;
        }
        return true;
    }
};

int main(){
    Solution s;
    int zero = 2;
    int one = 1;
    int limit = 3;
    cout<<s.numberOfStableArrays(zero,one,limit)<<endl;
}