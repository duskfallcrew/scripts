import os
import argparse

def create_text_files(folder_path, words_to_insert):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip if it's already a text file
        if filename.endswith(".txt"):
            continue

        # Create a corresponding text file
        text_filename = f"{os.path.splitext(filename)[0]}.txt"
        text_file_path = os.path.join(folder_path, text_filename)

        # Open the text file and insert specified words
        with open(text_file_path, 'w') as text_file:
            text_file.write(f"{words_to_insert}\n")

def main():
    parser = argparse.ArgumentParser(description="Create text files for non-text files and insert specified words.")
    parser.add_argument("folder_path", help="Path to the folder containing non-text files")
    parser.add_argument("words_to_insert", help="Words to insert into each text file")

    args = parser.parse_args()
    create_text_files(args.folder_path, args.words_to_insert)

if __name__ == "__main__":
    main()
