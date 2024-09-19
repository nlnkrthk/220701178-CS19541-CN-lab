import random

# Function to read from Sender_Buffer
def read_from_sender_buffer():
    with open('Sender_Buffer.txt', 'r') as f:
        frames = []
        for line in f:
            frame_no, data = line.strip().split(',')
            frames.append((int(frame_no), data))
        return frames

# Function to write ACK/NACK to Receiver_Buffer
def write_to_receiver_buffer(ack):
    with open('Receiver_Buffer.txt', 'w') as f:
        f.write(f'{ack}\n')

def sliding_window_receiver():
    expected_frame = 0

    while True:
        frames = read_from_sender_buffer()
        for frame in frames:
            frame_no, data = frame
            if frame_no == expected_frame:
                print(f"Received frame {frame_no} correctly.")
                expected_frame += 1
            else:
                print(f"Received frame {frame_no} out of order. Sending NACK.")
                write_to_receiver_buffer(expected_frame)
                return

        # Simulate error in acknowledgment
        if random.random() < 0.1:  # 10% chance to induce error
            print("Inducing error in ACK")
            write_to_receiver_buffer(expected_frame - 1)
        else:
            write_to_receiver_buffer(expected_frame)
            print(f"Sending ACK for frame {expected_frame - 1}")

        time.sleep(2)  # Simulate processing delay

# Start the receiver process
sliding_window_receiver()
