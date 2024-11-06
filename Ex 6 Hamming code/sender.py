def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def add_parity_bits(data):
    n = len(data)
    r = 1
    while 2**r < n + r + 1:
        r += 1

    hamming_code = list('0' * (n + r))
    j = 0
    for i in range(1, n + r + 1):
        if i == 2**j:
            j += 1
        else:
            hamming_code[i - 1] = data[i - j - 1]
    
    for i in range(r):
        parity_index = 2**i - 1
        parity_value = 0
        for j in range(1, len(hamming_code) + 1):
            if j & (parity_index + 1):
                parity_value ^= int(hamming_code[j - 1])
        hamming_code[parity_index] = str(parity_value)
    
    return ''.join(hamming_code)

def main():
    input_text = input("Enter text to send: ")
    binary_data = text_to_binary(input_text)
    hamming_code = add_parity_bits(binary_data)
    
    with open('channel.txt', 'w') as channel_file:
        channel_file.write(hamming_code)
    
    print("Data sent and saved to channel.txt")

if __name__ == "__main__":
    main()
