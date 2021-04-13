from threading import Thread
from queue import Queue
import socket
import time

timeout = 1.0

def check_port(host: str, port: int, results: Queue):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    if result == 0:
        results.put(port)
    sock.close()

if __name__ == '__main__':
    start = time.time()
    threads = []
    scan_range = range(80, 100)
    host = 'localhost'

    outputs = Queue()
    for port in scan_range:
        params = (host, port, outputs)
        t = Thread(target=check_port, args=params)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    while not outputs.empty():
        print(f"Port {outputs.get()} is open")

    elapsed = time.time() - start
    print(f"Completed scan in {elapsed} seconds")
