### Part 1 of lab
## Part 1a
# Write a program (in any language, such as C, C++, Java, JavaScript, or Python)
# that generates a parity bit (even or odd - you choose)
# for each byte of data and verify its correct operation.*
## Part 1b
# Write another program to detect correct data based on the parity you have defined.
# Then use the program to generate a byte of data along with the parity bit (9-bits total),
# and observe what happens when there are 0, 1, 2, or 3 bits in error in a given byte.
# Include a screenshot of the results (command line or other) and discuss the probability of an undetected error occurring.
import random

def get_parity(byte):
    count_ones = byte.count('1')
    if count_ones % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"
        
    return parity
    
def set_parity_bit(parity):
    if parity == "Odd":
        parity_bit = '1'
    else:
        parity_bit = '0'
    return parity_bit

def generate_byte():
    byte = ""
    for i in range(8):
        byte += str(random.randint(0,1))
    return byte

def generate_errors(num_errors, byte):
    error_byte = byte
    for i in range (num_errors):
        if byte[i] == '0':
            error_byte = error_byte[:i] + '1' + error_byte[i + 1:]
        else:
            error_byte = error_byte[:i] + '0' + error_byte[i + 1:]
    return error_byte
    
    
def main():
    byte = generate_byte()
    print("Byte: " + byte)
    
    parity = get_parity(byte)
    parity_bit = set_parity_bit(parity)
    print("Parity Bit: " + parity_bit)
    
    num_errors = int(input("\nEnter number of errors (0-8): "))
    if num_errors == 0:
        print("\nNo errors generated\n")
    elif num_errors > 8:
        print("\nInvalid number of errors\n")
    else:
        error_byte = generate_errors(num_errors, byte)
        print("\nByte with errors: " + error_byte)
        
        error_parity = get_parity(error_byte)
        error_parity_bit = set_parity_bit(error_parity)
        print("Parity Bit: " + error_parity_bit)
        
        if error_parity_bit == parity_bit:
            print("No error detected\n")
        else:
            print("Error detected\n")
     
         
if __name__ == "__main__":
    main()