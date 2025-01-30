import os
import zipfile
import folder_paths
from datetime import datetime

# In theory zips images, this is a "NOt likely needed" node, buti wanted to update it's code anyways, but it won'y go on K/N

class ZipImages:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "filename_prefix": ("STRING", {
                    "default": "my_archive"
                }),
            }
        }

    RETURN_TYPES = ()
    OUTPUT_NODE = True
    CATEGORY = "image"
    FUNCTION = "zip_images"

    def zip_images(self, filename_prefix):
        # Create a zip file with a timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        zip_filename = f"{filename_prefix}_{timestamp}.zip"
        zip_path = os.path.join(self.output_dir, zip_filename)

        image_extensions = (".png", ".jpg", ".jpeg", ".gif", ".webp")  # Add more if needed

        try:
            with zipfile.ZipFile(zip_path, 'w') as zip_file:
                for filename in os.listdir(self.output_dir):
                    if filename.lower().endswith(image_extensions):
                        file_path = os.path.join(self.output_dir, filename)
                        zip_file.write(file_path, arcname=filename)

            print(f"\033[92mImages zipped successfully: {zip_path}\033[0m") #Success message in green
            return ()
        except Exception as e:
            print(f"\033[91mError creating zip file: {e}\033[0m") #Error message in red
            return ()

# Register the node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "ZipImages": ZipImages
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ZipImages": "Zip Images"
}
