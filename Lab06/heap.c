#include <stdio.h>
#include <stdlib.h>

int main(){
    char* arr = malloc(4);
    arr[6] = 'a'; // out-of-bounds access
    printf("%c\n",arr[6]);
    free(arr);
    return 0;
}