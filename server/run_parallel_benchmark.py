import sys
from time import sleep

from helper import run_command, start_server

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print(
            "Usage: python3 run_parallel_benchmark.py <benchmarking_file_name> <number_clients>"
        )
        exit()

    cwd = run_command("pwd")

    run_command(f"preserve -# 1 -t 00:15:00")

    while True:
        result = run_command("preserve -llist | grep $USER")
        cells = result.split()
        if cells[-1] != "-":
            nodes = cells[-node_count:]
            break
        sleep(2)

    print("Nodes: ", nodes)

    master = nodes[-1]

    start_server(master, sys.argv[1], int(sys.argv[2]))
