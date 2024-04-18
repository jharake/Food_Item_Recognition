import os
from PIL import Image
import csv
import numpy as np

input_directory = 'data'
output_directory = 'data_processed'
csv_file = 'data.csv'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

min_size = 256

# Create a CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['label', 'array'])  # Write header row

    for folder in range(1, 10):
        input_folder = os.path.join(input_directory, str(folder))
        output_folder = os.path.join(output_directory, str(folder))

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        image_files = [f for f in os.listdir(input_folder) if f.endswith('.jpg') or f.endswith('.png')]

        for image_file in image_files:
            image = Image.open(os.path.join(input_folder, image_file))
            width, height = image.size
            left = (width - min_size) // 2
            top = (height - min_size) // 2
            right = left + min_size
            bottom = top + min_size
            cropped_image = image.crop((left, top, right, bottom))
            resized_image = cropped_image.resize((min_size, min_size))
            grayscale_image = resized_image.convert('L')  # Convert to grayscale
            image_array = np.array(grayscale_image,dtype=np.uint8).flatten()  # Flatten the array
            output_path = os.path.join(output_folder, image_file)
            cropped_image.save(output_path)

            # # Write image path, label, and flattened array to CSV file
            # writer.writerow([str(folder), str(image_array.tolist())])
