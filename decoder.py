import random
import sys

SPECIAL_SECRET_ARRAY = [
    0x11, 0x22, 0x4, 0x8, -0x67, 0x4, 0x24, 0x16, 0x4, -0x56, -0x45, -0x34, -0x10,
    0x60, 0x61, -0x33, -0x31, -0x80, 0x35, 0x2a
]

def decrypt1(array, rand_num):
    for i in range(len(array)):
        array[i] ^= rand_num
    return array

def decrypt2(array):
    startpos = 4
    secret_array_length = len(SPECIAL_SECRET_ARRAY)
    for i in range(startpos, len(array)):
        # Ensure the index is within the range of SPECIAL_SECRET_ARRAY
        index = (i - startpos) % secret_array_length
        array[i] ^= SPECIAL_SECRET_ARRAY[index]
    return array


def unreversal(array):
    v0 = 2
    v1 = len(array) - 1
    while v0 <= v1:
        tmp = array[v0]
        array[v0] = array[v1]
        array[v1] = tmp
        v0 += 1
        v1 -= 1
    return array

def hex_string_to_int_list(hex_string):
    # Strip off the "0x" prefix if present
    if hex_string.startswith("0x"):
        hex_string = hex_string[2:]
    
    # Convert each pair of hex digits to an integer
    return [int(hex_string[i:i+2], 16) for i in range(0, len(hex_string), 2)]

def decoder(encoded_hex_string):
    # Convert the hex string to a list of integers
    encoded_array = hex_string_to_int_list(encoded_hex_string)

    # Continue with the rest of the decoding process
    encoded_array = unreversal(encoded_array)

    # Extract the random integer and remove the CRC checksum
    rand_int = encoded_array[23]
    encoded_array = encoded_array[:-2]

    # Decryption 2
    encoded_array = decrypt2(encoded_array)

    # Decryption 1
    encoded_array = decrypt1(encoded_array, rand_int)

    # Extract the original data
    original_data = encoded_array[13:23]  # Adjust indices as needed
    return original_data

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 decoder.py <encoded_hex_string>")
        sys.exit(1)

    encoded_data = sys.argv[1]
    decoded_data = decoder(encoded_data)
    print(decoded_data)
