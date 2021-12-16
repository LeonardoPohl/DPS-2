# Nitocris - a distributed processing system

In ancient Egypt, it is believed that Pharaoh Nitocris ruled at the end of the 6th Dynasty from 2182 to 2179 BC. It is believed that she built the smallest pyramid, the third pyramid at Giza. To achieve that, she needed people to help her accomplish that task. Similarly, we try to achieve a big goal by distributing the work. Another similarity is that we are, as of yet, not aiming to build the greatest pyramids.

This is the Repository, which contains the codebase of what we are planning to become a python package. Nitocris is planned to be a p2p processing system. Our main idea is that python code is run on one computer, server or even thin client.

The workload is intended to be a map function. This function is then pickled and compiled into web assembly. A link is then created, which allows any device, which has access to internet to contribute with compute resources.

## Install python without root privileges

```sh
wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz
tar -xf Python-3.9.1.tgz
cd Python-3.9.1
./configure --enable-optimizations
make -j 8
wget https://bootstrap.pypa.io/get-pip.py
./python get-pip.py --user
cd -
```
