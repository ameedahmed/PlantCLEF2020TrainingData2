from mpi4py import MPI
import os
import shutil
from PIL import Image, ExifTags
import csv

def main():
    
    file_path_new = 'herbarium_photo_associations'
    # Gather the list of all image files
    img_files = []
    for subfolder in os.listdir(file_path_new):
        subfolder_path = os.path.join(file_path_new, subfolder)
        if os.path.isdir(subfolder_path):
            for file in os.listdir(subfolder_path):
                if file.endswith(".jpg"):
                    img_files.append(os.path.join(subfolder_path, file))
        else:
            print(f"{subfolder_path}| is not a directory")
    print(f"Found {len(img_files)} image files")

    # Process image files assigned to this process
    csv_filename = "HerbariumPhotoAssociationsImageInformation.csv"
    image_data = []
    i = 1
    print(img_files)
    for file in img_files:
        print(f"Processing file {i} of {len(img_files)}")
        i += 1
        try:
            with Image.open(file) as img:
                width, height = img.size
                image_data.append([file, width, height, img.info.get("dpi")])
                #shutil.move(file, destination_path)
                #print(f"Image {width} and {height} moved to")
                
        except Exception as e:
            print(f"Error processing file {file}: {e}")
    csv_headers = ["Filename", "Width", "Height","DPI Information"]
    with open(csv_filename,mode = "w",newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(csv_headers)
        writer.writerows(image_data)     
    
if __name__ == "__main__":
    main()