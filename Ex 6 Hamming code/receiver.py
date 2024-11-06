def check_and_correct(data):
    n = len(data)
    r = 0
    while 2**r < n + 1:
        r += 1

    error_position = 0
    for i in range(r):
        parity_index = 2**i - 1
        parity_value = 0
        for j in range(1, n + 1):
            if j & (parity_index + 1):
                parity_value ^= int(data[j - 1])
        if parity_value != 0:
            error_position += 2**i

    if error_position > 0:
        print(f"Error detected at position: {error_position}")
        data = list(data)
        data[error_position - 1] = '0' if data[error_position - 1] == '1' else '1'
        data = ''.join(data)

    corrected_data = []
    j = 0
    for i in range(1, n + 1):
        if i != 2**j:
            corrected_data.append(data[i - 1])
        else:
            j += 1

    return ''.join(corrected_data)

def binary_to_text(binary_data):
    ascii_chars = [chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8)]
    return ''.join(ascii_chars)

def main():
    with open('channel.txt', 'r') as channel_file:
        hamming_code = channel_file.read()

    corrected_binary_data = check_and_correct(hamming_code)
    text_output = binary_to_text(corrected_binary_data)
    
    print("Received text:", text_output)

if __name__ == "__main__":
    main()
