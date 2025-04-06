from image import Image
import math

# # Generated in part by genAI
def get_edge_pixels(image):
    """Returns the top and bottom pixel rows of an image strip."""
    top_pixels = []
    bottom_pixels = []
    for i in range(image.get_width()):
        top_pixels.append(image.get_pixel(0, i))  # Top row
        bottom_pixels.append(image.get_pixel(image.get_height() - 1, i))  # Bottom row
    return [top_pixels, bottom_pixels]

def find_distance_pixels(strip1, strip2):
    """Computes Euclidean distance between corresponding pixels in two rows."""
    distance = 0
    for i in range(len(strip1)):
        r1, g1, b1 = strip1[i].get_r(), strip1[i].get_g(), strip1[i].get_b()
        r2, g2, b2 = strip2[i].get_r(), strip2[i].get_g(), strip2[i].get_b()
        distance += math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)
    return distance

def find_bottom_strip(image_strips):
    """Finds the strip whose bottom row has the most empty white space."""
    """I noticed that the bottom strip was mostly whitespace so in this case, 
        this is the best way to determine which is the bottom strip"""
    bottom_strip = None
    biggest = -1

    for strip in image_strips:
        white_count = 0
        strip_bottom = get_edge_pixels(strip)[1]
        for pixel in strip_bottom:
            if pixel.get_r() == 0 and pixel.get_g() == 0 and pixel.get_b() == 0:
                white_count += 1
        if white_count > biggest:
            biggest = white_count
            bottom_strip = strip

    return bottom_strip
def find_similar_above_strip(strip, image_strips):
    """Finds the closest matching strip that should go directly above the given strip."""
    min_distance = float('inf')
    best_match = None

    for other_strip in image_strips:
        if strip != other_strip:
            distance = find_distance_pixels(get_edge_pixels(other_strip)[1], get_edge_pixels(strip)[0])  # Match top-to-bottom
            if distance < min_distance:
                min_distance = distance
                best_match = other_strip

    return best_match


def stitch_images(ordered_strips, Image):
    """Merge ordered strips into a single image in the correct order."""
    width, height = ordered_strips[0].get_width(), ordered_strips[0].get_height() * len(ordered_strips)
    final_image = Image(width, height)

    for idx, strip in enumerate(ordered_strips):
        for r in range(strip.get_height()):
            for c in range(strip.get_width()):
                final_image.set_pixel(idx * strip.get_height() + r, c, strip.get_pixel(r, c))

    return final_image




def main():
    """Main function to reconstruct the shredded image."""
    image_strips = [Image.read_bmp(f'images/image_strip_{i}.bmp') for i in range(16)]

    # Find the bottom-most strip
    bottom_strip = find_bottom_strip(image_strips)
    ordered_strips = [bottom_strip]
    remaining_strips = set(image_strips) - {bottom_strip}  # Use set for efficiency

    # Iteratively find and prepend the closest matching strip (above)
    while len(ordered_strips) < len(image_strips):
        last_strip = ordered_strips[0]  # The current bottom-most strip
        similar_above = find_similar_above_strip(last_strip, remaining_strips)

        if similar_above:
            ordered_strips.insert(0, similar_above)  # Insert at the front
            remaining_strips.remove(similar_above)
    
    # Stitch the ordered strips together
    final_image = stitch_images(ordered_strips, Image)
    final_image.save_bmp('reconstructed_image.bmp')
    print("Reconstructed image saved as 'reconstructed_image.bmp'")

main()




