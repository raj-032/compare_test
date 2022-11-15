# Python program to explain filecmp.cmpfiles() method

# importing filecmp module
import filecmp
print('hi')
# Path of first directory
dir1 = "/home / User / Documents"

# Path of second directory
dir2 = "/home / User / Desktop"

# Common files
common = ["file1.txt", "file2.txt", "file3.txt"]

# Shallow compare the files
# common in both directories
match, mismatch, errors = filecmp.cmpfiles(dir1, dir2, common)

# Print the result of
# shallow comparison
print("Shallow comparison:")
print("Match :", match)
print("Mismatch :", mismatch)
print("Errors :", errors, "\n")


# Compare the
# contents of both files
# (i.e deep comparison)
match, mismatch, errors = filecmp.cmpfiles(dir1, dir2, common,
											shallow = False)

# Print the result of
# deep comparison
print("Deep comparison:")
print("Match :", match)
print("Mismatch :", mismatch)
print("Errors :", errors)

import os

# path of the directory
directoryPath = "D:\project1"

# Checking the boolean value of list
if not os.listdir(directoryPath):
	print("No files found in the directory.")
else:
	print("Some files found in the directory.")



# Python program to check if
# the directory is empty

import os


# Function for checking if the directory
# containes file or not
def isEmpty(directoryPath):

	# Checking if the directory exists or not
	if os.path.exists(directoryPath):

		# Checking if the directory is empty or not
		if len(os.listdir(directoryPath)) == 0:
			return "No files found in the directory."
		else:
			return "Some files found in the directory."
	else:
		return "Directory does not exist !"

# Driver's code

# Valid directory
directoryPath = "D:\project1"
print("Valid path:", isEmpty(directoryPath))

# Invalid directory
directoryPath = "D:\project2"
print("valid path:", isEmpty(directoryPath))


# import OS module
import os

# Get the list of all files and directories
path = "D:\project1"
project1 = os.listdir(path)

print("Files and directories in '", path, "' :")

# prints all files
print(project1)

path = "D:\project2"
project2 = os.listdir(path)

print("Files and directories in '", path, "' :")

# prints all files
print(project2)
print("__________________________________________________")

#
# project2_missed_files = (project1) - (project2)
# print(project2_missed_files)
#
# project1_missed_files = project2 - project1
# print(project1_missed_files)
#
#
# common_dirs = (project1 and project2)
# print(common_dirs)


# import filecmp
# file1 = "D:\project1"
# file2 = "D:\project2"
# dc = filecmp.dircmp("D:\project1","D:\project2")
# print(dc.report_full_closure())




import filecmp
file1 = "E:\\like"
file2 = "D:\\like"
dc = filecmp.dircmp("E:\\like","D:\\like")
print(dc.report_full_closure())

















# Python program to explain filecmp.cmpfiles() method

# importing filecmp module
# import filecmp
#
# # Path of first directory
# project1 = "D:\project1"
#
# # Path of second directory
# project2 = "D:\project2"
#
# # Common files
# common = ["sample1.txt", "sample2.txt", "sample3.txt"]
#
# # Shallow compare the files
# # common in both directories
# match, mismatch, errors = filecmp.cmpfiles(project1, project2, common)
#
# # Print the result of
# # shallow comparison
# print("Shallow comparison:")
# print("Match :", match)
# print("Mismatch :", mismatch)
# print("Errors :", errors, "\n")
#
#
# # Compare the
# # contents of both files
# # (i.e deep comparison)
# match, mismatch, errors = filecmp.cmpfiles(dir1, dir2, common,
# 											shallow = True)
#
# # Print the result of
# # deep comparison
# print("Deep comparison:")
# print("Match :", match)
# print("Mismatch :", mismatch)
# print("Errors :", errors)







