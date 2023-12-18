import os
import zipfile

class ZipImagesNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_folder": ("STRING", {"default": "/path/to/images", "multiline": False}),
                "output_zip": ("STRING", {"default": "/path/to/output.zip", "multiline": False}),
            }
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "execute"

    def execute(self, input_folder, output_zip):
        try:
            # Ensure the input folder exists
            if not os.path.exists(input_folder):
                raise ValueError(f"Input folder '{input_folder}' does not exist.")

            # Create a zip file and add images from the folder
            with zipfile.ZipFile(output_zip, 'w') as zip_file:
                for root, dirs, files in os.walk(input_folder):
                    for file in files:
                        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, input_folder)
                            zip_file.write(file_path, arcname=arcname)

            success_notification = f"Images in '{input_folder}' zipped successfully. Output: '{output_zip}'"
            return (success_notification,)
        except Exception as e:
            # Handle errors gracefully
            return (str(e),)
