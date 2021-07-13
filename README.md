Install python 3.8+ version

install mbed-cli https://os.mbed.com/docs/mbed-os/v6.8/build-tools/install-and-set-up.html

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
