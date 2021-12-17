import logging
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable, Iterable, List

import psutil


def start_server(hostname: str, f: str, num_clients: int):
    execute_on_host(
        hostname,
        f"""
            cd server

            cd Python-3.9.1
            alias python=`pwd`/python
            cd -  

            python -m venv --copies .env
            source .env/bin/activate
            python -m pip install --upgrade pip
            python -m pip install -r requirements.txt

            source .env/bin/activate

            {'python headless_client.py ws://127.0.0.1:7700 &' * num_clients}

            cd benchmarks
            python {f} {num_clients} 
        """,
    )


def parallel_map(
    function: Callable[[Any], Any],
    values: Iterable[Any],
    concurrency=psutil.cpu_count(),
    chunk_size=10000,
) -> List[Any]:
    values = list(values)

    with ThreadPoolExecutor(max_workers=concurrency) as p:
        return p.map(function, values, chunksize=chunk_size)


def run_command(command: str) -> str:
    logging.info(f"Executing: {command}")

    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    result = ""
    for c in iter(lambda: process.stdout.read(1), b""):
        sys.stdout.buffer.write(c)
        sys.stdout.buffer.flush()
        result += c.decode("utf-8", errors="ignore")

    return result.strip()


def execute_on_host(hostname: str, script: str) -> str:
    return run_command(f"ssh {hostname} <<\EOD\n{script}\nEOD")
