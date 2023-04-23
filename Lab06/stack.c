#include <stdio.h>
#include <stdlib.h>

int main(){
    char arr[5] = {'1', '2', '3', '4', '5'};
    arr[5] = '0';
    printf("%c\n",arr[5]);
    return 0;
}