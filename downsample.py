import os
from PIL import Image

# Paths
input_folder = 'TextOCR\\train_val_images\\train_images'  # Folder where your original images are stored
output_folder = 'TextOCR\\train_val_images\sized_train_images'  # Folder where the downsampled images will be saved

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Downsample size (Width, Height)
target_size = (256, 256)  # Adjust this to the desired size

def downsample_images(input_dir, output_dir, size):
    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp')):  # Check for image files
            input_path = os.path.join(input_dir, filename)
            
            # Open the image
            with Image.open(input_path) as img:
                # Resize the image
                img_resized = img.resize(size, Image.Resampling.LANCZOS)
                
                # Save the resized image to the output directory
                output_path = os.path.join(output_dir, filename)
                img_resized.save(output_path)

                print(f"Saved downsampled image: {output_path}")

# Run the downsampling function
downsample_images(input_folder, output_folder, target_size)

print("Downsampling complete!")
