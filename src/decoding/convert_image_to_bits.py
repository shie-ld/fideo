from PIL import Image

def convert_image_to_bits(imagepath):
    image = Image.open(imagepath)
    width, height = image.size
    bits = ""
    pixels = image.load()
    del image
    
    for j in range(height):
        for i in range(width):
            pixel = pixels[i, j]
            pixel_bin_rep = "0"
            
#           if white difference is smaller then black difference, then 
#           pixel_bin_rep must be "1"
            if (abs(pixel[0] - 255) < abs(pixel[0] - 0)
            and abs(pixel[1] - 255) < abs(pixel[1] - 0)
            and abs(pixel[2] - 255) < abs(pixel[2] - 0)):
                pixel_bin_rep = "1"
                
            bits += str(pixel_bin_rep)
    del pixels
    return bits