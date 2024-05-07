import os
from PIL import Image
from datetime import datetime

def get_image_metadata(directory_path):
    # Iterate through each file in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Check if the file is a regular file and not a subdirectory
        if os.path.isfile(file_path):
            try:
                with Image.open(file_path) as img:
                    # Extract folder name, file name, and title for the image
                    folder_name = os.path.basename(directory_path)
                    file_name = os.path.splitext(filename)[0]

                    # Attempt to get title from EXIF data
                    title = None
                    file_type = img.format
                    exif_data = img._getexif()
                    if exif_data is not None and 270 in exif_data:  # 270 corresponds to ImageDescription
                        title = exif_data[270]

                    description = None
                    if exif_data is not None and 270 in exif_data:  # Adjust this if description uses a different tag
                        description = exif_data[270]

                    date_created_timestamp = os.path.getctime(file_path)
                    date_modified_timestamp = os.path.getmtime(file_path)

                    # Format date in dd/mm/yyyy
                    date_created = datetime.fromtimestamp(date_created_timestamp).strftime('%d/%m/%Y')
                    date_modified = datetime.fromtimestamp(date_modified_timestamp).strftime('%d/%m/%Y')


                    # Print the information
                    print(f"Folder: {folder_name}")
                    print(f"File Name: {file_name}")
                    print(f"Title: {title or 'Not available'}")
                    print(f"FileType {file_type}")
                    print(f"description {description}")
                    print(f"date_created {date_created}")
                    print(f"date_modified {date_modified}")
                    print()

            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example usage
directory_path = r"C:\Users\Amanpreet Kaur\Desktop\upload"  # Replace with the actual directory path
get_image_metadata(directory_path)
