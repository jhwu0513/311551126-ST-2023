# Lab06 Report

### Heap out-of-bounds read/write
Code
```
#include <stdio.h>
#include <stdlib.h>

int main(){
    char* arr = malloc(4);
    arr[6] = 'a'; // out-of-bounds access
    printf("%c\n",arr[6]);
    free(arr);
    return 0;
}
```
ASan report
```
=================================================================
==1485==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x602000000016 at pc 0x55812a600a8c bp 0x7ffeae356bb0 sp 0x7ffeae356ba0
WRITE of size 1 at 0x602000000016 thread T0
    #0 0x55812a600a8b in main /home/jhwu/Lab06.c:6
    #1 0x7f9cbbdc2c86 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21c86)
    #2 0x55812a600959 in _start (/home/jhwu/heap+0x959)

0x602000000016 is located 2 bytes to the right of 4-byte region [0x602000000010,0x602000000014)
allocated by thread T0 here:
    #0 0x7f9cbc270b40 in __interceptor_malloc (/usr/lib/x86_64-linux-gnu/libasan.so.4+0xdeb40)
    #1 0x55812a600a4b in main /home/jhwu/Lab06.c:5
    #2 0x7f9cbbdc2c86 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21c86)

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/jhwu/Lab06.c:6 in main
Shadow bytes around the buggy address:
  0x0c047fff7fb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c047fff8000: fa fa[04]fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8010: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8020: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==1485==ABORTING
```

Valgrind report
```
==965== Memcheck, a memory error detector
==965== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==965== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info
==965== Command: ./a.out
==965== 
==965== Invalid write of size 1
==965==    at 0x1086F8: main (in /home/jhwu/a.out)
==965==  Address 0x522f046 is 2 bytes after a block of size 4 alloc'd
==965==    at 0x4C31B0F: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==965==    by 0x1086EB: main (in /home/jhwu/a.out)
==965== 
==965== Invalid read of size 1
==965==    at 0x108703: main (in /home/jhwu/a.out)
==965==  Address 0x522f046 is 2 bytes after a block of size 4 alloc'd
==965==    at 0x4C31B0F: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==965==    by 0x1086EB: main (in /home/jhwu/a.out)
==965== 
a
==965== 
==965== HEAP SUMMARY:
==965==     in use at exit: 0 bytes in 0 blocks
==965==   total heap usage: 2 allocs, 2 frees, 1,028 bytes allocated
==965== 
==965== All heap blocks were freed -- no leaks are possible
==965== 
==965== For counts of detected and suppressed errors, rerun with: -v
==965== ERROR SUMMARY: 2 errors from 2 contexts (suppressed: 0 from 0)
```

Compiler : GCC 
Version : gcc version 7.5.0
ASan : 可以
Valgrind : 可以

### Stack out-of-bounds read/write
Code
```
#include <stdio.h>
#include <stdlib.h>

int main(){
    int arr[5] = {1, 2, 3, 4, 5};
    arr[6] = 10;
    printf("%d\n",arr[6]);
    return 0;
}
```
ASan report
```
=================================================================
==1996==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7fff8adb71e8 at pc 0x563035800c67 bp 0x7fff8adb71a0 sp 0x7fff8adb7190
WRITE of size 4 at 0x7fff8adb71e8 thread T0
    #0 0x563035800c66 in main /home/jhwu/Lab06/stack.c:6
    #1 0x7fc017cd4c86 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21c86)
    #2 0x563035800999 in _start (/home/jhwu/Lab06/stack+0x999)

Address 0x7fff8adb71e8 is located in stack of thread T0 at offset 56 in frame
    #0 0x563035800a89 in main /home/jhwu/Lab06/stack.c:4

  This frame has 1 object(s):
    [32, 52) 'arr' <== Memory access at offset 56 overflows this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism or swapcontext
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow /home/jhwu/Lab06/stack.c:6 in main
Shadow bytes around the buggy address:
  0x1000715aede0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1000715aedf0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1000715aee00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1000715aee10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1000715aee20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x1000715aee30: 00 00 00 00 00 00 f1 f1 f1 f1 00 00 04[f2]00 00
  0x1000715aee40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1000715aee50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1000715aee60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1000715aee70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1000715aee80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==1996==ABORTING
```
Valgrind report
```
==1936== Memcheck, a memory error detector
==1936== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==1936== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info
==1936== Command: ./stack
==1936== 
10
*** stack smashing detected ***: <unknown> terminated
==1936== 
==1936== Process terminating with default action of signal 6 (SIGABRT)
==1936==    at 0x4E7CE87: raise (raise.c:51)
==1936==    by 0x4E7E7F0: abort (abort.c:79)
==1936==    by 0x4EC7836: __libc_message (libc_fatal.c:181)
==1936==    by 0x4F72B30: __fortify_fail_abort (fortify_fail.c:33)
==1936==    by 0x4F72AF1: __stack_chk_fail (stack_chk_fail.c:29)
==1936==    by 0x108719: main (in /home/jhwu/Lab06/stack)
==1936== 
==1936== HEAP SUMMARY:
==1936==     in use at exit: 0 bytes in 0 blocks
==1936==   total heap usage: 1 allocs, 1 frees, 1,024 bytes allocated
==1936== 
==1936== All heap blocks were freed -- no leaks are possible
==1936== 
==1936== For counts of detected and suppressed errors, rerun with: -v
==1936== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```

Compiler : GCC 
Version : gcc version 7.5.0
ASan : 可以
Valgrind : 可以

### Global out-of-bounds read/write
Code 
```
#include <stdio.h>
#include <stdlib.h>

int arr[5] = {1, 2, 3, 4, 5};

int main(){
    arr[5] = 10; // out-of-bounds write
    printf("%d\n",arr[5]); // out-of-bounds read
    return 0;
}
```
ASan report
```
=================================================================
==2339==ERROR: AddressSanitizer: global-buffer-overflow on address 0x5555af001034 at pc 0x5555aee00a28 bp 0x7ffd07b4b4c0 sp 0x7ffd07b4b4b0
WRITE of size 4 at 0x5555af001034 thread T0
    #0 0x5555aee00a27 in main /home/jhwu/Lab06/global.c:7
    #1 0x7f9fcd91bc86 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21c86)
    #2 0x5555aee00909 in _start (/home/jhwu/Lab06/global+0x909)

0x5555af001034 is located 0 bytes to the right of global variable 'arr' defined in 'global.c:4:5' (0x5555af001020) of size 20
SUMMARY: AddressSanitizer: global-buffer-overflow /home/jhwu/Lab06/global.c:7 in main
Shadow bytes around the buggy address:
  0x0aab35df81b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0aab35df81c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0aab35df81d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0aab35df81e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0aab35df81f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0aab35df8200: 00 00 00 00 00 00[04]f9 f9 f9 f9 f9 00 00 00 00
  0x0aab35df8210: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0aab35df8220: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0aab35df8230: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0aab35df8240: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0aab35df8250: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==2339==ABORTING
```
Valgrind report
```
==2305== Memcheck, a memory error detector
==2305== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==2305== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info
==2305== Command: ./global
==2305== 
10
==2305== 
==2305== HEAP SUMMARY:
==2305==     in use at exit: 0 bytes in 0 blocks
==2305==   total heap usage: 1 allocs, 1 frees, 1,024 bytes allocated
==2305== 
==2305== All heap blocks were freed -- no leaks are possible
==2305== 
==2305== For counts of detected and suppressed errors, rerun with: -v
==2305== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```

Compiler : GCC 
Version : gcc version 7.5.0
ASan : 可以
Valgrind : 不行


### Use-after-free

Code
```
#include <stdio.h>
#include <stdlib.h>

int main(){
    char* arr = (char *)malloc(sizeof(char) *4);
    free(arr);
    printf("%c\n",arr[0]);
    return 0;
}
```

ASan report
```
=================================================================
==2743==ERROR: AddressSanitizer: heap-use-after-free on address 0x602000000010 at pc 0x555e62400a40 bp 0x7ffea5670830 sp 0x7ffea5670820
READ of size 1 at 0x602000000010 thread T0
    #0 0x555e62400a3f in main /home/jhwu/Lab06/uaf.c:7
    #1 0x7f17c7f2fc86 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21c86)
    #2 0x555e62400909 in _start (/home/jhwu/Lab06/uaf+0x909)

0x602000000010 is located 0 bytes inside of 4-byte region [0x602000000010,0x602000000014)
freed by thread T0 here:
    #0 0x7f17c83dd7a8 in __interceptor_free (/usr/lib/x86_64-linux-gnu/libasan.so.4+0xde7a8)
    #1 0x555e62400a0b in main /home/jhwu/Lab06/uaf.c:6
    #2 0x7f17c7f2fc86 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21c86)

previously allocated by thread T0 here:
    #0 0x7f17c83ddb40 in __interceptor_malloc (/usr/lib/x86_64-linux-gnu/libasan.so.4+0xdeb40)
    #1 0x555e624009fb in main /home/jhwu/Lab06/uaf.c:5
    #2 0x7f17c7f2fc86 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21c86)

SUMMARY: AddressSanitizer: heap-use-after-free /home/jhwu/Lab06/uaf.c:7 in main
Shadow bytes around the buggy address:
  0x0c047fff7fb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c047fff8000: fa fa[fd]fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8010: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8020: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==2743==ABORTING
```

Valgrind report
```
==2649== Memcheck, a memory error detector
==2649== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==2649== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info
==2649== Command: ./uaf
==2649== 
==2649== Invalid read of size 1
==2649==    at 0x108700: main (in /home/jhwu/Lab06/uaf)
==2649==  Address 0x522f040 is 0 bytes inside a block of size 4 free'd
==2649==    at 0x4C32D3B: free (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==2649==    by 0x1086FB: main (in /home/jhwu/Lab06/uaf)
==2649==  Block was alloc'd at
==2649==    at 0x4C31B0F: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==2649==    by 0x1086EB: main (in /home/jhwu/Lab06/uaf)
==2649== 

==2649== 
==2649== HEAP SUMMARY:
==2649==     in use at exit: 0 bytes in 0 blocks
==2649==   total heap usage: 2 allocs, 2 frees, 1,028 bytes allocated
==2649== 
==2649== All heap blocks were freed -- no leaks are possible
==2649== 
==2649== For counts of detected and suppressed errors, rerun with: -v
==2649== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
```

Compiler : GCC 
Version : gcc version 7.5.0
ASan : 可以
Valgrind : 可以

### Use-after-return
Code 
```
#include <stdio.h>
#include <stdlib.h>

int *ptr;
void FunctionThatEscapesLocalObject() {
  int local[100];
  ptr = &local[0];
}

int main(int argc, char **argv) {
  FunctionThatEscapesLocalObject();
  return ptr[argc];
}
```

ASan report
```
=================================================================
==4007==ERROR: AddressSanitizer: stack-use-after-return on address 0x7f73f7300024 at pc 0x565165c00adc bp 0x7ffeea4501b0 sp 0x7ffeea4501a0
READ of size 4 at 0x7f73f7300024 thread T0
    #0 0x565165c00adb in main /home/jhwu/Lab06/uar.c:12
    #1 0x7f73faf8ec86 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21c86)
    #2 0x565165c00839 in _start (/home/jhwu/Lab06/uar+0x839)

Address 0x7f73f7300024 is located in stack of thread T0 at offset 36 in frame
    #0 0x565165c00929 in FunctionThatEscapesLocalObject /home/jhwu/Lab06/uar.c:5

  This frame has 1 object(s):
    [32, 432) 'local' <== Memory access at offset 36 is inside this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism or swapcontext
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-use-after-return /home/jhwu/Lab06/uar.c:12 in main
Shadow bytes around the buggy address:
  0x0feefee57fb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0feefee57fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0feefee57fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0feefee57fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0feefee57ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0feefee58000: f5 f5 f5 f5[f5]f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5
  0x0feefee58010: f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5
  0x0feefee58020: f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5 f5
  0x0feefee58030: f5 f5 f5 f5 f5 f5 f5 f5 00 00 00 00 00 00 00 00
  0x0feefee58040: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0feefee58050: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==4007==ABORTING
```

Valgrind report
```
==4104== Memcheck, a memory error detector
==4104== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==4104== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info
==4104== Command: ./uar
==4104== 
==4104== Invalid read of size 4
==4104==    at 0x1086D6: main (in /home/jhwu/Lab06/uar)
==4104==  Address 0x1ffefff724 is on thread 1's stack
==4104==  428 bytes below stack pointer
==4104== 
==4104== 
==4104== HEAP SUMMARY:
==4104==     in use at exit: 0 bytes in 0 blocks
==4104==   total heap usage: 0 allocs, 0 frees, 0 bytes allocated
==4104== 
==4104== All heap blocks were freed -- no leaks are possible
==4104== 
==4104== For counts of detected and suppressed errors, rerun with: -v
==4104== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
```

Compiler : GCC 
Version : gcc version 7.5.0
ASan : 可以，但ASan預設是沒有開啟 stack-use-after-return 的偵測，需要在全域變數內設定 ASAN_OPTIONS
$ export ASAN_OPTIONS=detect_stack_use_after_return=1
Valgrind : 可以

### Bypass ASan

Code
```
#include <stdio.h>
#include <stdlib.h>

int main(){
    int a[8] = {0},b[8] = {1};
    printf("%ld\n",b-a); // 相減後得到16，表示b跟a的位址相差16個int = 64 bytes = 32 bytes of a + 32 bytes of redzone
    printf("%d\n",a[(b-a)]);
    return 0;
}
```

ASan output
```
$ gcc -fsanitize=address -g bypassAsan.c -o bypassAsan
$ ./bypassAsan 
16
1
```
Compiler : GCC 
Version : gcc version 7.5.0
ASan : 不行，由於redzone檢查機制只在變數的前後加redzone，而redzone為32 bytes，所以只要跳過a:32 bytes + redzone:32bytes = 64 bytes = 16 int就可以存取b[0]