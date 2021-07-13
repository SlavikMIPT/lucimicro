Install python 3.8+ version

install mbed-cli https://os.mbed.com/docs/mbed-os/v6.8/build-tools/install-and-set-up.html

Install Cmake version 3.19.0 or newer https://cmake.org/download/

Install Ninja version 1.0.0 or newer sudo apt-get install ninja-build

Install GNU Arm Embedded Compiler version 9 https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads

```bash
python import_lib.py
```
```bash
cd ONE
git apply ../one.patch
cd ..
```
```bash
cd mbed-os
git apply ../mbed-os.patch
cd ..
```
```bash
mbed-tools compile -m NUCLEO_F746ZG -t GCC_ARM
```
