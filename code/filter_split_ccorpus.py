import os
import re
import sys

pattern = r'^@@\d+\s*'  

def clean_text(line):
    line = line.split(' ', 1)[-1]
    line = line.replace('<p>', '').replace('<h>', '')
    return line.strip()

def split_lines(input_file, output_dir):
    with open(input_file, 'r') as f:
        lines = f.readlines()
        
    output_file_count = 0

    for line in lines:
        if len(line) > 0:
            output_file = output_file = os.path.join(output_dir, f'output_{output_file_count}.txt')
            with open(output_file, 'w') as f:
                split = line.split('.')
                if split[0].startswith('@@'):
                    split[0] = re.sub(pattern, '', split[0])
                for sent in split:
                    cleanedsent = clean_text(sent)
                    if len(cleanedsent) > 3:
                        f.write(cleanedsent + ' .\n')
            output_file_count += 1
        

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python program.py input_file output_directory")
        sys.exit(1)

    input_file = sys.argv[1]
    output_dir = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Error: {input_file} does not exist or is not a file.")
        sys.exit(1)

    if not os.path.isdir(output_dir):
        print(f"Error: {output_dir} is not a valid directory.")
        sys.exit(1)

    split_lines(input_file, output_dir)
    print("Splitting complete.")
