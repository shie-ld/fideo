# bitstring module :  for the creation and analysis of binary data
from bitstring import BitArray

import os

# function : get binary representation of a file
def get_bitarray(INPUT):
    print("Converting " + os.path.basename(INPUT) + " to binary form...")
    
#   stores the hexdump of the file in a bitstring.BitArray object
    bitarray = BitArray(filename = INPUT)
#     print("Type: " ,type(bitarray))
#     print("Hexdump: ", bitarray)

    # removing the gzip file after deriving bitarray from it
    os.remove(INPUT + ".gz")
    
    print("Successfully converted " + os.path.basename(INPUT) + " to binary form")

#   returns the binary dump of file
#     print("Bindump: ", bitarray.bin)
    return bitarray.bin
    