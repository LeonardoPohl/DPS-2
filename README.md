# Nitocris - a distributed data processing system

> [Documentation](docs/report.pdf)

## Build

```sh
./initialize.sh
```

> Have yarn (Node), Python (version 3.8<) installed

## Run

### Start the execution

```sh
cd server
source .env/bin/activate
cd benchmarks
python3 test-vec.py
```

### Open the client

Go to [http://0.0.0.0:7701](http://0.0.0.0:7701) in your browser of choice.

## Install modern Python without root privileges

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

> Useful on DAS-5
