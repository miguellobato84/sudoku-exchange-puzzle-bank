import os

# Define the paths to your text files
file_names = ["easy.txt", "medium.txt", "hard.txt", "diabolical.txt"]
data = {}


# Function to read a single file
def read_file(file_path):
    entries = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:  # Ensure the line has the expected three parts
                yield [parts[0], parts[1], parts[2]]


# Read each file and store its contents in the data dictionary
for file_name in file_names:
    if os.path.exists(file_name):  # Ensure the file exists before trying to read it
        data[file_name.split(".")[0]] = read_file(file_name)
    else:
        print(f"File {file_name} does not exist.")

# Print the data for verification
opened_files = {}
count = {}
for category, entries in data.items():
    for entry in entries:
        rating = entry[2]
        if rating not in opened_files:
            opened_files[rating] = open(f"{rating}.txt", "w")
            count[rating] = 0
        opened_files[rating].write(" ".join(entry) + "\n")
        count[rating] += 1

print("| Filename            | Difficulty Rating | Total Entries       |")
print("| ------------------- | ----------------- | ------------------- |")
for key in sorted(opened_files.keys()):
    opened_files[key].close()
    # Print the file name (and a link to the file), difficulty rating, and total entries
    print(f"| [{key}.txt](./{key}.txt) | {key} | {count[key]} |")
