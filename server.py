import socket
import time
import ctypes


def lock_screen_windows():
    ctypes.windll.user32.LockWorkStation()


def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024).decode("utf-8")
        print(f"Received message from client: {data}")

        valid_student_ids = ["1200029", "1210412", "1210880"]
        if data in valid_student_ids:
            print("Valid student ID. Locking screen in 10 seconds.")

            conn.sendall(b"Locking screen in 10 seconds.\n")

            time.sleep(10)

            lock_screen_windows()

            print("Screen locked.")
        else:
            print("Invalid student ID. Error message sent to client.")
            conn.sendall(b"Error: Invalid student ID.\n")


def main():
    host = "localhost"
    port = 9955

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()

        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = s.accept()
            handle_connection(conn, addr)


main()
