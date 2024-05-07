from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_image_size_and_date(image_path):
    try:
        with Image.open(image_path) as img:

            file_type = img.format
            print(f"File Type: {file_type}")
            # Get the size of the image
            width, height = img.size
            print(f"Image Size: {width} x {height}")

            # Get the date created from EXIF data
            exif_data = img._getexif()
            if exif_data is not None and 36867 in exif_data:  # 36867 corresponds to DateTimeOriginal
                date_created = exif_data[36867]
                print(f"Date Created: {date_created}")
            else:
                print("Date Created information not found.")
    except Exception as e:
        print(f"Error: {e}")


# Example usage
image_path = r"C:\Users\Amanpreet Kaur\Desktop\upload\unnamed4.jpg"
get_image_size_and_date(image_path)
