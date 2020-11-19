from bitstring import Bits, BitArray

def get_file_from_bits(bits, OUTPUT):
    print("Generating file from bits...")
    
    bitstring = Bits(bin = bits)
    bitstring = BitArray(bitstring)
    
    
    with open(OUTPUT, 'wb') as outfile:
        bitstring.tofile(outfile)
        
    del bitstring
    
    print("Successfully retrieved the file")