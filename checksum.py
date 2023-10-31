### Part 2 of lab
## Part 2a
# Write a program that generates an 8-bit CRC checksum for a data stream.
# An example of this program follows, in pseudocode.
# This same program may be used to check correct reception of the data stream.
# The simplest data stream for which this may be used is two bytes;
# simulate at least 5 different 2-byte data streams both with and without errors and log the results.
# Particularly interesting are error data streams which differ by only 1 bit from the correct data.
## Part 2b
# Also, simulate at least one 32-byte data stream with at least one error and log the results.
# Include a screenshot of the results and discuss the probability of an undetected error occurring
import crcmod
import random

# Define the CRC algorithm (8-bit)
crc8 = crcmod.mkCrcFun(0x131, rev=True, initCrc=0, xorOut=0)

# Input data (as a byte string)
data_1 = bytearray([0x10, 0x20]) 
data_2 = bytearray([0x11, 0x21]) 
data_3 = bytearray([0x12, 0x22]) 
data_4 = bytearray([0x13, 0x23]) 
data_5 = bytearray([0x64, 0x28]) 

# Generate random data for 32 byte data stream
list = []
for i in range(32):
    list.append(random.randint(0, 255))
data_6 = bytearray(list)
    
# Generate random data for 32 byte data stream
list_2 = []
for i in range(32):
    list_2.append(random.randint(0, 255))
data_7 = bytearray(list_2)

# Create list of all data streams for ease of use
two_byte_list = [data_1, data_2, data_3, data_4, data_5]
thirty_two_byte_list = [data_6, data_7]

# Count the number of bit differences between two byte arrays
def count_binary_differences(byte_array1, byte_array2):
    if len(byte_array1) != len(byte_array2):
        raise ValueError("Both byte arrays must have the same length")

    differences = 0

    for byte1, byte2 in zip(byte_array1, byte_array2):
        xor_result = byte1 ^ byte2
        differences += bin(xor_result).count('1')

    return differences


def main():
    # Run CRC algorithm on each 2-byte data stream
    for i in range(len(two_byte_list)):
        print("Data Streams: 1 & " + str(i + 1))
        print("Input Data In Hexadecimal:")
        print(", ".join(f"{hex(b)}" for b in two_byte_list[0]))
        print("Output Data In Hexadecimal:")
        print(", ".join(f"{hex(b)}" for b in two_byte_list[i]))
        print("\nInput Data In Binary:")
        print(", ".join(f"{b:08b}" for b in two_byte_list[0]))
        print("Output Data In Binary:")
        print(", ".join(f"{b:08b}" for b in two_byte_list[i]))
        print(f"\nNumber of Bit Errors: {count_binary_differences(two_byte_list[0], two_byte_list[i])}")
        print(f"\n8-bit CRC Checksum for Input Data: 0x{crc8(two_byte_list[0]):02X}")
        print(f"8-bit CRC Checksum for Output Data: 0x{crc8(two_byte_list[i]):02X}\n")
    
    # Run CRC algorithm on each 32-byte data stream
    for i in range(len(thirty_two_byte_list)):
        print("Data Streams: 1 & " + str(i + 1))
        print("Input Data In Hexadecimal:")
        print(", ".join(f"{hex(b)}" for b in thirty_two_byte_list[0]))
        print("Output Data In Hexadecimal:")
        print(", ".join(f"{hex(b)}" for b in thirty_two_byte_list[i]))
        print("\nInput Data In Binary:")
        print(", ".join(f"{b:08b}" for b in thirty_two_byte_list[0]))
        print("Output Data In Binary:")
        print(", ".join(f"{b:08b}" for b in thirty_two_byte_list[i]))
        print(f"\nNumber of Bit Errors: {count_binary_differences(thirty_two_byte_list[0], thirty_two_byte_list[i])}")
        print(f"\n8-bit CRC Checksum for Input Data: 0x{crc8(thirty_two_byte_list[0]):02X}")
        print(f"8-bit CRC Checksum for Output Data: 0x{crc8(thirty_two_byte_list[i]):02X}\n")
        


if __name__ == "__main__":
    main()