import os
import sys

def split_file(file_path, max_size=90 * 1024 * 1024):
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return

    file_size = os.path.getsize(file_path)
    if file_size <= max_size:
        print(f"File size is already within the limit ({file_size} bytes). No split needed.")
        return

    base_name = os.path.basename(file_path)
    dir_name = os.path.dirname(file_path)
    part_num = 1
    bytes_written = 0
    part_file = None

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if part_file is None:
                    part_path = os.path.join(dir_name, f"{base_name}.part{part_num}")
                    part_file = open(part_path, 'w', encoding='utf-8')
                    print(f"Creating: {part_path}")

                part_file.write(line)
                bytes_written += len(line.encode('utf-8'))

                if bytes_written >= max_size:
                    part_file.close()
                    part_file = None
                    part_num += 1
                    bytes_written = 0

            if part_file:
                part_file.close()
                print(f"Created part {part_num}.")

        print("Splitting completed successfully.")

    except Exception as e:
        print(f"An error occurred during splitting: {e}")
        if part_file:
            part_file.close()

def merge_files(part_file_path):
    if not os.path.isfile(part_file_path):
        print(f"Error: Part file '{part_file_path}' does not exist.")
        return

    base_name = os.path.basename(part_file_path)
    if '.part' not in base_name:
        print("Error: The specified file does not appear to be a split part file.")
        return

    original_file_name = base_name.split('.part')[0]
    dir_name = os.path.dirname(part_file_path)
    merged_file_path = os.path.join(dir_name, original_file_name)

    part_num = 1
    try:
        with open(merged_file_path, 'w', encoding='utf-8') as merged_file:
            while True:
                part_path = os.path.join(dir_name, f"{original_file_name}.part{part_num}")
                if not os.path.isfile(part_path):
                    break

                print(f"Merging: {part_path}")
                with open(part_path, 'r', encoding='utf-8') as part_file:
                    for line in part_file:
                        merged_file.write(line)

                part_num += 1

        print(f"Merging completed successfully. Merged file: {merged_file_path}")

    except Exception as e:
        print(f"An error occurred during merging: {e}")

def print_usage():
    print("Usage:")
    print("  To split a file:")
    print("    python file_split_merge.py split path/to/your/largefile.txt")
    print("")
    print("  To merge files:")
    print("    python file_split_merge.py merge path/to/largefile.txt.part1")

def main():
    if len(sys.argv) != 3:
        print("Error: Incorrect number of arguments.")
        print_usage()
        sys.exit(1)

    mode = sys.argv[1].lower()
    file_path = sys.argv[2]

    if mode == 'split':
        split_file(file_path)
    elif mode == 'merge':
        merge_files(file_path)
    else:
        print(f"Error: Unknown mode '{mode}'.")
        print_usage()
        sys.exit(1)

if __name__ == "__main__":
    main()
