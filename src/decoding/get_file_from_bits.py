from bitstring import Bits, BitArray

def get_file_from_bits(bits, filepath):
    print("Generating gzip of original file from bits...")
    
    bitstring = Bits(bin = bits)
    bitstring = BitArray(bitstring)
    
    
    with open(filepath, 'wb') as outfile:
        bitstring.tofile(outfile)
        
    del bitstring
    
    print("Successfully retrieved the zipped archive")