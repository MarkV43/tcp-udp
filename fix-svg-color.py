import os

# Grab the names of all files from folder ./svgs
def files_from_folder(folder):
	files = []
	for file in os.listdir(folder):
		if file.endswith(".svg"):
			files.append(os.path.join(folder, file))
	return files

files = files_from_folder("./svgs")

# Loop through all files
for file in files:
	print(file)
	# Open file as read and write
	with open(file, 'r') as f:
		# Read the first line
		lines = f.readlines()
	lines[0] = lines[0].replace('<ns0:svg', '<ns0:svg fill="white"', 1)
	# Write the line back to the file
	with open(file, 'w') as f:
		f.writelines(lines)
