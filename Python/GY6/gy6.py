# Task "File Handling with Exceptions"

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



# Task "File Explorer with Python's os module"

import os

directory = input("Enter a directory path: ")

try:
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
    else:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    file_size = os.path.getsize(entry.path)
                    print(f"File: {entry.name} - Size: {file_size} bytes")
                elif entry.is_dir():
                    num_files = len([f for f in os.listdir(entry.path) if os.path.isfile(os.path.join(entry.path, f))])
                    print(f"Directory: {entry.name} - Files: {num_files}")
except Exception as e:
    print(f"An error occurred: {e}")


# Task "Event Countdown"

from datetime import datetime

event_date_str = input("Enter the event date (YYYY-MM-DD): ")

try:
    event_date = datetime.strptime(event_date_str, "%Y-%m-%d")
    current_date = datetime.now()

    days_left = (event_date - current_date).days

    if days_left > 0:
        print(f"There are {days_left} days left until the event.")
    elif days_left == 0:
        print("The event is today!")
    else:
        print(f"The event was {-days_left} days ago.")

except ValueError:
    print("Invalid date format. Please enter the date as YYYY-MM-DD.")