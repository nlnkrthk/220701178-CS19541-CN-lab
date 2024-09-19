import time
import random

# Function to write frames to Sender_Buffer
def write_to_sender_buffer(frames):
    with open('Sender_Buffer.txt', 'w') as f:
        for frame in frames:
            f.write(f'{frame[0]},{frame[1]}\n')

# Function to read the Receiver_Buffer
def read_from_receiver_buffer():
    with open('Receiver_Buffer.txt', 'r') as f:
        ack = f.readline().strip()
        return int(ack)

def sliding_window_sender(window_size, message):
    frames = [(i, message[i]) for i in range(len(message))]
    window_start = 0
    window_end = min(window_size, len(frames))

    while window_start < len(frames):
        # Send frames in the current window
        current_window = frames[window_start:window_end]
        print(f"Sending frames: {current_window}")
        write_to_sender_buffer(current_window)
        time.sleep(2)  # Simulate waiting for acknowledgment

        # Read acknowledgment
        ack = read_from_receiver_buffer()
        if ack >= window_start + 1:
            print(f"Received ACK for frame {ack}")
            window_start = ack
            window_end = min(window_start + window_size, len(frames))
        else:
            print(f"Received NACK for frame {ack}")
            window_end = min(window_start + window_size, len(frames))

# Input from the user
window_size = int(input("Enter window size: "))
message = input("Enter the text message: ")

# Start the sender process
sliding_window_sender(window_size, message)
