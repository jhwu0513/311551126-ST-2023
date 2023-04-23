#include <stdio.h>
#include <stdlib.h>

int main(){
    int a[8] = {0},b[8] = {1};
    printf("%ld\n",b-a); // 相減後得到16，表示b跟a的位址相差16個int = 64 bytes = 32 bytes of a + 32 bytes of redzone
    printf("%d\n",a[(b-a)]);
    return 0;
}