#Name: Itai Lavie
#Email: itai.lavie47@myhunter.cuny.edu
#Date: March 24, 2024
#This program completes assignment 32

from PIL import Image

def main():
    # Ask the user for the input and output file names
    input_image_name = input("Enter image file name: ")
    output_image_name = input("Enter output file: ")
    
    # Open the input image
    with Image.open(input_image_name) as img:
        # Calculate the dimensions for the lower left quarter
        width, height = img.size
        new_width = width // 2
        new_height = height // 2
        
        # Crop the image to the lower left quarter
        # The box is defined by (left, upper, right, lower)
        cropped_img = img.crop((0, new_height, new_width, height))
        
        # Save the cropped image to the output file
        cropped_img.save(output_image_name)

if __name__ == "__main__":
    main()