import os
import argparse
import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def sanitize_path(path):
    """
    Sanitizes a file path to prevent directory traversal attacks.

    Args:
        path (str): The file path to sanitize.

    Returns:
        str: The sanitized file path.
    """
    # Resolve to an absolute path
    path = os.path.abspath(path)

    # Normalize the path to remove redundant separators and up-level references
    path = os.path.normpath(path)

    # Remove any potentially unsafe characters
    path = re.sub(r"[^a-zA-Z0-9_\-\\/.]", "", path)

    return path

def validate_template(template):
    """
    Validates a template string to ensure it only contains safe placeholders.

    Args:
        template (str): The template string to validate.

    Raises:
        ValueError: If the template contains unsafe placeholders.
    """
    # Define allowed placeholders
    allowed_placeholders = ["{filename}", "{words}"]

    # Find all placeholders in the template
    placeholders = re.findall(r"\{.*?\}", template)

    # Check if all placeholders are allowed
    for placeholder in placeholders:
        if placeholder not in allowed_placeholders:
            raise ValueError(f"Unsafe placeholder found in template: {placeholder}")

def create_text_files(folder_path, words_to_insert, append_mode=False, template=None, secure_permissions=False):
    """
    Creates or modifies text files corresponding to non-text files in a specified folder.

    Args:
        folder_path (str): Path to the folder containing files.
        words_to_insert (str): Words to insert into each text file.
        append_mode (bool): Whether to append to existing text files. Defaults to False (overwrite).
        template (str): A template string for inserting words, e.g., "File: {filename}\nWords: {words}".
        secure_permissions (bool): Whether to set secure file permissions (owner read/write only). Defaults to False.

    Raises:
        FileNotFoundError: If the folder does not exist.
        IOError: If there are issues reading or writing files.
        ValueError: If an unsafe template is used.
    """
    safe_folder_path = sanitize_path(folder_path)

    if not os.path.exists(safe_folder_path):
        raise FileNotFoundError(f"The specified folder '{safe_folder_path}' does not exist.")

    for filename in os.listdir(safe_folder_path):
        file_path = os.path.join(safe_folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        text_filename = f"{os.path.splitext(filename)[0]}.txt"
        text_file_path = os.path.join(safe_folder_path, text_filename)

        try:
            mode = "a" if append_mode and os.path.exists(text_file_path) else "w"
            with open(text_file_path, mode) as text_file:
                if template:
                    validate_template(template)
                    content = template.format(filename=filename, words=words_to_insert)
                else:
                    content = f"{words_to_insert}\n"
                text_file.write(content)

            # Set secure permissions if requested
            if secure_permissions:
                os.chmod(text_file_path, 0o600)

            logging.info(f"Processed '{filename}' -> '{text_filename}'")
        except IOError as e:
            logging.error(f"Error processing '{filename}': {e}")
        except ValueError as e:
            logging.error(f"Template error: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Create or modify text files for non-text files and insert specified words."
    )
    parser.add_argument("folder_path", help="Path to the folder containing non-text files")
    parser.add_argument("words_to_insert", help="Words to insert into each text file")
    parser.add_argument(
        "-a",
        "--append",
        action="store_true",
        help="Append to existing text files instead of overwriting",
    )
    parser.add_argument(
        "-t",
        "--template",
        type=str,
        help="Template string for inserting words (e.g., 'File: {filename}\\nWords: {words}')",
    )
    parser.add_argument(
        "-s",
        "--secure",
        action="store_true",
        help="Set secure file permissions (owner read/write only)",
    )

    args = parser.parse_args()

    try:
        create_text_files(
            args.folder_path,
            args.words_to_insert,
            append_mode=args.append,
            template=args.template,
            secure_permissions=args.secure,
        )
    except Exception as e:
        logging.error(e)
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
