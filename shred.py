import os
import binascii
import random
import shutil


# Define the 35-pass Gutmann method
gutmann_method = [0x55, 0xAA, 0x92, 0x49, 0x24, 0x12, 0x49, 0x24, 0x92, 0x49, 0x24, 0x55,
0xAA, 0x92, 0x49, 0x24, 0x12, 0x49, 0x24, 0x92, 0x49, 0x24, 0x55, 0xAA, 0x92, 0x49, 0x24,
0x12, 0x49, 0x24, 0x92, 0x49, 0x24, 0x00, 0x00, 0x00]


def random_shred_file(filename, passes=10):
    print(f"Shredding file {filename}")
    fileSize = os.path.getsize(filename)
    for _ in range(passes):
        # Write random bytes to the file
        random_bytes = os.urandom(fileSize)
        with open(filename, "wb") as f:
            f.write(random_bytes)
    print(f"Shredding file {filename} completed!")

def random_shred_directory(directory, passes=10):
    #   directory (str): The path to the directory to be shredded.
    #  passes (int): The number of passes for overwriting the files.
    for i in os.listdir(directory):
        path = os.path.join(directory, i)
        if os.path.isdir(path):
            # The path is a directory, execute this function again with the directory path
            print(f"Shredding directory {i}")
            random_shred_directory(path, passes)
            print("Done!")
            continue
        try:
            random_shred_file(path, passes)
        except Exception as e:
            print(f"Skipping file {path} due to error: {e}")
            

def shred_file_gutmann(file_path):
    # Open the file in binary mode
    with open(file_path, "rb") as file:
        # Get the size of the file
        file_size = os.path.getsize(file_path)

        # Overwrite the file with the Gutmann method
        for i in range(len(gutmann_method)):
            file.seek(0)
            for j in range(file_size):
                file.write(bytes([gutmann_method[i]]))


def shred_folder_gutmann(folder_path):
    # Delete the folder and its contents with the Gutmann method
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Shred each file with the 3-pass DoD 5220.22-M method
            shred_file_gutmann(file_path)

    
    
def shred_file_dod(file_path):
    # Define the 3-pass DoD 5220.22-M method
    dod_method = [0x00, 0xFF, 0x00]

    # Open the file in binary mode
    with open(file_path, "rb+") as file:
        # Get the size of the file
        file_size = os.path.getsize(file_path)

        # Overwrite the file with the DoD 5220.22-M method
        for i in range(len(dod_method)):
            file.seek(0)
            for j in range(file_size):
                file.write(bytes([dod_method[i]]))
    

def shred_folder_dod(folder_path):
    # Iterate through all files in the directory
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Shred each file with the 3-pass DoD 5220.22-M method
            shred_file_dod(file_path)

    
    
def overwrite_hex_values(file_path, passes=3):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()

            # Convert the content to hexadecimal representation
            hex_content = binascii.hexlify(content)
            for _ in range(passes):
                # Choose random positions to overwrite
                positions = [random.randint(0, len(hex_content) - 2) for _ in range(len(hex_content) // 2)]

                # Overwrite the chosen positions with random hex values
                for pos in positions:
                    hex_content = hex_content[:pos] + format(random.randint(0, 255), '02x').encode() + hex_content[pos + 2:]

            # Convert the modified hexadecimal content back to bytes
            new_content = binascii.unhexlify(hex_content)

            # Write the modified content back to the file
            with open(file_path, 'wb') as output_file:
                output_file.write(new_content)

        print(f"File '{file_path}' hex values overwritten securely.")
    except Exception as e:
        print(f"Error overwriting hex values for file '{file_path}': {e}")


def Hybrid_shredFile(file_path):
    random_shred_file(file_path)
    shred_file_gutmann(file_path)
    shred_file_dod(file_path)
    overwrite_hex_values(file_path)
   
    
def Hybrid_shredDirectory(directory):
    random_shred_directory(directory)
    shred_folder_gutmann(directory)
    shred_folder_dod(directory)