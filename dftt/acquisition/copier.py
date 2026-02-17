import hashlib
import shutil
import os

def secure_copy(source, destination):
    # Verify source file exists
    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist.")

    # Calculate SHA-256 hash of the source file
    sha256_hash = hashlib.sha256()
    with open(source,"rb") as f:
        # Read the file in chunks
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    sha256_digest = sha256_hash.hexdigest()

    # Copy the file
    shutil.copy2(source, destination)

    # Calculate SHA-256 hash of the copied file
    hash_of_copied = hashlib.sha256()
    with open(destination,"rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            hash_of_copied.update(byte_block)
    copied_digest = hash_of_copied.hexdigest()

    # Verify the hash
    if sha256_digest != copied_digest:
        raise ValueError("Hash verification failed: The copied file is not identical to the source file.")
    else:
        print("File copied successfully and verified.")

# Example usage
# secure_copy('path/to/source/file.txt', 'path/to/destination/file.txt')
