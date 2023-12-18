from PIL import Image
import numpy as np

def add_white_background(image_path, output_path):
    # Open the image
    with Image.open(image_path) as img:
        # Get the size of the image
        h, w = img.size

        # Create a white background image
        white_background = Image.new('RGBA', (h, w), (255, 255, 255, 255))

        # Paste the original image onto the white background
        white_background.paste(img, (0, 0), img)

        # Save the new image
        white_background.save(output_path, format='PNG')

    return output_path
def create_mask_and_visualize(image_path, visualization_output_path):
    # Open the image
    with Image.open(image_path) as img:
        # Convert the image to a numpy array
        img_array = np.array(img)

        # Extract the alpha channel (assuming it's the fourth channel)
        alpha_channel = img_array[:, :, 3]

        # Create a mask, non-transparent parts as 1, transparent parts as 0
        mask = np.where(alpha_channel > 0, 1, 0)


        # For visualization, create a black and white image
        visualization = np.where(mask == 1, 255, 0).astype(np.uint8)
        Image.fromarray(visualization).convert('L').save(visualization_output_path)

    return visualization_output_path


def convert_transparency_to_color(image_path, output_path, color=(255, 255, 255)):
    """
    Convert transparent parts of a PNG image to a specified color.

    Parameters:
    image_path (str): Path to the input PNG image.
    output_path (str): Path where the output image will be saved.
    color (tuple): The color to replace the transparent parts with (default is white).
    """
    # Open the image
    with Image.open(image_path) as img:
        # Convert image to RGBA if it's not
        img = img.convert("RGBA")

        # Extract RGBA data
        data = img.getdata()

        # Replace transparent parts with the specified color
        newData = []
        for item in data:
            if item[3] == 0:  # Check if it's transparent
                newData.append(color + (255,))  # Replace with the color
            else:
                newData.append(item)

        # Update image data
        img.putdata(newData)

        # Save the new image
        img.save(output_path, "PNG")

    return output_path
# Example usage
# Assuming your image path is 'path/to/your/image.png'
# You can call this function and specify the output paths like so:
# create_mask_and_visualize('path/to/your/image.png', 'path/to/your/mask.png', 'path/to/your/visualization.png')

if __name__ == '__main__':
    #add_white_background('./working_card/card_edge.png', './working_card/card_edge_white.png')
    #create_mask_and_visualize('./working_card/card_mask.png',
                              #'./working_card/card_mask_vis.png')
    convert_transparency_to_color('./working_card/example_1.png','./working_card/example_1_white.png')