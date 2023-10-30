import random

# Part 1 of lab: Parity

## Part 1a
#### genByte will generate a byte of 8 bits, and return them as a list.
def genByte():
    byte = []
    for i in range (8):
        bit = random.randint(0,1)
        byte.append(bit)
    return byte

#### genParity will generate an even parity bit from a passed list, and return the bit.
def genParity(byte):
    occurences = byte.count(1)
    parity_bit = occurences % 2
    return parity_bit
   


## Part 1b
#### corruptByte will take a given byte, and flip the passed number (num_errors) of random bits.
def corruptByte(byte, num_errors):
    corrupt_byte = byte.copy()
    error_locations = random.sample(range(0,len(byte)), num_errors)
    for i in error_locations:
        corrupt_byte[i] = 1 if corrupt_byte[i] == 0 else 0
    return corrupt_byte




#### Main function to kick off the whole program.
def main():
    # Repeats 4 times, using 0, 1, 2, or 3 errors each time.
    for num_errors in range (0,4):
        print("Number of errors:  " + str(num_errors))

        ## Part 1a, generating byte and parity
        byte = genByte()
        parity_bit = genParity(byte)
        parity_byte = byte.copy()
        parity_byte.append(parity_bit)

        print("Transmitted byte:  ", end="")
        print(parity_byte)



        ## Part 1b, detecting errors
        received_byte = corruptByte(parity_byte, num_errors)
        print("Received Byte:     ", end="")
        print(received_byte)

        received_parity = received_byte[-1]
        print("Received Parity:   ", end="")
        print(received_parity)

        received_byte_noparity = received_byte.copy()
        received_byte_noparity.pop()
        calculated_parity = genParity(received_byte_noparity)
        print("Calculated Parity: ", end="")
        print(calculated_parity)


        match = 1 if received_parity == calculated_parity else 0
        if match == 1:
            print("No error detected.")
        else:
            print("Error detected!")

        print("")


if __name__ == "__main__":
    main()