import random

### Part 2 of lab

## Part 2a
# *Write a program that generates an 8-bit CRC checksum for a data stream.
# An example of this program follows, in pseudocode.
# This same program may be used to check correct reception of the data stream.
# The simplest data stream for which this may be used is two bytes;
# simulate at least 5 different 2-byte data streams both with and without errors and log the results.
# Particularly interesting are error data streams which differ by only 1 bit from the correct data.

def genBytes(num):
    data = ''
    for n in range (num):
        byte = ''
        for i in range (8):
            bit = random.randint(0,1)
            byte += str(bit)
        data += byte
    return data

def genCRC(data):
    # Initialize everything:
    data_array = list(data)
    for n in range(len(data_array)):
        data_array[n] = int(data_array[n])

    next = []
    present = []
    for n in range(8):
        next.append(0)
        present.append(0)

    # Run circuit
    for n in range(len(data)):
        next[0] = data_array.pop()
        next[1] = present[0]
        next[2] = present[1] ^ present[7]
        next[3] = present[2] ^ present[7]
        next[4] = present[3] ^ present[7]
        next[5] = present[4]
        next[6] = present[5]
        next[7] = present[6]
        present = next.copy()

    for n in range(len(present)):
        present[n] = str(present[n])

    present = "".join(present)

    return present

def genErrors(data, num_errors):
    corrupt_data = list(data)
    error_locations = random.sample(range(0,len(data)), num_errors)
    for i in error_locations:
        corrupt_data[i] = '1' if corrupt_data[i] == '0' else '0'
    corrupt_data = "".join(corrupt_data)
    return corrupt_data


## Part 2b
# Also, simulate at least one 32-byte data stream with at least one error and log the results.
# Include a screenshot of the results and discuss the probability of an undetected error occurring

#### Main function to kick off the whole program.
def main():
    print("Part 2a: ")
    for n in range (5):
        datastream = genBytes(2)
        crc = genCRC(datastream)
        # num_errors = random.randint(0,2)
        received_datastream = genErrors(datastream, n)
        received_crc = genCRC(received_datastream)

        print("  Run " + str(n+1) + " with " + str(n) + " error(s)")
        print("    Transmitted Data:  ", end="")
        print(datastream + " / " + str(hex(int(datastream,2))))
    
        print("    Received Data:     ", end="")
        print(received_datastream + " / " + str(hex(int(received_datastream,2))))

        print("    Transmitted CRC:   ", end="")
        print(str(crc) + " / " + str(hex(int(crc,2))))

        print("    Received CRC:      ", end="")
        print(str(received_crc) + " / " + str(hex(int(received_crc,2))))

        print("")
    print("")

    print("Part 2b: ")
    for n in range (3):
        datastream = genBytes(32)
        crc = genCRC(datastream)
        # num_errors = random.randint(0,2)
        received_datastream = genErrors(datastream, n)
        received_crc = genCRC(received_datastream)

        print("  Run " + str(n+1) + " with " + str(n) + " error(s)")
        print("    Transmitted Data:  ", end="")
        print(hex(int(datastream,2)))
    
        print("    Received Data:     ", end="")
        print(hex(int(received_datastream,2)))

        print("    Transmitted CRC:   ", end="")
        print(str(crc) + " / " + str(hex(int(crc,2))))

        print("    Received CRC:      ", end="")
        print(str(received_crc) + " / " + str(hex(int(received_crc,2))))

        print("")
        

if __name__ == "__main__":
    main()