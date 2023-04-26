#include <stdio.h>
#include <stdlib.h>

int main(){
    int arr[5] = {1, 2, 3, 4, 5};
    arr[5] = 6;
    printf("%d\n",arr[5]);
    return 0;
}