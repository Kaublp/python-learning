import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1.5)
result = sock.connect_ex(("127.0.0.1", 8080))
print(f"返回值是{result}")

if result == 0:
    print("端口 8080 开放")

sock.close()