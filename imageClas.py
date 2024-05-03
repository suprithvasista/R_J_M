
import os

file_path = "/Users/suprithm/Downloads/en.openfoodfacts.org.products (1).csv"  # Replace with the actual file path
max_size = 1 * 1024 * 1024 * 1024  # 1GB in bytes

file_size = os.path.getsize(file_path)
if file_size > max_size:
    with open(file_path, 'rb') as file:
        chunk_size = 1 * 1024 * 1024 * 1024  # 1MB chunk size
        num_chunks = file_size // chunk_size + 1

        for i in range(num_chunks):
            output_path = f"/Users/suprithm/DataSet/file_part{i}.csv"
            with open(output_path, 'wb') as output_file:
                chunk = file.read(chunk_size)
                output_file.write(chunk)

    print("File split successfully.")
else:
    print("File does not need to be split.")