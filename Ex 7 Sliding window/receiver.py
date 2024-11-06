import os

def read_sender_buffer(file_path):
    """Reads the frames from Sender_Buffer.txt."""
    if not os.path.exists(file_path):
        print(f"{file_path} does not exist.")
        return []
    
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            frames = [(int(line.split()[0]), line.split()[1]) for line in lines]
            return frames
    except IOError as e:
        print(f"Error reading from file {file_path}: {e}")
        return []

def receiver_protocol(sender_file_path, receiver_file_path):
    """Processes the frames and sends ACK/NACK."""
    frames = read_sender_buffer(sender_file_path)
    if not frames:
        print("No frames to process.")
        return
    
    expected_frame_no = 0

    for frame in frames:
        print(f'Processing Frame: {frame[0]} | Data: {frame[1]}')
        if frame[0] == expected_frame_no:
            print(f'Frame {frame[0]} received correctly.')
            expected_frame_no += 1
        else:
            print(f'Error detected! Expected Frame: {expected_frame_no}, but got Frame: {frame[0]}')
            write_acknowledgement(expected_frame_no, receiver_file_path)
            return

    write_acknowledgement(expected_frame_no, receiver_file_path)
    print(f'All frames received correctly. Sending ACK: {expected_frame_no}')

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
    
    print("Receiver is running...")
    receiver_protocol(sender_file_path, receiver_file_path)
