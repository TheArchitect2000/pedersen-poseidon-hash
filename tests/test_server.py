import socket

def test_server_helo():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 10000))
    client.sendall(b"HELO\n")
    response = client.recv(1024).decode().strip()
    assert response == "OK", f"Expected 'OK', but got {response}"
    client.close()