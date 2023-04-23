#include <stdio.h>
#include <stdlib.h>

int main(){
    char* arr = (char *)malloc(sizeof(char) *4);
    free(arr);
    printf("%c\n",arr[0]);
    return 0;
}