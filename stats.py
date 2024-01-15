import json
from tabulate import tabulate
import glob

# Load the keystrokes data from all JSON files
def load_keystrokes_from_files():
    keystrokes_data = {}
    file_list = glob.glob("keystrokes_*.json")
    file_list = glob.glob("keystrokes_2023-07-14_15-08-21*.json")
    
    for filename in file_list:
        with open(filename, "r") as file:
            data = json.load(file)
            for key, count in data.items():
                if key in keystrokes_data:
                    keystrokes_data[key] += count
                else:
                    keystrokes_data[key] = count
    return keystrokes_data

# Sort the keystrokes by most occurrences
def sort_keystrokes(keystrokes_data):
    sorted_keystrokes = sorted(keystrokes_data.items(), key=lambda x: x[1], reverse=True)
    return sorted_keystrokes

# Create a table from the sorted keystrokes
def create_table(sorted_keystrokes):
    table = []
    for key, count in sorted_keystrokes:
        table.append([key, count])
    return table

# Write the table to a file
def write_table_to_file(table):
    with open("keystrokes_table.txt", "w") as file:
        file.write(tabulate(table, headers=["Key", "Occurrences"], tablefmt="grid"))

# Load the keystrokes data from all JSON files
keystrokes_data = load_keystrokes_from_files()

# Sort the keystrokes by most occurrences
sorted_keystrokes = sort_keystrokes(keystrokes_data)

# Create a table from the sorted keystrokes
table = create_table(sorted_keystrokes)

# Write the table to a file
write_table_to_file(table)
