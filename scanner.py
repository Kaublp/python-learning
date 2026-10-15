import socket
from threading import Thread
from queue import Queue

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex(("127.0.0.1", port))
    if result == 0:
        print(f"返回值是{result}")
        print(f"端口{port}开放")
    sock.close()

def worker():
    while not queue.empty():
        port = queue.get()
        scan_port(port)
        queue.task_done()

queue = Queue()

for port in range (1,1001):
    queue.put(port)

for _ in range(50):
    t = Thread(target = worker)
    t.start()

queue.join()
print("扫描完成")