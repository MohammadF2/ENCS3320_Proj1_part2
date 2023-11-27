import socket


def main():
    host = "localhost"
    port = 9955

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        student_id = "123"

        s.sendall(student_id.encode("utf-8"))

        data = s.recv(1024)
        print(f"Server response: {data.decode('utf-8')}")


main()
