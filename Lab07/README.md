# Lab07

## PoC
Link : [Click](https://github.com/jhwu0513/311551126-ST-2023/tree/main/Lab07/out/crashes)
## The commands (steps) that you used in this lab
### Build AFL
```=
git clone https://github.com/google/AFL.git
cd AFL
make
sudo make install
```
### Fuzzing
```=
cd Lab07
export CC=~/AFL/afl-gcc
export AFL_USE_ASAN=1
make
mkdir in
cp test.bmp in/
~/AFL/afl-fuzz -i in -o out -m none -- ./bmpgrayscale @@ a.bmp
```
### ASAN report
```=
./bmpgrayscale out/crashes/id:000000* a.bmp
```

## Screenshot of AFL running (with triggered crash)
![](https://i.imgur.com/6n8mOFZ.png)

## Screenshot of crash detail (with ASAN error report)
![](https://i.imgur.com/LFuEyzC.png)
