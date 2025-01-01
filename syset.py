import os
import pandas as pd
import shutil
from sklearn.model_selection import train_test_split

# Paths
csv_file = '.\TextOCR\\annot.csv'  # Path to the annotation CSV file
image_folder = '.\TextOCR/train_val_images/train_images'  # Folder containing original images
output_image_folder = '.\TextOCR/train_val_images\sub_train_images'  # Folder to save the subset of images
output_csv_file = '.\TextOCR\\sub_annot.csv'  # New CSV file for the subset annotations

# Create the output image folder if it doesn't exist
os.makedirs(output_image_folder, exist_ok=True)

# Load the annotation CSV file
annot_df = pd.read_csv(csv_file)

# Randomly select 30% of the images
image_ids = annot_df['image_id'].unique()  # Get all unique image ids from the CSV
train_image_ids, _ = train_test_split(image_ids, train_size=0.3, random_state=42)  # Select 30% of the images

# Filter the annotations to keep only the selected images
subset_annot_df = annot_df[annot_df['image_id'].isin(train_image_ids)]

# Save the subset annotations to a new CSV file
subset_annot_df.to_csv(output_csv_file, index=False)

# Copy the corresponding images to the output folder
for image_id in train_image_ids:
    img_filename = f'{image_id}.jpg'  # Assuming the image files have .jpg extension
    src_path = os.path.join(image_folder, img_filename)
    dest_path = os.path.join(output_image_folder, img_filename)
    
    if os.path.exists(src_path):
        shutil.copy(src_path, dest_path)  # Copy the image to the new folder
        #print(f"Copied {img_filename}")
    else:
        print(f"Image {img_filename} not found in {image_folder}")

print(f"Subset of images and annotations created: {len(train_image_ids)} images and new CSV at {output_csv_file}")
