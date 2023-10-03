from helper_functions import *
#-----------------------FILL IN THE FOLDER WHERE YOUR IMAGE EXISTS--------------------------
# Please change the path of images according to your system image location
datafolder = "/Users/expansionislife/Documents/BTH Python Assignments/Assignment-1/assgn1code/images/"
imgpath =  datafolder + '6.jpg'
#----------------------------------------STARTER CODE----------------------------------------
# Convert the color image to grayscale and returns the grayscale pixels 
pixel_values = read_colorimg(imgpath)
# The returned pixel values INCLUDE 2 boundary rows and 2 boundary colns. Therefore,
numb_rows = len(pixel_values) - 2
numb_colns = len(pixel_values[0]) - 2
#
#----------------------------------------WRITE YOUR CODE HERE----------------------------------------
# Create a data structure to store updated pixel information

new_pixel_values = [[0] * numb_colns for _ in range(numb_rows)]

# Define the 3 x 3 mask as a tuple of tuples
mask = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]

# Implement a function to slice a part from the image as a 2D list
def get_slice_2d_list(pix_values, row_s, col_s):
    neighbouring_pixels = []
    for x in range(row_s - 1, row_s + 2):
        row_pixels = []
        for y in range(col_s - 1, col_s + 2):
            row_pixels.append(pix_values[x][y])
        neighbouring_pixels.append(row_pixels)
    return neighbouring_pixels

# Implement a function to flatten a 2D list or a 2D tuple
def flatten(d_list):
    temp_lst = []
    for sublist in d_list:
        for items in sublist:
            temp_lst.append(items)
    return temp_lst

# multiply the values of neighboring pixels and mask values
def multiply(temp1:int,temp2:int):
    result_1 = temp1*temp2
    return result_1

for row in range(1, numb_rows + 1):
    for col in range(1, numb_colns + 1):
        # Create little local 3x3 box using list slicing
        neighbour_pixels = get_slice_2d_list(pixel_values, row, col)

        # Apply the mask
        neighbour_pixels_flattening = flatten(neighbour_pixels)
        #print("**********TESTING********")
        #print(neighbour_pixels_flattening)
        # Apply the mask
        mask_flattening = flatten(mask)
       #print("**********TESTING********")
        #print(mask_flattening)
        
        #Multiply the neighbour_pixels_flattening and mask_flattening
        mult_result = map(multiply, neighbour_pixels_flattening, mask_flattening)
        
        # Sum all the multiplied values and set the new pixel value
        total_value = 0
        for item in mult_result:
            total_value += item
        print(total_value)
        #For testing wether the values are being added are not!!!!!
        new_pixel_values[row - 1][col - 1] = total_value

# Verify your result
verify_result(pixel_values, new_pixel_values, mask)
# View the original image and the edges of the image
view_images(imgpath, new_pixel_values)
