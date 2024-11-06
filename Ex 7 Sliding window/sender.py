import time
import os

def send_frames(frames, window_size, file_path):
    """Writes frames to the Sender_Buffer.txt file."""
    try:
        with open(file_path, 'w') as f:
            for frame in frames[:window_size]:
                f.write(f'{frame[0]} {frame[1]}\n')
                print(f'Writing Frame: {frame[0]} | Data: {frame[1]} to Sender_Buffer.txt')
                time.sleep(1)  # Simulate delay
    except IOError as e:
        print(f"Error writing to file {file_path}: {e}")

def write_acknowledgement(ack_num, file_path):
    """Writes the acknowledgment number to Receiver_Buffer.txt."""
    try:
        with open(file_path, 'w') as f:
            f.write(str(ack_num))
        print(f'ACK updated to: {ack_num}')
    except IOError as e:
        print(f"Error writing to file {file_path}: {e}")

if __name__ == "__main__":
    sender_file_path = "C:\\Users\\Jessielyn Jenisha\\Documents\\Sem 5\\CN\\Sliding Window\\Sender_Buffer.txt"
    receiver_file_path = "C:\\Users\\Jessielyn Jenisha\\Documents\\Sem 5\\CN\\Sliding Window\\Receiver_Buffer.txt"
    
    window_size = int(input("Enter the window size: "))
    message = input("Enter the text message: ")

    # Simulate sending frames
    frames = [(i, ch) for i, ch in enumerate(message)]
    send_frames(frames, window_size, sender_file_path)
    
    # Simulate writing acknowledgment
    write_acknowledgement(0, receiver_file_path)
