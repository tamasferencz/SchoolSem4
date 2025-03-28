filename = input("Enter the name of the text file: ")

try:
    with open(filename, 'r') as file:
        contents = file.read()

        print("\nContents of the file:")
        print(contents)

        lines = contents.splitlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_characters = len(contents)

        print("\nFile statistics:")
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {num_characters}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")

except PermissionError:
    print(f"Error: You do not have permission to open the file '{filename}'.")
