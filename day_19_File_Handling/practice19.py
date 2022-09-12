# ----------------------File Handling-------------------------

#-------------Open() built-in function----------------
# to handle data
# syntax
# open('filename', mode)  mode(r, a, w, x, t, b)

# r: Read. Opens a file for reading, it returns an error if the file does not exist.
# a: Append. Opens a file for appending, creates the file if it does not exist.
# w: Write. Opens a file for writing, creates the file if it does not exist.
# x: Create. Creates the specified file, return an error if the file exist.
# t: Text. Default value. Text mode
# b: Binary. Binary mode. (images)

#----------------Opening files for reading ----------------------
# the deafult mode of open is reading
# To open file I have created and saved a file named reading_file.txt in the file directory
f = open('./reading_file.txt')
print(f) 
 