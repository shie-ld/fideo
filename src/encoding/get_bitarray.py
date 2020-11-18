# bitstring module :  for the creation and analysis of binary data
from bitstring import BitArray

# function : get binary representation of a file
def get_bitarray(filepath):
    print("Converting " + os.path.basename(filepath) + " to binary form...")
    
#   stores the hexdump of the file in a bitstring.BitArray object
    bitarray = BitArray(filename = filepath)
#     print("Type: " ,type(bitarray))
#     print("Hexdump: ", bitarray)
    
    print("Successfully converted " + os.path.basename(filepath) + " to binary form")

#   returns the binary dump of file
#     print("Bindump: ", bitarray.bin)
    return bitarray.bin
    